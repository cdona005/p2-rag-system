"""Reranker (stage 1): ask Claude to reorder a first-stage system's top 20 candidates.

It is rerank_one() of the 13 lab's pipeline.py, over this repo's systems:
- the first stage is [rerank] first_stage of p2.toml (default "hybrid"), built through
  p2.retrievers.build so its index is made once per run; its top [rerank] candidates (default 20)
  are shown to Claude as numbered passages [1] to [n], each cut to [rerank] passage_chars characters;
- ONE p2.claude.call per query forces the reply into {"order": [n numbers]}; the schema is built
  from the real number of candidates n, and its items run from 1 to n, so Claude cannot answer with
  a number that names no passage;
- a reply that is missing, has an error, or is not each of 1 to n exactly once keeps the
  first-stage order of the candidates (the lab's behavior), and a warning is printed;
- results below the top n keep their first-stage order underneath, so a run file of k lines is
  always full; a reranker can only reorder its candidates, so a relevant document the first stage
  ranked below the top n cannot be rescued.

The passage of a document. In "chunk" mode (the default) the passage of a document is the chunk of
it that the first stage ranks best for the query (its best-matching 300 words, with the title put
in front when the chunk is not the first), because a document of the own corpus is a 12,000
character notice whose first 2,000 characters are mostly letterhead and addressees. A document the
first stage has no chunk ranking for gets its first passage_chars characters instead, which is also
what passage = "doc" gives. In `search_chunks` the passage of a candidate is its chunk.

Replies are cached by p2.claude.call (.cache/claude/, keyed on the model, schema and prompt).
`p2 run --fresh` and `--repeat N` set cfg.cache_claude to False, p2.claude.cache_folder(cfg) then
returns None, and every call asks Claude again; this file reads the folder from the cfg it was
built with, so it follows without any code of its own.

NEEDS_CLAUDE = True tells p2 that searching calls claude -p, so CI never regenerates this system's
runs: they are produced on your machine and committed with their traces.
"""

from __future__ import annotations

from p2 import claude, retrievers

NEEDS_CLAUDE = True

DEFAULT_FIRST_STAGE = "hybrid"  # [rerank] first_stage in p2.toml overrides it
DEFAULT_CANDIDATES = 20  # [rerank] candidates; the 13 lab reranks 20
DEFAULT_PASSAGE_CHARS = 2500  # [rerank] passage_chars; a 300-word chunk is about 2,000 characters on the shared corpus and up to about 2,500 on the NRC notices

