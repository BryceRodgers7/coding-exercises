"""
=================================================================
PRACTICE TEST — Mini RAG Pipeline
=================================================================

Format follows a GenAI engineering interview style with three scored sections:

  Section 1 — Python fundamentals (4 pts)   ~ 20 hidden tests
  Section 2 — RAG mechanics      (4 pts)   ~  8 hidden tests + 1 written
  Section 3 — Prompt engineering (4 pts)   ~  6 hidden tests

You may use ONLY the Python standard library (no numpy, no sklearn,
no external embedding libraries). Network access is disabled.

Suggested time: 60 minutes.

-----------------------------------------------------------------
SCENARIO
-----------------------------------------------------------------
You are building a minimal Retrieval-Augmented Generation (RAG)
prototype to answer questions over a small corpus of product
documentation. A real embedding model is not available, so you
will implement a DETERMINISTIC mock embedding scheme that behaves
just enough like a real one for the rest of the pipeline to work.

The pipeline:

    user question
        |
        v
    embed_text  ----> vector
        |
        v
    score_chunks ---> ranked chunks
        |
        v
    build_prompt ---> grounded prompt for an LLM


=================================================================
SECTION 1 — PYTHON FUNDAMENTALS  (4 points)
=================================================================

Implement THREE functions:

(1) tokenize(text: str) -> List[str]
    - Lowercase the text.
    - Return a list of alphanumeric tokens.
    - Empty / None-ish input -> return [].

(2) embed_text(text: str, dim: int = 32) -> List[float]
    - Deterministic mock embedding.
    - Same input MUST always produce the same vector.
    - Use a STABLE hash (hashlib.*) — NOT Python's built-in hash().
    - For each token, map it to one of `dim` buckets and give it
      a +1 or -1 contribution (your choice of how to derive both
      the index and the sign from the hash digest).
    - The final vector MUST be L2-normalized (unit length), unless
      it is the zero vector (empty input).
    - Default `dim` is 32 for this exercise (note: different from
      the warm-up — do NOT hardcode 16).

(3) cosine_similarity(a: List[float], b: List[float]) -> float
    - Standard cosine similarity.
    - Mismatched lengths or empty vectors -> return 0.0.
    - Zero-norm on either side -> return 0.0.


=================================================================
SECTION 2 — RAG MECHANICS  (4 points)
=================================================================

(4) retrieve(
        query: str,
        chunks: List[str],
        top_k: int = 3,
        min_score: float = 0.0,
    ) -> List[Dict[str, Any]]

    - Embed the query and every chunk using embed_text.
    - Score each chunk with cosine_similarity against the query.
    - Return up to `top_k` chunks, sorted by score DESCENDING.
    - FILTER OUT any chunk whose score is strictly less than
      `min_score` (this is the new twist vs. the warm-up — make
      sure your filter is applied BEFORE the top_k cut).
    - Each returned item must be a dict with the keys:
        {"index": int, "text": str, "score": float}
      where `index` is the chunk's original position in `chunks`.
    - Edge cases to handle: empty chunks, top_k <= 0, empty query.

WRITTEN QUESTION (worth ~0.5 of the section score):

    Suppose this prototype is moved into production and the corpus
    grows to ~10 million chunks, with thousands of queries per
    second. Identify TWO distinct bottlenecks the current
    `retrieve()` implementation will hit at that scale, and for
    EACH bottleneck propose a concrete mitigation (name specific
    techniques, data structures, or product categories — not just
    "make it faster"). Write your answer in the WRITTEN_ANSWER
    string below; aim for ~6-10 sentences total.

    Hint: strong answers cover at least TWO of:
      - embedding compute cost on the hot path
      - O(N) similarity scan vs. ANN indexing
      - in-memory footprint of N * dim floats
      - cache locality / query-side caching
      - re-ranking, hybrid search, freshness


=================================================================
SECTION 3 — PROMPT ENGINEERING  (4 points)
=================================================================

(5) build_prompt(
        question: str,
        retrieved: List[Dict[str, Any]],
    ) -> str

    Produce a single prompt string suitable for an instruction-
    tuned LLM. The grader checks for the presence of these
    elements (case-insensitive substring match on the returned
    string):

      a) A system-style instruction describing the assistant's
         role as a grounded question-answering assistant.
      b) An EXPLICIT instruction to use ONLY the provided context
         (no outside knowledge).
      c) An EXPLICIT fallback instruction for when the answer is
         not in the context (a clear "I don't know"-style phrase).
      d) An instruction to CITE the source chunk (by index or
         number) when using information from it.
      e) The user's question, wrapped in a clear delimiter
         (e.g. <QUESTION>...</QUESTION>).
      f) The retrieved context, wrapped in its own clear
         delimiter (e.g. <CONTEXT>...</CONTEXT>), with each
         chunk individually labelled with its index AND score.

    If `retrieved` is empty, the context section must still be
    present and must contain a clear "no context" marker — the
    grounding + fallback rules must still hold.


=================================================================
END OF SPEC — write your implementations below.
=================================================================
"""

from __future__ import annotations

import hashlib
import math
import re
from typing import Any, Dict, List


# ---------------------------------------------------------------
# Section 1
# ---------------------------------------------------------------

def tokenize(text: str) -> List[str]:
    if not text:
        return []

    return re.findall(r"[a-z0-9]+", text.lower())


