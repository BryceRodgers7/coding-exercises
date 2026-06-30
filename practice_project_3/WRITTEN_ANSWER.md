# Section 3 — Written Reasoning Question

> Your team has shipped a RAG-style claims assistant that answers natural-language questions over the retrieved claim records. Adjusters have started reporting **unsupported answers** — confident-sounding responses that cite real claims but make assertions that the cited claim does not actually contain.
>
> 1. Describe **how you would diagnose** the prevalence and patterns of these unsupported answers in production. Be specific about telemetry, evaluation methods, and labeling strategy.
> 2. Describe **how you would reduce** their frequency. Cover BOTH retrieval-side mitigations (what the system feeds the model) AND generation-side mitigations (how the model is prompted and constrained), and name specific techniques or product categories where applicable.

---

In order to diagnose prevalence and patterns of unsupported answers, you must first log (query, retrieved_documents, document_scores, final_prompt, generated_answer).
Then you'd want to perform AUTOMATED FAITHFULNESS SCORING by using RAGAS (requiring human-written ground truth) and/or LLM-as-judge across a cross-section of system calls, then SLICE FAILURE RATES by query intent and retrieval score to find where the bad answers cluster.

To reduce their frequence you'd want to use hybrid search (BM25 + vector) and re-rank top retrieved documents using a cross-encoder.
You would also want to give the LLM instructions to ground its responses, for example "only use information from the <CONTEXT>" and "if the answer is not in the context, say you don't know".
And finally, tell it to return structured output, including citing the document/chunk so you can log it and verify later.














































## Your answer

In order to diagnose you first need to log relevant information such as (query, retrieved_docs, doc_scores, prompt, generated_answer). 
Next you would want to run an automated faithfulness check using RAGAS (with human-intervetion to add ground truth) or LLM-as-a-judge against a cross-section of calls to the system  and slice by retrieval score or query intent to identify where the problems are occurring. 

To reduce the occurrances you would want to use hybrid search (keyword matching + vector similarity), re-rank top results by using a cross-encoder and abstain when nothing crosses a retrieval-confidence threshold.
You would also give grounding instructions to the LLM such as "only use information from <CONTEXT>" and "if the answer is not in the context then say you don't know", as well as require structured output including citations/DocID that you can use to verify.

