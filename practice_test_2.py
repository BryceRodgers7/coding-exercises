"""
=================================================================
PRACTICE TEST — Mini RAG Pipeline (v2)
=================================================================

Format follows a GenAI engineering interview style with three scored
sections, mirroring an example score report:

  Section 1 — Python              (4 pts)   ~ 20 hidden tests
  Section 2 — RAG                 (4 pts)   ~  8 hidden tests + 1 written
  Section 3 — LLM / GenAI Systems
             in Production        (4 pts)   ~  6 hidden tests

You may use ONLY the Python standard library (no numpy, no sklearn,
no external embedding libraries). Network access is disabled.

Suggested time: 60 minutes.

-----------------------------------------------------------------
SCENARIO
-----------------------------------------------------------------
You are prototyping a Retrieval-Augmented Generation (RAG) pipeline
over a small text corpus. No real embedding model is available, so
you will implement a DETERMINISTIC mock embedding function that
behaves enough like a real one for the rest of the pipeline to work.

The pipeline:

    user query
        |
        v
    embed_query  --------> query vector
        |
        v
    retrieve     --------> top_k ranked chunks (cosine similarity)
        |
        v
    assemble_prompt -----> grounded prompt for an LLM


=================================================================
SECTION 1 — PYTHON  (4 points)
=================================================================

Implement TWO functions. The grader runs ~20 hidden test cases
that exercise correctness AND edge cases for both.

(1) embed_query(query: str, dim: int = 24) -> List[float]
    - DETERMINISTIC mock embedding.
    - Same input MUST always produce the exact same vector.
    - Must use a STABLE hash (hashlib.*) — NOT Python's built-in
      hash() (which is randomized per process).
    - Tokenize the query into lowercase alphanumeric tokens.
    - For each token, derive an index in [0, dim) AND a sign
      (+1 or -1) from the hash digest, and accumulate into the
      vector at that index.
    - The returned vector MUST be L2-normalized to unit length,
      UNLESS the input produced no tokens (then return the
      all-zero vector of length `dim`).
    - Default `dim` is 24 — do NOT hardcode 16 or 32.
    - Edge cases the grader will check:
        * empty string
        * whitespace-only string
        * punctuation-only string
        * mixed-case input ("Hello WORLD" == "hello world")
        * very long input (hundreds of tokens)
        * `dim` values other than the default

(2) retrieve(
        query: str,
        chunks: List[str],
        top_k: int = 3,
    ) -> List[Dict[str, Any]]
    - Embed the query and EACH chunk using embed_query.
    - Score each chunk with cosine similarity against the query.
    - Return up to `top_k` chunks, sorted by score DESCENDING.
    - Each returned item must be a dict containing exactly these
      keys:
        {"index": int, "text": str, "score": float}
      where `index` is the chunk's original position in `chunks`
      (0-based) and `score` is the cosine similarity (a float).
    - Edge cases the grader will check:
        * empty `chunks` list   -> []
        * `top_k <= 0`          -> []
        * `top_k` larger than `len(chunks)` -> return all chunks,
          still sorted by score descending
        * ties in score (stable behavior is fine — grader will not
          break ties beyond "score must be non-increasing")


=================================================================
SECTION 2 — RAG  (4 points)
=================================================================

The grader runs ~8 retrieval tests against your `retrieve()` from
Section 1, plus one written question worth ~0.5 of the section
score.

The retrieval tests verify cosine-similarity-based semantic ranking:
queries that share tokens with a chunk should rank that chunk
higher than an unrelated chunk; the top-1 result for a query that
is identical to a chunk should be that chunk; etc.

WRITTEN QUESTION (worth ~0.5 of the section score):

    Suppose this prototype is moved into production and the corpus
    grows to ~10 MILLION chunks, with thousands of queries per
    second. The current `retrieve()` implementation will hit
    multiple bottlenecks at that scale.

    In the WRITTEN_ANSWER string below, identify the bottlenecks
    you consider most important and propose CONCRETE mitigations
    for each. Name specific techniques, data structures, or product
    categories — not just "make it faster".

    A strong answer covers ALL THREE of:
      1. Embedding compute on the hot path (and how to avoid it).
      2. Vector-database indexing — i.e. the O(N) full-corpus
         similarity scan vs. an approximate-nearest-neighbor
         (ANN) index. Name at least one ANN family or product.
      3. Memory / storage scaling — N * dim floats for 10M chunks
         does not fit comfortably in RAM. Discuss where the
         vectors live and how they are served.

    A weaker answer that only discusses caching (and skips ANN
    indexing or memory scaling) will lose partial credit, as noted
    in the example score report.

    Aim for ~8-12 sentences.


=================================================================
SECTION 3 — LLM / GENAI SYSTEMS IN PRODUCTION  (4 points)
=================================================================

(3) assemble_prompt(
        question: str,
        retrieved: List[Dict[str, Any]],
    ) -> str

    Produce a single prompt string suitable for an instruction-
    tuned LLM. The grader runs ~6 hidden tests that check, via
    case-insensitive substring matching on the returned string,
    that ALL of the following are present:

      a) A system-style instruction establishing the model's role
         as a GROUNDED question-answering assistant.
      b) An EXPLICIT instruction to use ONLY the provided context
         (no outside knowledge / no fabrication).
      c) An EXPLICIT fallback instruction for when the answer is
         NOT in the context (a clear "I don't know"-style phrase).
      d) An instruction to CITE the source chunk (by its index or
         number) whenever information from the context is used.
      e) The user's QUESTION, wrapped in an explicit delimiter
         such as <QUESTION>...</QUESTION>.
      f) The retrieved CONTEXT, wrapped in its own explicit
         delimiter such as <CONTEXT>...</CONTEXT>, with each
         chunk individually labelled with BOTH its index AND its
         score so the model can cite it precisely.

    If `retrieved` is empty, the context section must still be
    present and must contain a clear "no context retrieved" marker
    — the grounding rule and the fallback rule must still hold.


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
# Section 1 — Python
# ---------------------------------------------------------------


def simple_hash(text: str) -> int:

    # build hash from each char
    h = 0

    for c in text:
        
        h = (h * 31 + ord(c)) % 1000003

    return h


def simple_hash(text: str) -> int:
    # build hash from each char

    h = 0

    for c in text:
        h = (h * 31 + ord(c)) % 1000003

    return h

def simple_hash(text: str) -> int:
    # build hash from each char

    h = 0

    for c in text:
        h = (h * 31 + ord(c)) % 1000003

    return h



def embed_query(query: str, dim: int = 24) -> List[float]:
    # use hashlib.md5 or simple_hash to has each token
    # from each token, calculate index/sign, and build the vector
    # normalize the vector & return it

    vector = [0.0] * dim

    tokens = re.findall(r"[a-z0-9]+", query.lower())

    if not tokens:
        return vector
    
    for token in tokens:
        digest = hashlib.md5(token.encode("utf-8")).hexdigest()

        index = int(digest[:8], 16) % dim

        sign = 1.0 if int(digest[8:16], 16) % 2 == 0 else -1.0

        # if hashlib is not allowed:
        # index = simple_hash(token)
        # sign = 1.0 if simple_hash(token + "_sign") % 2 == 0 else -1.0

        vector[index] += sign

    norm = math.sqrt(sum(x * x for x in vector))

    if norm == 0:
        return vector
    
    return [x / norm for x in vector]
















































def embed_query(query: str, dim: int = 24) -> List[float]:
    # tokenize input (create separate function for this?)
    # for each token: calculate hash, index, sign, and update vector
    # normalize the vector and return it

    vector = [0.0] * dim

    tokens = re.findall(r"[a-z0-9]+", query.lower())
    
    if not tokens:
        return vector

    for token in tokens:

        # index = simple_hash(token) % dim

        # sign = 1.0 if simple_hash(token + "_sign") % 2 == 0 else -1.0

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



def retrieve(
    query: str,
    chunks: List[str],
    top_k: int = 3,
) -> List[Dict[str, Any]]:
    
    # tokenize & embed query
    # for each chunk, tokenize & embed, then calculate cosine similarity & store in list
    # sort list by similarity

    if top_k <= 0 or not chunks or not query:
        return []

    query_embedding = embed_query(query)

    scored_chunks = []

    for chunk in chunks:
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)

        scored_chunks.append({
            "text" : chunk,
            "score" : similarity
        })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]

def retrieve(
    query: str,
    chunks: List[str],
    top_k: int = 3,
) -> List[Dict[str, Any]]:

    # embed query
    # for each chunk, embed, calculate cosine similarity, store in list
    # cosine similarity = dot product / (norma * normb)
    # sort list and return top_k

    if not query or not chunks or top_k <= 0:
        return []

    query_embedding = embed_query(query)
    norm_query = math.sqrt(sum(x * x for x in query_embedding))
    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)

        similarity = 0.0

        dot = sum(x * y for x, y in zip(query_embedding, chunk_embedding))
        norm_chunk = math.sqrt(sum(y * y for y in chunk_embedding))

        if norm_query != 0 and norm_chunk != 0:
            similarity = dot / (norm_query * norm_chunk)

        scored_chunks.append({
            "index" : i,
            "text" : chunk,
            "score" : similarity
        })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]



# ---------------------------------------------------------------
# Section 2 — RAG (written answer)
# ---------------------------------------------------------------

WRITTEN_ANSWER = """