def embed_text(text: str, dim: int = 32) -> List[float]:

    # tokenize the text
    # for each token, calculate hash, index, sign, and update vector
    # normalize vector & return it

    vector = [0.0] * dim
    tokens = tokenize(text)

    if not tokens:
        return vector

    for token in tokens:
        digest = hashlib.md5(token.encode("utf-8")).hexdigest()
        index = int(digest[:8], 16) % dim
        sign = 1.0 if int(digest[8:16], 16) % 2 == 0 else -1.0
        vector[index] += sign

    norm = math.sqrt(sum(x * x for x in vector))

    if norm == 0:
        return vector

    return [x / norm for x in vector]


def cosine_similarity(a: List[float], b: List[float]) -> float:

    # calculate dot product
    # calculate norm for both input vectors
    # normalize dot product and return it

    if not a or not b or len(a) != len(b):
        return 0.0

    dot = sum(x * y for x, y in zip(a,b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)


# ---------------------------------------------------------------
# Section 2
# ---------------------------------------------------------------

def retrieve(
    query: str,
    chunks: List[str],
    top_k: int = 3,
    min_score: float = 0.0,
) -> List[Dict[str, Any]]:
    
    # embed query
    # for each chunk, embed, calculate cosine similarity w/ query, store in list
    # sort list & return top results with score > min_score

    if not chunks or not query or top_k <= 0:
        return []

    query_embedding = embed_text(query)
    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_text(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)
        scored_chunks.append({
            "index" : i,
            "text" : chunk,
            "score" : similarity
        })

    filtered_chunks = [c for c in scored_chunks if c.get("score") >= min_score]

    filtered_chunks.sort(key=lambda item: item['score'], reverse=True)

    return filtered_chunks[:top_k]



WRITTEN_ANSWER = """
If this were a real production system, we would want to use a better embedding scheme than md5, preferrably a neural network with more dimensions than 32 to better capture semantic meaning.
If this were a scaled up system, we would NOT want to calculate embeddings for every chunk on every request. That is too much (unnecessary) computation.
Instead we would want to pre-compute the embeddings and persist them (they do not change). Keeping millions of embeddings each made up of 100s of floats (or more) takes too much memory.
We also would NOT want to calculate cosine similarity against every chunk for every request, that is too much (unnecessary) computation.
Instead we would want to use a vector-indexing scheme such as Approximate Nearest Neighbor (there are others). 
There are inexpensive commerical vector database platforms (such as Qdrant) which will do all of this for you: store chunks, store embeddings, maintain a vector-index & perform efficient vector-searches.
Also, if the queries are repeated often enough then we might want to cache those embeddings.
""".strip()


# ---------------------------------------------------------------
# Section 3
# ---------------------------------------------------------------

def build_prompt(question: str, retrieved: List[Dict[str, Any]]) -> str:

    # construct context
    # construct structured prompt + insert context & question
    # return prompt

    context_blocks = []

    for doc in retrieved:
        context_blocks.append(f"Chunk={doc['index']} | Score={doc['score']}\n"
                              f"{doc['text']}")

    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    prompt = f"""

You are a grounded question-answering assistant. 

Instructions:
- Answer the question using only information within <CONTEXT>.
- Do not use any outside knowledge.
- Do not make up any information.
- Cite the chunk number when using information from the context.
- If the answer is not found within the context, say "I don't know, from the context provided."
- Keep answers concise.

<CONTEXT>
{context}
</CONTEXT>

<QUESTION>
{question}
</QUESTION>

ANSWER:
""".strip()

    return prompt



# ---------------------------------------------------------------
# Local sanity tests (NOT the grader — just to help you iterate).
# Run:   python practice_test.py
# ---------------------------------------------------------------

def _self_check() -> None:
    # Section 1
    assert tokenize("") == []
    assert tokenize("Hello, WORLD! 123") == ["hello", "world", "123"]

    v1 = embed_text("hello world")
    v2 = embed_text("hello world")
    assert v1 == v2, "embed_text must be deterministic"
    assert len(v1) == 32, "default dim should be 32"
    norm = math.sqrt(sum(x * x for x in v1))
    assert abs(norm - 1.0) < 1e-9, "embed_text must be unit-normalized"
    assert embed_text("") == [0.0] * 32

    assert cosine_similarity([], [1.0]) == 0.0
    assert cosine_similarity([1.0, 0.0], [1.0, 0.0]) == 1.0
    assert abs(cosine_similarity([1.0, 0.0], [0.0, 1.0])) < 1e-9

    # Section 2
    chunks = [
        "Python is great for backend services and data pipelines.",
        "Cosine similarity measures the angle between two vectors.",
        "Vector databases use ANN indexes to scale similarity search.",
        "Bananas are yellow and grow in tropical climates.",
    ]
    out = retrieve("How does vector search scale?", chunks, top_k=2)
    assert isinstance(out, list) and len(out) <= 2
    assert all({"index", "text", "score"} <= set(d.keys()) for d in out)
    assert all(
        out[i]["score"] >= out[i + 1]["score"]
        for i in range(len(out) - 1)
    ), "results must be sorted descending"
    assert retrieve("anything", [], top_k=3) == []
    assert retrieve("anything", chunks, top_k=0) == []
    high = retrieve("vector", chunks, top_k=4, min_score=0.99)
    assert all(d["score"] >= 0.99 for d in high)

    # Section 3
    prompt = build_prompt(
        "What is cosine similarity?",
        retrieve("What is cosine similarity?", chunks, top_k=2),
    )
    low = prompt.lower()
    for needle in ("context", "question", "cite", "don't know"):
        assert needle in low, f"prompt missing required element: {needle}"
    assert "<context>" in low and "</context>" in low
    assert "<question>" in low and "</question>" in low

    empty_prompt = build_prompt("anything", []).lower()
    assert "context" in empty_prompt and "don't know" in empty_prompt

    print("All local sanity checks passed.")


if __name__ == "__main__":
    _self_check()