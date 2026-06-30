# Claims Search — Ranking & Refinement Practice Exercise

## Overview

You are building a document-ranking workflow for an insurance **claims search** experience. Given a natural-language query, your code must:

1. Blend several **relevance signals** (lexical, semantic, business-priority) into a single score per claim.
2. **Refine** the ranked list — enforce diversity across categories — before returning it.
3. Answer a **written reasoning question** about diagnosing and preventing unsupported answers in an AI-powered retrieval system.

The detailed spec for each function lives in **its docstring inside `claim_search.py`** — open that file as you work. This README only covers the framing, the data shapes, and the written question.

## Project Layout

```
.
├── README.md              ← this file (framing only)
├── claim_search.py        ← implement here — each function's spec is in its docstring
├── test_claim_search.py   ← visible tests; run: python test_claim_search.py
├── sample_claims.py       ← in-memory claims corpus used by the tests
└── WRITTEN_ANSWER.md      ← write your answer to the reasoning question here
```

## Constraints

- Python **standard library only**. No numpy, scikit-learn, external embedding APIs, or `hashlib`.
- Network access is disabled.
- Suggested time: **60 minutes**.
- The visible tests in `test_claim_search.py` are a **subset** of the hidden tests the grader will run.

## Scoring

Three sections, 4 points each (12 total).

| # | Section                                | Tests                              |
|---|----------------------------------------|------------------------------------|
| 1 | Python & Scoring Primitives            | ~10 hidden tests                   |
| 2 | Ranking Workflow & Refinement          | ~8 hidden tests                    |
| 3 | Diagnosing Unsupported Answers         | 1 written answer                   |

---

## Data shapes (used by Section 2)

A "claim" is a dict with at least these fields:

```python
{
    "claim_id":    str,    # e.g. "CL-001"
    "claim_type":  str,    # "auto" | "home" | "health" | "life"
    "status":      str,    # "open" | "pending" | "closed" | "denied"
    "filed_date":  str,    # "YYYY-MM-DD"
    "description": str,
    "amount":      float,
}
```

A **result** is a dict that contains all the original claim fields **plus**:

```python
{
    "score":   float,                # blended final score
    "signals": Dict[str, float],     # {"keyword": ..., "semantic": ..., "status": ...}
}
```

### Constants you must use

Already defined for you at the top of `claim_search.py`:

```python
STATUS_PRIORITY = {
    "open":    1.0,
    "pending": 0.7,
    "closed":  0.3,
    "denied":  0.1,
}

DEFAULT_WEIGHTS = {
    "keyword":  0.4,
    "semantic": 0.4,
    "status":   0.2,
}
```

Any unknown status → `0.0`.

---

## Section 3 — Written Question

Section 3 is a single open-ended reasoning question — no code. Answer it in `WRITTEN_ANSWER.md`, **between the `<!-- BEGIN ANSWER -->` and `<!-- END ANSWER -->` markers**. Aim for ~4-8 sentences — name concrete techniques rather than padding.

> Your team has shipped a RAG-style claims assistant that answers natural-language questions over the retrieved claim records. Adjusters have started reporting **unsupported answers** — confident-sounding responses that cite real claims but make assertions that the cited claim does not actually contain.
>
> 1. Describe **how you would diagnose** the prevalence and patterns of these unsupported answers in production. Be specific about telemetry, evaluation methods, and labeling strategy.
> 2. Describe **how you would reduce** their frequency. Cover BOTH retrieval-side mitigations (what the system feeds the model) AND generation-side mitigations (how the model is prompted and constrained), and name specific techniques or product categories where applicable.

A strong answer touches both parts and names concrete techniques (e.g. faithfulness evaluators, citation-required prompting, abstention thresholds, reranking, hybrid search).

---

## Running the visible tests

From this directory:

```
python test_claim_search.py
```

You should see `All visible tests passed.` when every function is implemented to spec.