# The prompt Claude gets. {n} is the number of candidates, {query} the query text, {passages} the
# numbered passages. Edit the wording here; a changed prompt is a new call, so saved replies of the old one are not reused.
RERANK_PROMPT = """Below are {n} passages from a collection of technical regulatory documents, numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def rerank_schema(n: int) -> dict:
    """The JSON schema of the reply: {"order": [n integers]}, each between 1 and n (counting from 1)."""
    return {
        "type": "object",
        "properties": {"order": {"type": "array", "items": {"type": "integer", "minimum": 1, "maximum": n}, "minItems": n, "maxItems": n}},
        "required": ["order"],
    }


def valid_order(order, n: int) -> bool:
    """True when `order` is a list holding each of 1 to n exactly once (booleans and floats do not count)."""
    return isinstance(order, list) and all(type(i) is int for i in order) and sorted(order) == list(range(1, n + 1))


def pairs(ids: list[str]) -> list[tuple[str, float]]:
    """(id, score) pairs for ids in their final order, best first.

    The score falls with the rank: (total - rank) / total, with rank counting from 0, so the best
    id scores 1.0. The scores are all different at six decimals (the precision of a run file), so
    ordering them by score, as p2 does, never moves an id.
    """
    total = len(ids)
    return [(i, (total - rank) / total) for rank, i in enumerate(ids)]


class Rerank:
    def __init__(self, corpus, cfg):
        """Build the first stage and read the [rerank] settings."""
        self.corpus = corpus
        self.cfg = cfg
        table = cfg.table("rerank")
        self.first_name = str(table.get("first_stage", DEFAULT_FIRST_STAGE))
        self.candidates = int(table.get("candidates", DEFAULT_CANDIDATES))
        self.passage_chars = int(table.get("passage_chars", DEFAULT_PASSAGE_CHARS))
        self.passage_mode = str(table.get("passage", "chunk"))  # "chunk" (best chunk of a document) or "doc" (start of the document)
        if self.first_name == "rerank":
            raise ValueError("[rerank] first_stage cannot be rerank itself; use hybrid, dense or bm25.")
        # candidates must be at least 2: with one candidate there is nothing to reorder, no call is made,
        # and p2 check would then find a rerank run that records no Claude call.
        if self.candidates < 2 or self.passage_chars < 1 or self.passage_mode not in ("chunk", "doc"):
            raise ValueError(f'[rerank] in p2.toml needs candidates >= 2, passage_chars >= 1 and passage = "chunk" or "doc"; got candidates = {self.candidates}, passage_chars = {self.passage_chars}, passage = {self.passage_mode!r}.')
        self.first = retrievers.build(self.first_name, corpus, cfg)
        self.model = cfg.model  # recorded in traces
        self.chunk_text = corpus.chunk_texts(cfg.chunk_words, cfg.chunk_overlap)
        self.n_chunks = len(self.chunk_text)

    def passage(self, chunk_id: str) -> str:
        """The text of one chunk, cut to passage_chars; a chunk that is not a document's first gets the title in front."""
        text = self.chunk_text[chunk_id]
        if not chunk_id.endswith("#0"):
            doc = self.corpus.docs[chunk_id.rsplit("#", 1)[0]]
            text = f"# {doc.title}\n\n{text}"
        return text[: self.passage_chars]

    def best_chunks(self, text: str) -> dict[str, str]:
        """{docid: chunk id of the document's best chunk for this query}, by the first stage's chunk ranking.

        Empty when the mode is "doc" or the first stage has no search_chunks."""
        if self.passage_mode != "chunk" or not callable(getattr(self.first, "search_chunks", None)):
            return {}
        best: dict[str, str] = {}
        for chunk_id, _ in self.first.search_chunks(text, self.n_chunks):
            best.setdefault(chunk_id.rsplit("#", 1)[0], chunk_id)  # the first chunk met is the best
        return best

    def reorder(self, text: str, ids: list[str], passages: list[str]) -> list[str]:
        """The ids after one Claude call over the passages of the first len(passages) ids.

        `ids` is the whole first-stage list, best first; only the first len(passages) are reordered,
        the others follow in their first-stage order. A reply that is not a permutation of 1 to n
        (or no reply) leaves everything in the first-stage order."""
        n = len(passages)
        if n < 2:
            return list(ids)  # nothing to reorder, so no call
        numbered = "\n\n".join(f"[{i}] {p}" for i, p in enumerate(passages, 1))
        prompt = RERANK_PROMPT.format(n=n, query=text, passages=numbered)
        reply = claude.call(prompt, rerank_schema(n), model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg))
        order = reply.output.get("order") if reply is not None and reply.error is None and isinstance(reply.output, dict) else None
        if not valid_order(order, n):
            why = reply.error if reply is not None and reply.error else f"the reply was not each of 1 to {n} once: {order}"
            print(f"  warning: keeping the first-stage order ({why})", flush=True)
            return list(ids)
        return [ids[i - 1] for i in order] + list(ids[n:])

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        """The k best documents as (docid, score): the first stage's top candidates reordered by Claude."""
        ids = [d for d, _ in self.first.search(text, max(k, self.candidates))]
        top = ids[: self.candidates]
        best = self.best_chunks(text) if len(top) > 1 else {}
        passages = [self.passage(best[d]) if d in best else self.corpus.docs[d].text[: self.passage_chars] for d in top]
        return pairs(self.reorder(text, ids, passages)[:k])

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        """The k best chunks as (chunk id, score): the first stage's top candidate chunks reordered by Claude."""
        ids = [c for c, _ in self.first.search_chunks(text, max(k, self.candidates))]
        passages = [self.passage(c) for c in ids[: self.candidates]]
        return pairs(self.reorder(text, ids, passages)[:k])


def build(corpus, cfg):
    """The rerank system for a corpus and settings."""
    return Rerank(corpus, cfg)
