"""
Claims Search — implementation file.

The detailed spec for EACH function is in its docstring below. The
README only covers the overall framing, data shapes, and the Section 3
written question — function-by-function rules live HERE.

Run:
    python test_claim_search.py
"""

from __future__ import annotations

import math
import re
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

# NOTE: `hashlib` is NOT available in this exam environment.
# Roll your own deterministic hash for embed_text. A polynomial
# rolling hash is simple and memorable:
#     h = 0
#     for c in token:
#         h = h * 31 + ord(c)


# ---------------------------------------------------------------
# Constants — used by Section 2 (rank_claims).
# ---------------------------------------------------------------

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


# ---------------------------------------------------------------
# Section 1 — Python & Scoring Primitives
# ---------------------------------------------------------------

def tokenize(text: str) -> List[str]:
    if not text:
        return []
    
    return re.findall(r"[a-z0-9]+", text.lower())


# hash function

# def simple_hash(text: str) -> int:














































def simple_hash(text: str) -> int:
    # build hash from each char in text

    h = 0
    
    for c in text:
        h = (h * 31 + ord(c)) % 1000003

    return h


def manual_hash(text: str) -> int:
    if not text:
        return 0
    h = 0
    for c in text:
        h = (h * 31 + ord(c)) % 1000003

    return h


