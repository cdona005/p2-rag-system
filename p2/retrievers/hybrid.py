"""Hybrid retriever: reciprocal rank fusion (RRF) of bm25 and dense.

It is the fusion of the 13 lab's pipeline.py (rrf, k = 60) over the two systems of this repo:
- the two systems come from p2.retrievers.build("bm25", ...) and build("dense", ...), so each
  index is built once per run, and the constant k is [hybrid] rrf_k of p2.toml (default 60);
- each system is asked for its FULL ranking (every document, or every chunk for search_chunks),
  never a top-10 list, because a document that is 11th in both lists can belong in the fused top 10;
- an item at rank r (counting from 1) in a ranking adds 1 / (k + r) to its fused score, and its
  score is the sum over the two rankings; the ranks come from a dict, not from list.index;
- the fused scores are ordered with p2.runfile.order, so equal scores fall in id order.

Zero-score padding: bm25 scores a document that shares no word with the query 0 and ranks those
documents in docid order, so their ranks are not real matches. This file keeps the lab's behavior
and fuses the rankings as they are, padding included. Padding sits below every real match, so it
matters only for a query with few matching documents; on the 20 shared practice queries that is
p01 (4 matching documents) and, barely, p04, p05 and p07 (18 each). Leaving the zero-score
documents out was tried on those queries only: recall@10 rose from 0.592 to 0.617 and nDCG@10
from 0.444 to 0.457 (identifier queries only), MRR@10 did not move. That is too small to call
harmful, so the lab's full rankings stay.
"""

from __future__ import annotations

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False

DEFAULT_RRF_K = 60  # the constant of the 13 lab; [hybrid] rrf_k in p2.toml overrides it


def rrf(rankings, k: int = DEFAULT_RRF_K) -> list[tuple[str, float]]:
    """Reciprocal rank fusion of rankings (each a list of ids, best first).

    An id at rank r (starting at 1) scores 1 / (k + r) in that ranking; its fused score is the
    sum over the rankings it appears in. Returns (id, score) pairs, best first, ties in id order.
    """
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, item in enumerate(ranking, 1):  # rank starts at 1
            scores[item] = scores.get(item, 0.0) + 1.0 / (k + rank)
    return order(scores.items())


class Hybrid:
    def __init__(self, corpus, cfg):
        """Get the two systems to fuse (built once per process) and read the RRF constant."""
        self.corpus = corpus
        self.cfg = cfg
        self.k = int(cfg.table("hybrid").get("rrf_k", DEFAULT_RRF_K))
        self.bm25 = retrievers.build("bm25", corpus, cfg)
        self.dense = retrievers.build("dense", corpus, cfg)
        self.n_chunks = len(corpus.chunks(cfg.chunk_words, cfg.chunk_overlap))

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        """The k best documents as (docid, fused score), fusing both systems' full document rankings."""
        n = len(self.corpus.docs)
        rankings = [[d for d, _ in system.search(text, n)] for system in (self.bm25, self.dense)]
        return rrf(rankings, self.k)[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        """The k best chunks as (chunk id, fused score), fusing both systems' full chunk rankings."""
        rankings = [[c for c, _ in system.search_chunks(text, self.n_chunks)] for system in (self.bm25, self.dense)]
        return rrf(rankings, self.k)[:k]


def build(corpus, cfg):
    """The hybrid system for a corpus and settings."""
    return Hybrid(corpus, cfg)
