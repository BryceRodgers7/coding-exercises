# Section 3 — Reference Written Answer

> **THIS IS THE REFERENCE ANSWER — study it, don't just copy.**
> Your practice file is `WRITTEN_ANSWER.md`. The visible test for
> Section 3 reads from that file, not this one.

---

## Recap of the question

Your team has shipped a RAG-style claims assistant that answers natural-language questions over the retrieved claim records. Adjusters have started reporting **unsupported answers** — confident-sounding responses that cite real claims but make assertions that the cited claim does not actually contain.

1. Describe **how you would diagnose** the prevalence and patterns of these unsupported answers in production.
2. Describe **how you would reduce** their frequency (retrieval-side AND generation-side).

---

## Reference answer (3 sentences, ~110 words)

**Diagnosis.** Log every production interaction as `(query, retrieved_chunk_ids, retrieval_scores, generated_answer, parsed_citations)` and run automated faithfulness scoring (RAGAS, TruLens, or LLM-as-judge) on a stratified sample backed by human-labelled ground truth — then slice failure rates by query intent and top retrieval score to find where unsupported answers cluster.

**Retrieval-side reduction.** Switch from pure dense search to **hybrid search** (BM25 + vector) so exact identifiers match literally, run the top-N through a **cross-encoder reranker** (Cohere Rerank, BGE-reranker), and **abstain** when no chunk crosses a retrieval-confidence threshold instead of feeding the model weak context.

**Generation-side reduction.** Prompt for explicit grounding ("answer only from <CONTEXT>, otherwise reply 'I don't know'"), require **structured output with citation IDs** that you programmatically verify against the retrieved set, and lower temperature for factual queries.

---

## Keywords to remember (the actual currency of the grade)

- **Diagnosis:** logging tuples, RAGAS / TruLens / LLM-as-judge, stratified human labels, slice by retrieval score.
- **Retrieval side:** hybrid search (BM25 + dense), cross-encoder reranker (Cohere Rerank, BGE), abstention threshold.
- **Generation side:** grounding prompt, "I don't know" fallback, structured output + citation IDs, low temperature.
