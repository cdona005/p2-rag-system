"""Ablation: bm25 with the 12 lab's plain tokenizer instead of the "codes" tokenizer.

It is bm25 and nothing else changes: the same k1, b, chunking and scoring. The only difference is
that words are cut into [a-z0-9]+ runs, so a code such as pno-ii-10-002 becomes the separate words
pno, ii, 10 and 002 instead of staying whole and also being indexed in parts.
"""

from __future__ import annotations

from p2.retrievers.bm25 import BM25

NEEDS_CLAUDE = False

BASE = "bm25"  # the system this variant is compared with in the own-ablation-queries table


def build(corpus, cfg):
    """A BM25 over the same settings as p2.toml, with the tokenizer set to "lab"."""
    return BM25(corpus, cfg.replace(tokenizer="lab"))
