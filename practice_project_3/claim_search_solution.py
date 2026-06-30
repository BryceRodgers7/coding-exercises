"""
==================================================================
REFERENCE SOLUTION — claim_search_solution.py
==================================================================
This is the reference implementation of every function in the
spec. The stub file you should fill in is `claim_search.py`.

To verify this solution against the visible test suite, run:

    python verify_solution.py

(That script swaps this module in as `claim_search` at import time
so the existing tests run against the reference code without
touching your practice file.)
==================================================================
"""

from __future__ import annotations

import math
import re
from typing import Any, Dict, Iterable, List, Optional, Union

# `hashlib` is NOT available in the exam environment, so we roll our
# own deterministic hash below (polynomial rolling hash, Java-style)
# and use it everywhere we would otherwise have called hashlib.md5.


STATUS_PRIORITY: Dict[str, float] = {
    "open":    1.0,
    "pending": 0.7,
    "closed":  0.3,
    "denied":  0.1,
}

DEFAULT_WEIGHTS: Dict[str, float] = {
    "keyword":  0.4,
    "semantic": 0.4,
    "status":   0.2,
}


_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokenize(text: str) -> List[str]:
    if not text:
        return []
    return _TOKEN_RE.findall(text.lower())


# --- stable hash (replacement for hashlib.md5) ---------------------
# Polynomial rolling hash, prime 31 (same idea as Java's String.hashCode).
# Deterministic across processes (unlike Python's built-in hash()),
# and small enough to reproduce from memory in an exam.

def _stable_hash(token: str) -> int:
    h = 0
    for c in token:
        h = h * 31 + ord(c)
    return h


# ------------------------------------------------------------------
# Section 1 — Python & Scoring Primitives
# ------------------------------------------------------------------

def embed_text(text: str, dim: int = 32) -> List[float]:
    vector = [0.0] * dim
    tokens = _tokenize(text)
    if not tokens:
        return vector

    for token in tokens:
        h = _stable_hash(token)
        # Use the low bits for the bucket index, and a HIGHER part of
        # the hash for the sign so the sign isn't trivially correlated
        # with `h % dim` (especially when dim is a power of two).
        index = h % dim
        sign = 1.0 if (h // dim) % 2 == 0 else -1.0
        vector[index] += sign

    norm = math.sqrt(sum(x * x for x in vector))
    if norm == 0:
        return vector
    return [x / norm for x in vector]


def cosine_similarity(a: List[float], b: List[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0

    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def keyword_overlap_score(query: str, text: str) -> float:
    q_tokens = set(_tokenize(query))
    t_tokens = set(_tokenize(text))
    if not q_tokens or not t_tokens:
        return 0.0
    return len(q_tokens & t_tokens) / len(q_tokens)


def normalize_scores(scores: List[float]) -> List[float]:
    if not scores:
        return []
    lo = min(scores)
    hi = max(scores)
    if hi == lo:
        return [0.0] * len(scores)
    span = hi - lo
    return [(s - lo) / span for s in scores]


def blend_scores(
    components: Dict[str, float],
    weights: Dict[str, float],
) -> float:
    total = 0.0
    for key, weight in weights.items():
        raw_score = components.get(key, 0.0)
        total += raw_score * weight
    return total


# ------------------------------------------------------------------
# Section 2 — Ranking Workflow & Refinement
# ------------------------------------------------------------------

def rank_claims(
    query: str,
    claims: List[Dict[str, Any]],
    weights: Dict[str, float],
    top_k: int = 5,
) -> List[Dict[str, Any]]:
    if not claims or top_k <= 0:
        return []

    query_embedding = embed_text(query)
    scored: List[Dict[str, Any]] = []

    for claim in claims:
        description = claim.get("description", "")
        signals = {
            "keyword":  keyword_overlap_score(query, description),
            "semantic": cosine_similarity(query_embedding, embed_text(description)),
            "status":   STATUS_PRIORITY.get(claim.get("status"), 0.0),
        }
        score = blend_scores(signals, weights)

        result = dict(claim)
        result["score"] = float(score)
        result["signals"] = signals
        scored.append(result)

    scored.sort(key=lambda r: r["score"], reverse=True)
    return scored[:top_k]


def diversify_by_type(
    results: List[Dict[str, Any]],
    max_per_type: int = 2,
) -> List[Dict[str, Any]]:
    counts: Dict[Any, int] = {}
    out: List[Dict[str, Any]] = []
    for r in results:
        t = r.get("claim_type")
        if counts.get(t, 0) >= max_per_type:
            continue
        counts[t] = counts.get(t, 0) + 1
        out.append(r)
    return out


def search_claims(
    query: str,
    claims: List[Dict[str, Any]],
    weights: Optional[Dict[str, float]] = None,
    top_k: int = 5,
    max_per_type: int = 2,
) -> List[Dict[str, Any]]:
    if weights is None:
        weights = DEFAULT_WEIGHTS
    if not claims or top_k <= 0:
        return []

    ranked = rank_claims(query, claims, weights, top_k=len(claims))
    diversified = diversify_by_type(ranked, max_per_type)
    return diversified[:top_k]


# ------------------------------------------------------------------
# Section 3 — Diagnosing Unsupported Answers
# ------------------------------------------------------------------
# No implementation in this section — Section 3 is the written
# reasoning question. See WRITTEN_ANSWER_solution.md.
