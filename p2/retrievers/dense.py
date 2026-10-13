"""Dense retriever: embed every chunk once, embed the query, and rank chunks by cosine similarity.

It is the 12 lab's dense_rankings over chunks instead of whole articles:
- the embedder comes from [dense] model of p2.toml (default embed.BGE, bge-small-en-v1.5), loaded
  with embed.load;
- every chunk is encoded once with embed.doc_vectors, which keeps the vectors in .cache/vectors/
  keyed by each text's hash, so only new or changed chunks are encoded on a later run;
- the query is encoded the same way, with [dense] query_prefix of p2.toml put in front of it
  (empty by default; some embedders are trained with an instruction before the query);
- vectors have length 1, so one matrix product of the query vector with the chunk vectors gives
  the cosine similarity of the query with every chunk.

ChunkScorer then ranks the chunks for search_chunks and lifts them to documents for search (a
document scores its best chunk). Equal scores fall in id order, as for every system.
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        """Load the embedder named in [dense] and encode (or fetch from the cache) every chunk."""
        super().__init__(corpus, cfg)
        table = cfg.table("dense")
        self.model = str(table.get("model", embed.BGE))  # recorded in traces
        self.query_prefix = str(table.get("query_prefix", ""))
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> list[float]:
        """The cosine similarity of the query with every chunk, in the order of self.chunks."""
        if not len(self.chunks):
            return []
        query = self.embedder.encode([self.query_prefix + text])  # shape (1, dim), length 1
        return (query @ self.vectors.T).ravel().tolist()


def build(corpus, cfg):
    """The dense system for a corpus and settings."""
    return Dense(corpus, cfg)