def embed_text(text: str, dim: int = 32) -> List[float]:
    """
    Deterministic mock embedding.

    - Tokenize `text` into lowercase alphanumeric tokens.
    - For each token, derive an index in [0, dim) AND a sign (+1 or -1)
      from a STABLE, process-independent hash, then accumulate into the
      vector at that index.
    - Do NOT use Python's built-in hash() (it is randomized per process),
      and hashlib is NOT available. A polynomial rolling hash works fine:
          h = 0
          for c in token:
              h = h * 31 + ord(c)
    - Return an L2-normalized vector, UNLESS the input produced no
      tokens — then return the all-zero vector of length `dim`.
    - Default `dim` is 32. Do not hardcode it.
    """

    # write hashing function then for each token calculat hash, index, sign, and update vector
    # normalize & return vector

    vector = [0.0] * dim

    tokens = tokenize(text)

    if not tokens:
        return vector
    
    for token in tokens:
        index = manual_hash(token) % dim

        sign = 1.0 if manual_hash(token + "_sign") % 2 == 0 else -1.0

        vector[index] += sign

    norm = math.sqrt(sum(x * x for x in vector))

    if norm == 0:
        return vector
    
    return [x / norm for x in vector]


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """
    Standard cosine similarity between two equal-length vectors.

    - Return dot(a, b) / (||a|| * ||b||).
    - Mismatched lengths, empty input on either side, or zero-norm on
      either side -> return 0.0.
    """

    # calculate dot
    # calculate norma & normb then normalize & return result

    if not a or not b or len(a) != len(b):
        return 0.0
    
    dot = sum(x * y for x, y in zip(a,b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)


# keyword_overlap_score

# def keyword_overlap_score(query: str, text: str) -> float:



















































def keyword_overlap_score(query: str, text: str) -> float:

    # use sets to union tokens from both strings
    # return fraction of union over query

    query_t = tokenize(query)
    text_t = tokenize(text)

    query_s = set(query_t)
    text_s = set(text_t)

    if len(query_s) == 0:
        return 0.0
    
    return (len(query_s & text_s) / len(query_s))

def keyword_overlap_score(query: str, text: str) -> float:
    """
    Simple lexical-coverage score in [0.0, 1.0].

    - Tokenize both inputs to lowercase alphanumeric tokens.
    - Return |unique_query_tokens ∩ unique_text_tokens| / |unique_query_tokens|.
    - Empty query OR empty text -> 0.0.
    """
    # tokenie & convert both inputs to a set
    # set-and to calculate fraction and return the result

    query_tokens = tokenize(query)
    text_tokens = tokenize(text)

    if not query_tokens or not text_tokens:
        return 0.0

    query_set = set(query_tokens)
    text_set = set(text_tokens)

    return (len(query_set & text_set) / len(query_set))


# normalize scores

# def normalize_scores(scores: List[float]) -> List[float]:
























































def normalize_scores(scores: List[float]) -> List[float]:

    # find span of scores
    # normalize each score
    # return normalized scores

    if not scores:
        return []

    hi = max(scores)
    lo = min(scores)

    span = hi - lo

    if span == 0:
        return [0.0] * len(scores)
    
    return [(s - lo) / span for s in scores]


def normalize_scores(scores: List[float]) -> List[float]:
    """
    Min-max normalize the list into [0.0, 1.0].

    - normalized[i] = (scores[i] - min) / (max - min)
    - Empty input -> [].
    - If max == min (all values tied), return a list of 0.0s with the
      SAME LENGTH as `scores` (avoid divide-by-zero).
    """
    if not scores:
        return []
    hi = max(scores)
    lo = min(scores)
    span = hi - lo
    if span == 0:
        return [0.0] * len(scores)
    norms = [(score - lo) / span for score in scores]
    return norms

# blend scores

# def blend_scores(components: Dict[str, float], weights: Dict[str, float]) -> float:
    """
    Weighted sum across the keys in `weights`:
        sum(components.get(k, 0.0) * weights[k] for k in weights)

    - Weights are used AS-IS — the caller is responsible for any
      normalization.
    - A key present in `weights` but MISSING from `components`
      contributes 0.0.
    """














































def blend_scores(components: Dict[str, float], weights: Dict[str, float]) -> float:

    # weight each component score by the appropriate weight

    total = 0.0

    for key in weights:
        raw = components.get(key, 0.0)
        weighted_score = raw * weights[key]
        total += weighted_score

    return total

def blend_scores(
    components: Dict[str, float],
    weights: Dict[str, float],
) -> float:
    # calculate weighted scores from weights + components and sum
    total = 0.0
    for key in weights:
        score = components.get(key, 0.0) * weights[key]
        total += score

    return total


# ---------------------------------------------------------------
# Section 2 — Ranking Workflow & Refinement
# ---------------------------------------------------------------


# rank claims

# def rank_claims(query: str, claims: List[Dist[str, any]], weights: Dict[str, float], top_k: int = 5) -> List[Dict[str, any]]:

"""
    Score each claim with three signals, blend, sort, return top_k.

    For each claim, compute three signal scores:
        "keyword"  = keyword_overlap_score(query, claim["description"])
        "semantic" = cosine_similarity(embed_text(query),
                                       embed_text(claim["description"]))
        "status"   = STATUS_PRIORITY.get(claim["status"], 0.0)

    Then blend with `blend_scores(signals, weights)` to get the final
    score.

    Each returned dict is the original claim AUGMENTED with:
        "score":   float                # the blended score
        "signals": Dict[str, float]     # the three component scores

    - Sort descending by score and return up to `top_k` items.
    - Empty `claims`   -> [].
    - top_k <= 0       -> [].
    """










































def rank_claims(query: str, claims: List[Dict[str, any]], weights: Dict[str, float], top_k: int = 5) -> List[Dict[str, any]]:

    # calculate signals, then blend to get score
    # shallow copy and add 'signals' and 'score'

    result = []

    if not claims or top_k <= 0:
        return result

    query_embedding = embed_text(query)
    
    for claim in claims:

        out = dict(claim)
        claim_embedding = embed_text(claim["description"])
        signals = {}
        signals["keyword"] = keyword_overlap_score(query, claim["description"])
        signals["semantic"] = cosine_similarity(query_embedding, claim_embedding)
        signals["status"] = STATUS_PRIORITY.get(claim["status"], 0.0)
        score = blend_scores(signals, weights)

        out["signals"] = signals
        out["score"] = score

        result.append(out)

    result.sort(key=lambda item: item["score"], reverse=True)

    return result[:top_k]


def rank_claims(
    query: str,
    claims: List[Dict[str, Any]],
    weights: Dict[str, float],
    top_k: int = 5,
) -> List[Dict[str, Any]]:

    # for each claim, calculate and store keyword, semantic, and status scores
    # blend all 3 into a single 'score'
    # output should match input + 'score' and 'signals'

    if not claims or top_k <= 0:
        return []

    query_embedding = embed_text(query)

    scored_claims = []

    for claim in claims:
        claim_copy = dict(claim)
        signals = {}
        signals["keyword"] = keyword_overlap_score(query, claim["description"])
        signals["semantic"] = cosine_similarity(query_embedding, embed_text(claim["description"]))
        signals["status"] = STATUS_PRIORITY.get(claim["status"], 0.0)
        claim_copy["signals"] = signals
        claim_copy["score"] = blend_scores(signals, weights)  #default weights??
        scored_claims.append(claim_copy)

    scored_claims.sort(key=lambda item: item["score"], reverse=True)

    return scored_claims[:top_k]



# diversify_by_type

# def diversify_by_type(results: List[Dict[str, any]], max_per_type: int = 2) -> List[Dict[str, any]]:

"""
    Cap the number of results from any single claim_type.

    - Walk `results` in order (assume input is already sorted by score
      descending — DO NOT re-sort).
    - Skip any entry whose `claim_type` has already reached
      `max_per_type`.
    - Preserve the relative order of the items you keep.
    """













































def diversify_by_type(results: List[Dict[str, Any]], max_per_type: int = 2) -> List[Dict[str, Any]]:

    # scan thru results and count members of each claim type
    # add claims to the output until a type is full and return

    out = []
    counts = {}

    for r in results:
        t = r.get("claim_type")
        if counts.get(t, 0) >= max_per_type:
            continue
        counts[t] = counts.get(t, 0) + 1
        out.append(r)

    return out

def diversify_by_type(
    results: List[Dict[str, Any]],
    max_per_type: int = 2,
) -> List[Dict[str, Any]]:
    
    # scan thru list, counting number of claims of each type & adding to output if not beyond threshhold

    counts = {}
    out = []
    for r in results:
        t = r.get("claim_type")
        if counts.get(t, 0) >= max_per_type:
            continue
        counts[t] = counts.get(t, 0) + 1
        out.append(r)

    return out

# search_claims

# def search_claims(query: str, claims: List[dict[str, any]], weights: Dict[str, float], top_k: int = 5, max_per_type: int = 2):

def search_claims(
    query: str,
    claims: List[Dict[str, Any]],
    weights: Optional[Dict[str, float]] = None,
    top_k: int = 5,
    max_per_type: int = 2,
) -> List[Dict[str, Any]]:
    """
    End-to-end pipeline:

        1. rank_claims(query, claims, weights, top_k=len(claims))
        2. diversify_by_type(..., max_per_type)
        3. Cut to top_k

    - If `weights` is None, use DEFAULT_WEIGHTS.
    - Empty `claims` -> [].
    - top_k <= 0     -> [].
    """


    # rank claims
    # diversify result of ranking claims
    # return top 5 (should already be sorted)

    if not query or not claims:
        return []
    
    if not weights:
        weights = DEFAULT_WEIGHTS
    
    ranked_claims = rank_claims(query, claims, weights, len(claims))

    diversified_ranked_claims = diversify_by_type(ranked_claims, max_per_type)

    return diversified_ranked_claims[:top_k]


# ---------------------------------------------------------------
# Section 3 — Diagnosing Unsupported Answers
# ---------------------------------------------------------------
# No implementation in this section — Section 3 is the written
# reasoning question. See WRITTEN_ANSWER.md.