If this were a real production system, you would want to use a better embedding scheme than md5, ideally a neural network with much higher dimensionality in order to better capture semantic meaning.
If this were scaled up significantly then you would NOT want to compute chunk embeddings for every request, that's too much (unnecessary) computation.
Instead, you would want to pre-compute chunk embeddings and persist them (they do not change). Millions of embeddings, each made up of 100s or more floats, is way too much memory.
You would NOT want to calculate cosine similarity against every single chunk embedding for every request, that is too much (unnecessary) computation. Instead you'd want to use a vector-indexing scheme such as Approximate Nearest Neighbor (there are others).
There are inexpensive, commercial vector database platforms (such as Qdrant) that do all of this for you: store chunks, store embeddings, maintain vector-indexes and efficiently perform vector-search.
Also, if the queries are repeated often enough, you might want to cache those too.


""".strip()




WRITTEN_ANSWER = """
If this were a real production system, you would want to use a better embedding scheme than an md5 hash - preferably a neural network with a much higher number of dimensions, to better capture semantic meaning.
If this were a scaled up system, you would want to pre-calculate embeddings and persist them (they don't change), because re-calculating them at run-time for each query is too much computation.
Also you would likely not be able to keep all embeddings & cosine similarities in memory at once, that is too much memory.
Instead you'd want to use a vector-indexing scheme such as Approximate Nearest Neighbor (there are others) to find the top_k vectors among the nearest vectors. 
There are inexpensive commercial vector database platforms (such as Qdrant) which will do this for you: store chunks & vector embeddings, maintain a vector-index & perform efficient vector-search.
You might also want to cache query embeddings, if they are repeated often enough.
"""








































# ---------------------------------------------------------------
# Section 3 — LLM / GenAI Systems in Production
# ---------------------------------------------------------------



def assemble_prompt(question: str, retrieved: List[Dict[str, Any]]) -> str:
    # build context from retrieved blocks
    # write structured prompt & insert question + context
    # return prompt


    context_blocks = []

    for doc in retrieved:
        context_blocks.append(f"{doc['text']}")

    context = "\n\n".join(context_blocks) if context_blocks else "no context provided."


    prompt = f"""Answer the <QUESTION> using the information inside <CONTEXT>.

Do not use any outside information, or make up any information.
If the answer isn't in the context, say you don't know.

<CONTEXT>
{context}
</CONTEXT>

<QUESTION>
{question}
</QUESTION>

ANSWER:"""
    
    return prompt












































def assemble_prompt(question: str, retrieved: List[Dict[str, Any]]) -> str:
    # construct context blocks 
    # construct structured prompt and insert context, then return the prompt

    context_blocks = []

    for doc in retrieved:
        context_blocks.append(f"Document={doc['index']}\n"
                              f"{doc['text']}")

    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    prompt = f"""

You are a grounded question-answering assistant.

Instructions:
- Answer the question using only the knowledge from <CONTEXT>.
- Do not use outside information.
- Do not make up any information.
- Cite the document number/index when using information in a document to answer the question.
- If the answer is not within the context, say "I don't know from the context provided."
- Keep answers concise

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
# Run:   python practice_test_2.py
# ---------------------------------------------------------------

def _self_check() -> None:
    # ---- Section 1: embed_query ----
    v1 = embed_query("hello world")
    v2 = embed_query("hello world")
    assert v1 == v2, "embed_query must be deterministic across calls"
    assert len(v1) == 24, "default dim should be 24"
    norm = math.sqrt(sum(x * x for x in v1))
    assert abs(norm - 1.0) < 1e-9, "embed_query must return a unit vector"

    assert embed_query("") == [0.0] * 24, "empty input -> zero vector of length dim"
    assert embed_query("   ") == [0.0] * 24, "whitespace-only -> zero vector"
    assert embed_query("!!!") == [0.0] * 24, "punctuation-only -> zero vector"

    assert embed_query("Hello WORLD") == embed_query("hello world"), \
        "embed_query must be case-insensitive at the token level"

    v_custom_dim = embed_query("hello world", dim=8)
    assert len(v_custom_dim) == 8, "dim parameter must be respected"

    # ---- Section 1: retrieve ----
    chunks = [
        "Python is great for backend services and data pipelines.",
        "Cosine similarity measures the angle between two vectors.",
        "Vector databases use ANN indexes to scale similarity search.",
        "Bananas are yellow and grow in tropical climates.",
    ]

    out = retrieve("How does vector search scale?", chunks, top_k=2)
    assert isinstance(out, list) and len(out) <= 2
    assert all({"index", "text", "score"} <= set(d.keys()) for d in out), \
        "each result must have index, text, score"
    assert all(isinstance(d["index"], int) for d in out)
    assert all(isinstance(d["score"], float) for d in out)
    assert all(
        out[i]["score"] >= out[i + 1]["score"]
        for i in range(len(out) - 1)
    ), "results must be sorted by score descending"

    assert retrieve("anything", [], top_k=3) == [], "empty chunks -> []"
    assert retrieve("anything", chunks, top_k=0) == [], "top_k=0 -> []"
    assert retrieve("anything", chunks, top_k=-1) == [], "top_k<0 -> []"

    all_back = retrieve("vectors", chunks, top_k=99)
    assert len(all_back) == len(chunks), \
        "top_k > len(chunks) should return all chunks"

    # ---- Section 2: written answer is non-empty and substantive ----
    assert "TODO" not in WRITTEN_ANSWER, "fill in the written answer"
    assert len(WRITTEN_ANSWER.split()) >= 80, \
        "written answer should be at least ~8 sentences"

    # ---- Section 3: assemble_prompt ----
    prompt = assemble_prompt(
        "What is cosine similarity?",
        retrieve("What is cosine similarity?", chunks, top_k=2),
    )
    low = prompt.lower()
    for needle in ("context", "question", "cite", "don't know"):
        assert needle in low, f"prompt missing required element: {needle}"
    assert "<context>" in low and "</context>" in low, \
        "context must use explicit delimiters"
    assert "<question>" in low and "</question>" in low, \
        "question must use explicit delimiters"
    assert "score" in low and ("chunk" in low or "index" in low or "document" in low), \
        "each context chunk must be labelled with its index and score"

    empty_prompt = assemble_prompt("anything", []).lower()
    assert "context" in empty_prompt and "don't know" in empty_prompt, \
        "empty retrieval must still produce a grounded prompt with fallback"
    assert "no context" in empty_prompt, \
        "empty retrieval must include a 'no context' marker"

    print("All local sanity checks passed.")


if __name__ == "__main__":
    _self_check()







