"""
Visible tests for the claims-search practice exercise.

Run:
    python test_claim_search.py

These are a SUBSET of the tests the grader will run. Passing them is
necessary but not sufficient.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List

from claim_search import (
    DEFAULT_WEIGHTS,
    STATUS_PRIORITY,
    blend_scores,
    cosine_similarity,
    diversify_by_type,
    embed_text,
    keyword_overlap_score,
    normalize_scores,
    rank_claims,
    search_claims,
)
from sample_claims import SAMPLE_CLAIMS


# ---------------------------------------------------------------
# Section 1 — Python & Scoring Primitives
# ---------------------------------------------------------------

def test_embed_text_determinism_and_norm() -> None:
    v1 = embed_text("hello world")
    v2 = embed_text("hello world")
    assert v1 == v2, "embed_text must be deterministic"
    assert len(v1) == 32, "default dim should be 32"
    norm = math.sqrt(sum(x * x for x in v1))
    assert abs(norm - 1.0) < 1e-9, "embed_text must return a unit vector"


def test_embed_text_edge_cases() -> None:
    assert embed_text("") == [0.0] * 32, "empty input -> zero vector of length dim"
    assert embed_text("   ") == [0.0] * 32, "whitespace-only -> zero vector"
    assert embed_text("!!!") == [0.0] * 32, "punctuation-only -> zero vector"
    assert embed_text("Hello WORLD") == embed_text("hello world"), "must be case-insensitive"
    v_small = embed_text("hello world", dim=8)
    assert len(v_small) == 8, "dim parameter must be respected"


def test_cosine_similarity() -> None:
    assert cosine_similarity([1.0, 0.0], [1.0, 0.0]) == 1.0
    assert abs(cosine_similarity([1.0, 0.0], [0.0, 1.0])) < 1e-9
    assert cosine_similarity([], [1.0]) == 0.0
    assert cosine_similarity([1.0, 2.0], [1.0]) == 0.0, "mismatched lengths -> 0.0"
    assert cosine_similarity([0.0, 0.0], [1.0, 1.0]) == 0.0, "zero-norm -> 0.0"


def test_keyword_overlap_score() -> None:
    assert keyword_overlap_score("rear bumper", "rear bumper damaged") == 1.0
    assert keyword_overlap_score("rear bumper", "front bumper damaged") == 0.5
    assert keyword_overlap_score("rear bumper", "totally unrelated text") == 0.0
    assert keyword_overlap_score("", "anything") == 0.0
    assert keyword_overlap_score("anything", "") == 0.0
    # case-insensitive
    assert keyword_overlap_score("ROOF", "roof damage") == 1.0


def test_normalize_scores() -> None:
    assert normalize_scores([]) == []
    out = normalize_scores([1.0, 2.0, 3.0, 4.0, 5.0])
    assert out == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert normalize_scores([7.0, 7.0, 7.0]) == [0.0, 0.0, 0.0], \
        "all-equal -> all zeros (no divide-by-zero)"


def test_blend_scores() -> None:
    # straightforward weighted sum
    out = blend_scores(
        {"keyword": 1.0, "semantic": 0.5, "status": 0.0},
        {"keyword": 0.4, "semantic": 0.4, "status": 0.2},
    )
    assert abs(out - (0.4 * 1.0 + 0.4 * 0.5 + 0.2 * 0.0)) < 1e-9
    # missing component -> contributes 0
    out2 = blend_scores(
        {"keyword": 1.0},
        {"keyword": 0.5, "semantic": 0.5},
    )
    assert abs(out2 - 0.5) < 1e-9


# ---------------------------------------------------------------
# Section 2 — Ranking & Refinement
# ---------------------------------------------------------------

def test_rank_claims_shape_and_order() -> None:
    out = rank_claims(
        "rear bumper damaged",
        SAMPLE_CLAIMS,
        DEFAULT_WEIGHTS,
        top_k=5,
    )
    assert isinstance(out, list) and len(out) <= 5
    for r in out:
        assert {"claim_id", "claim_type", "status", "score", "signals"} <= set(r.keys())
        assert {"keyword", "semantic", "status"} <= set(r["signals"].keys())
        assert isinstance(r["score"], float)
    assert all(out[i]["score"] >= out[i + 1]["score"] for i in range(len(out) - 1)), \
        "results must be sorted by score descending"


def test_rank_claims_edge_cases() -> None:
    assert rank_claims("anything", [], DEFAULT_WEIGHTS, top_k=3) == []
    assert rank_claims("anything", SAMPLE_CLAIMS, DEFAULT_WEIGHTS, top_k=0) == []


def test_diversify_by_type() -> None:
    results = [
        {"claim_id": "A1", "claim_type": "auto", "score": 0.95},
        {"claim_id": "A2", "claim_type": "auto", "score": 0.90},
        {"claim_id": "A3", "claim_type": "auto", "score": 0.85},
        {"claim_id": "H1", "claim_type": "home", "score": 0.80},
        {"claim_id": "H2", "claim_type": "home", "score": 0.70},
    ]
    out = diversify_by_type(results, max_per_type=2)
    ids = [r["claim_id"] for r in out]
    assert ids == ["A1", "A2", "H1", "H2"]


def test_search_claims_end_to_end() -> None:
    out = search_claims(
        query="roof damage from storm",
        claims=SAMPLE_CLAIMS,
        weights=DEFAULT_WEIGHTS,
        top_k=3,
        max_per_type=2,
    )
    assert isinstance(out, list)
    assert len(out) <= 3
    # sorted by score descending
    assert all(out[i]["score"] >= out[i + 1]["score"] for i in range(len(out) - 1))
    # diversity cap honored
    counts: Dict[str, int] = {}
    for r in out:
        counts[r["claim_type"]] = counts.get(r["claim_type"], 0) + 1
    assert all(c <= 2 for c in counts.values())


# ---------------------------------------------------------------
# Section 3 — Written Answer
# ---------------------------------------------------------------

def test_written_answer_is_filled_in() -> None:
    import os
    import re as _re
    path = os.path.join(os.path.dirname(__file__), "WRITTEN_ANSWER.md")
    with open(path, "r", encoding="utf-8") as f:
        body = f.read()
    m = _re.search(r"<!-- BEGIN ANSWER -->(.*?)<!-- END ANSWER -->", body, _re.DOTALL)
    assert m is not None, "WRITTEN_ANSWER.md is missing the BEGIN/END ANSWER markers"
    answer = m.group(1)
    assert "TODO" not in answer, "replace the TODO placeholder with your actual answer"
    assert len(answer.split()) >= 40, \
        "answer should be at least ~4 sentences (>= 40 words) between the BEGIN/END markers"


# ---------------------------------------------------------------
# Runner
# ---------------------------------------------------------------

ALL_TESTS = [
    test_embed_text_determinism_and_norm,
    test_embed_text_edge_cases,
    test_cosine_similarity,
    test_keyword_overlap_score,
    test_normalize_scores,
    test_blend_scores,
    test_rank_claims_shape_and_order,
    test_rank_claims_edge_cases,
    test_diversify_by_type,
    test_search_claims_end_to_end,
    test_written_answer_is_filled_in,
]


def main() -> None:
    failures: List[str] = []
    for t in ALL_TESTS:
        try:
            t()
            print(f"  PASS  {t.__name__}")
        except NotImplementedError:
            print(f"  SKIP  {t.__name__}  (not implemented yet)")
        except AssertionError as e:
            failures.append(f"{t.__name__}: {e}")
            print(f"  FAIL  {t.__name__}  -> {e}")
        except Exception as e:
            failures.append(f"{t.__name__}: {type(e).__name__}: {e}")
            print(f"  ERROR {t.__name__}  -> {type(e).__name__}: {e}")
    print()
    if failures:
        print(f"{len(failures)} failing test(s).")
        raise SystemExit(1)
    print("All visible tests passed.")


if __name__ == "__main__":
    main()
