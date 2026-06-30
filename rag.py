# imports
































































import math
import re
import hashlib
from typing import List, Dict, Any


import math
import re
import hashlib
from typing import List, Dict, Any


import hashlib
import re
import math
from typing import List, Dict, Any



# tokenize























































def tokenize(text: str) -> List[str]:
    # return list of lowercase alphanumeric words/tokens

    if not text:
        return []
    
    return re.findall(r"[a-z0-9]+", text.lower())

def tokenize(text: str) -> List[str]:

    # reduce to alphanumeric & return list of words

    if not text:
        return []
    
    return re.findall(r"[a-z0-9]+", text.lower())

def tokenize(text: str) -> List[str]:

    # return list of alphanumeric words, all lowercase for simplicity

    if not text:
        return []
    
    return re.findall(r"[a-z0-9]+", text.lower())

def tokenize(text: str) -> List[str]:

    # return list of words

    if not text:
        return []
    
    return re.findall(r"[a-z0-9]+", text.lower())

def tokenize(text: str) -> List[str]:

    if not text:
        return []
    
    return re.findall(r"[a-z0-9]+", text.lower())


def tokenize(text: str) -> List[str]:

    if not text:
        return []
    
    return re.findall(r"[a-z0-9]+", text.lower())


def tokenize(text: str) -> List[str]:

    if not text:
        return []
    
    return re.findall(r"[a-z0-9]+", text.lower())


# tokenize function:

def tokenize(text: str) -> List[str]:

    # convert string to lower case, then .split()

    if not text:
        return []

    return re.findall(r"[a-z0-9]+", text.lower())

# tokenize:

# string in, list of strings out. Convert one string into a list of words (lower case)

def tokenize(text: str) -> List[str]:
    """
    Lowercase and split text into simple word tokens.
    """
    if not text:
        return []

    return re.findall(r"[a-z0-9]+", text.lower())



# embed query






















































def embed_query(query: str, dim: int = 16) -> List[float]:

    # tokenize query
    # for each token, hash (md5), calculate index, sign, and update vector
    # normalize & return vector


    vector = [0.0] * dim
    tokens = tokenize(query)

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

def embed_query(text: str, dim: int = 16) -> List[float]:

    # tokenize text, for each word: calculate hash, index, sign, the update vector
    # normalize vector & return

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


def embed_query(query: str, dim: int = 16) -> List[float]:

    # hash each word in the query using md5, find the index, sign, and update the vector
    # normalize & return vector

    vector = [0.0] * dim
    tokens = tokenize(query)

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


def embed_query(query: str, dim: int = 16) -> List[float]:

    # tokenize query, for each word: hash, calculate index & sign, update vector. 
    # normalize vector & return

    vector = [0.0] * dim
    tokens = tokenize(query)

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


def embed_query(query: str, dim: int = 16) -> List[float]:

    # tokenize query, calculate hash, index, sign, vector
    # normalize, return normalized vector

    vector = [0.0] * dim
    tokens = tokenize(query)

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


def embed_query(query: str, dim: int = 16) -> List[float]:

    vector = [0.0] * dim
    tokens = tokenize(query)

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



def embed_query(text: str, dim: int = 16) -> List[float]:
    
    vector = [0.0] * dim
    tokens = tokenize(text)

    if not tokens:
        return vector    

    for token in tokens:
        # digest, index, sign, vector
        digest = hashlib.md5(token.encode("utf-8")).hexdigest()

        index = int(digest[:8], 16) % dim

        sign = 1.0 if int(digest[8:16], 16) % 2 == 0 else -1.0

        vector[index] += sign

    norm = math.sqrt(sum(x * x for x in vector))

    if norm == 0:
        return vector

    return [x / norm for x in vector]


# embed query: list of words in, dimensionality in, list of floats out

def embed_query(text: str, dim: int = 16) -> List[float]:

    # tokenize text, init vector at 0 * dim
    # scan thru each word in list, hash it, find the vector dimension (index), move it up or down
    # return normalized vector: 1/sum(sqrt(x**2)) 

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


# embed query:

# string in, dimension-count in, list of floats out. Convert the string to an embedding of dimension-length floats.

def embed_query(text: str, dim: int = 16) -> List[float]:
    """
    Deterministic mock embedding.

    Requirements hit:
    - same text always produces same vector
    - semantically-ish related text shares token-based signal
    - vector is normalized to unit length
    - handles empty input safely
    """
    vector = [0.0] * dim
    tokens = tokenize(text)

    if not tokens:
        return vector

    for token in tokens:
        # Stable hash, unlike Python's built-in hash()
        digest = hashlib.md5(token.encode("utf-8")).hexdigest()

        # Map token to a dimension
        index = int(digest[:8], 16) % dim

        # Use another part of hash to choose direction
        sign = 1.0 if int(digest[8:16], 16) % 2 == 0 else -1.0

        vector[index] += sign

    norm = math.sqrt(sum(x * x for x in vector))

    if norm == 0:
        return vector

    return [x / norm for x in vector]



# cosine similarity





















































def cosine_similarity(a: List[float], b: List[float]) -> float:

    # calculate dot product, norm_a, and norm_b
    # normalize dot product and return it

    if not a or not b or len(a) != len(b):
        return 0.0
    
    dot = sum(x * y for x, y in zip(a,b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)


def cosine_similarity(a: List[float], b: List[float]) -> float:

    # calculate dot product
    # calculate norm-a and norm-b
    # normalize & return dot product

    if not a or not b or len(a) != len(b):
        return 0.0


    dot = sum(x * y for x, y in zip(a,b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)

def cosine_similarity(a: List[float], b: List[float]) -> float:

    # calculate dot-product of both vectors
    # calculate norm_a and norm_b
    # normalize dot-product & return it

    if not a or not b or len(a) != len(b):
        return 0.0
    
    dot = sum(x * y for x, y in zip(a,b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)


def cosine_similarity(a: List[float], b: List[float]) -> float:

    # calculate dot, norm_a, norm_b, normalize dot & return

    if not a or not b or len(a) != len(b):
        return 0.0
    
    dot = sum(x * y for x, y in zip(a,b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)

def cosine_similarity(a: List[float], b: List[float]) -> float:

    # calcualte dot, norm_a, norm_b, normalize dot & return

    if not a or not b or len(a) != len(b):
        return 0.0
    
    dot = sum(x * y for x, y in zip(a,b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)


def cosine_similarity(a: List[float], b: List[float]) -> float:

    # calculate dot a and b
    # calculate norma & normb
    # return normalized dot

    if not a or not b or len(a) != len(b):
        return 0.0
    
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)


def cosine_similarity(a: List[float], b: List[float]) -> float:

    if not a or not b or len(a) != len(b):
        return 0.0
    
    dot = sum(x * y for x, y in zip(a,b))

    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)

# cosine_similarity function: list of floats in, another list of floats in, float out

def cosine_similarity(a: List[float], b: List[float]) -> float:

    # calculate dot product
    # calculate norms
    # return dot / (norma * normb)

    if not a or not b or len(a) != len(b):
        return 0.0

    dot = sum(x * y for x, y in zip(a,b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)

def cosine_similarity(a: List[float], b: List[float]) -> float:
    """
    Cosine similarity.

    Since embed_query() returns normalized vectors, this is usually
    just the dot product. This version is defensive in case raw vectors
    are passed in.
    """
    if not a or not b or len(a) != len(b):
        return 0.0

    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)



# retrieve





















































def retrieve(query: str, chunks: List[str], top_k: int = 3) -> List[Dict[str, any]]:

    # calculate query embedding
    # for each chunk, calculate chunk embedding, cosine similarity w/ query, and store in list
    # sort list by cosine similarity & return top_k items

    if top_k <= 0 or not chunks:
        return []
    
    query_embedding = embed_query(query)

    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)
        scored_chunks.append({
            "index" : i,
            "score" : similarity,
            "text" : chunk
        })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]

def retrieve(query: str, chunks: List[str], top_k: int = 3) -> List[Dict[str, any]]:

    # calc query embedding
    # for each chunk, calculate embedding, similarity w/ query, store in list
    # sort list, return top_k results


    if top_k <= 0 or not chunks:
        return []

    query_embedding = embed_query(query)

    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)
        scored_chunks.append({
            "index" : i,
            "score" : similarity,
            "text" : chunk
        })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]


def retrieve(query: str, chunks: List[str], top_k: int = 3) -> List[Dict[str, any]]:

    # calculate query embedding
    # for each chunk, calculate chunk embedding, calculate cosine similarity, store in list
    # sort list by score, return top_k results

    if top_k <= 0:
        return []
    
    query_embedding = embed_query(query)
    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)
        scored_chunks.append({
            "index" : i,
            "score" : similarity,
            "text" : chunk
        })

    scored_chunks.sort(key= lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]

def retrieve(query: str, chunks: List[str], top_k: int = 3) -> List[Dict[str, any]]:

    # calculate query embedding
    # for each chunk, calculate embedding, cosine similarity with query, add to data structure
    # sort data structure by similiarty score & return top_k items

    if top_k <= 0:
        return []
    
    query_embedding = embed_query(query)
    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)
        scored_chunks.append({
            "index" : i,
            "score" : similarity,
            "text" : chunk
        })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]


def retrieve(query: str, chunks: List[str], top_k: int = 3) -> List[Dict[str, any]]:

    # embed query, embed each chunk & calc cosine similarity
    # sort by cosine similarity & return top_k results

    if not query or top_k <= 0: 
        return []
    
    query_embedding = embed_query(query)

    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)

        scored_chunks.append({
            "index" : i,
            "score" : similarity,
            "text" : chunk
        })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]


def retrieve(query: str, chunks: List[str], top_k: int = 3) -> List[Dict[str, any]]:

    if top_k <= 0:
        return []
    
    # embed query
    # for each chunk, embed and calculate cosine similarity (store in list)
    # sort list for cosine similarity scores, return top_k 


    query_embedding = embed_query(query)

    scored_docs = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)

        scored_docs.append({
            "index" : i,
            "score" : similarity,
            "text" : chunk
        })

    scored_docs.sort(key=lambda item: item["score"], reverse=True)

    return scored_docs[:top_k]

def retrieve(query: str, chunks: List[str], top_k: int = 3) -> List[Dict[str, any]]:

    if top_k <= 0 or not query:
        return []
    
    query_embedding = embed_query(query)

    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)

        scored_chunks.append({"index" : i,
                              "text": chunk,
            "score" : similarity})
        
    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]


# retrieve funciton: query in, list of chunks in, top_k in, list of dicts out

def retrieve(query: str, chunks: List[str], top_k : int = 3) -> List[Dict[str, any]]:

    # embed query
    # embed each chunk, calculate cosine similarity w/ query, add result to list
    # sort list by descending score & return top_k items

    if not query or top_k <= 0 or not chunks:
        return []
    
    query_embedding = embed_query(query)
    chunk_scores = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        similarity = cosine_similarity(query_embedding, chunk_embedding)
        chunk_scores.append({"index": i, "text": chunk, "score": similarity})

    chunk_scores.sort(key=lambda item: item["score"], reverse=True)

    return chunk_scores[:top_k]


def retrieve(
    query: str,
    chunks: List[str],
    top_k: int = 3
) -> List[Dict[str, Any]]:

    if top_k <= 0 or not chunks:
        return []

    query_embedding = embed_query(query)

    scored_chunks = []

    for i, chunk in enumerate(chunks):
        chunk_embedding = embed_query(chunk)
        score = cosine_similarity(query_embedding, chunk_embedding)

        scored_chunks.append({
            "index": i,
            "text": chunk,
            "score": score,
        })

    scored_chunks.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return scored_chunks[:min(top_k, len(scored_chunks))]




# build_prompt
























































def build_prompt(question: str, retrieved_docs: List[Dict[str, any]]) -> str:

    # construct context from retrieved docs
    # construct structured prompt & insert context
    # return prompt

    context_blocks = []

    for i, doc in enumerate(retrieved_docs, start=1):
        context_blocks.append(f"[Document={i} | Score={doc['score']:.4f}]\n"
                              f"{doc['text']}")
        
    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    prompt = f"""

You are a grounded question-answering assistant.

Instructions:
- Answer the question using only information from the <CONTEXT>.
- Do not use outside knowledge.
- Do not make up information.
- Cite the document number when using information from the context.
- If the answer is not in the context, say "I don't know from the context provided."
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


def build_prompt(query: str, retrieved_docs: List[Dict[str, any]]) -> str:

    # create context
    # structure prompt & inject context
    # return prompt

    context_blocks = []

    for i, doc in enumerate(retrieved_docs, start=1):
        context_blocks.append(f"[Document={i} | Score={doc['score']:.4f}]\n"
                              f"{doc['text']}")
        
    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."


    prompt = f"""
You are a grounded question-answering assistant.

Instructions:
- Answer the question using only the information in the <CONTEXT> provided.
- Do not use outside knowledge.
- Do not make up any information.
- Cite the document when using information from the <CONTEXT>.
- If the answer is not in the <CONTEXT> then say "I don't know, from the context provided."
- Keep answers concise
<CONTEXT>
{context}
</CONTEXT>

<QUESTION>
{query}
</QUESTION>

ANSWER:
""".strip()
    
    return prompt


def build_prompt(query: str, retrieved_docs: List[Dict[str, any]]) -> str:

    # create context
    # write prompt structure & insert context
    # return prompt

    context_blocks = []

    for i, doc in enumerate(retrieved_docs, start=1):
        context_blocks.append(f"[Document={i} | Score={doc['score']:.4f}\n]"
                              f"{doc['text']}")
        
    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    prompt = f"""

You are a grounded question-answering assistant.

Instructions:
- Answer the question using only information from the <CONTEXT>.
- Do not use outside knowledge.
- Do not make up information.
- Cite the document when using information from the <CONTEXT>.
- If the answer is not contained in the <CONTEXT> then say "I don't know, from the context provided."
- Keep answers concise.

<CONTEXT>
{context}
</CONTEXT>

<QUESTION>
{query}
</QUESTION>


ANSWER:
""".strip()
    
    return prompt


def build_prompt(query: str, retrieved_docs: List[Dict[str, any]]) -> str:

    # construct context, write structured prompt, insert context & query, return prompt

    context_blocks = []

    for i, doc in enumerate(retrieved_docs, start=1):
        context_blocks.append(f"[Document={i} | Score={doc['score']:.4f}\n]"
                              f"{doc['text']}")
        
    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    prompt = f"""

You are a grounded question-answering assistant.

Instructions:
- Answer the question using the CONTEXT provided
- Do not use outside information
- Do not make up any information
- Cite the document when you use information from the CONTEXT
- If the answer is not in the CONTEXT then say "I don't know from the context retrieved."
- Keep answers concise

<QUESTION>
{query}
</QUESTION>

<CONTEXT>
{context}
</CONTEXT>

ANSWER:
""".strip()
    
    return prompt


def build_prompt(question: str, retrieved_docs: List[Dict[str, any]]) -> str:

    # construct context, structure prompt, insert context + question, return prompt 

    context_blocks = []

    for i, doc in enumerate(retrieved_docs, start=1):
        context_blocks.append(
            f"[Document={i} | Score={doc['score']:.4f}]\n]"
            f"{doc['text']}"
        )

    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    prompt = f"""

You are a grounded question-answering assistant.

Instructions:
- Answer the question using only the information in the provided <CONTEXT>
- Do not use outside information
- Do not make up information
- Cite the document number when you use information from it
- If the answer is not within the provided <CONTEXT> then say "I don't know, from the context retrieved."
- Keep answers concise

<QUESTION>
{question}
</QUESTION>

<CONTEXT>
{context}
</CONTEXT>

ANSWER:
""".strip()
    
    return prompt


def build_prompt(query: str, retrieved_docs: List[Dict[str, any]]) -> str:


    # create context
    # write prompt structure
    # insert question & context, then return


    context_blocks = []

    for i, doc in enumerate(retrieved_docs, start=1):
        context_blocks.append(f"[Document={i} | Score={doc['score']:.4f}\n]"
                       f"{doc['text']}")
        

    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    prompt = f"""

You are a grounded question-answering assistant.

Instructions:
- Answer the question using the <CONTEXT> provided
- Do not use outside information, only use information from the <CONTEXT>
- Do not make up any information
- Cite the document number when using information from the context
- If the answer is not in the <CONTEXT> say "I don't know, from the context provided."
- Keep answers concise

<QUESTION>
{query}
</QUESTION>

<CONTEXT>
{context}
</CONTEXT>

ANSWER:
""".strip()
    
    return prompt


def build_prompt(query: str, retrieved_chunks: List[str]) -> str:

    context_blocks = []

    for i, doc in enumerate(retrieved_chunks, start=1):
        context_blocks.append(f"[Document {i} | Score {doc['score']:.4f}]\n"
                              f"{doc['text']}")

    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    
    prompt = f"""

You are a grounded question-answering assistant.

Instructions:
- Answer the question using only the information in <CONTEXT>
- Do not use any outside information
- Do not make up any information
- Cite the document number when using information in the context.
- If the answer to the question is not contained within the <CONTEXT> then say "I don't know, using the context provided."
- Keep the answer concise

<QUESTION>
{query}
</QUESTION>

<CONTEXT>
{context}
</CONTEXT>

ANSWER:
""".strip()
    
    return prompt

# build_prompt function: question/string in, list of dicts / scored strings (context) in, string out

def build_prompt(question: str, retrieved_docs: List[Dict[str, any]]) -> str:

    # arrange question & retrieved docs into a big prompt and return it

    context_blocks = []

    for i, doc in enumerate(retrieved_docs, start=1):
        context_blocks.append(
            f"[Chunk[{i}] | score={doc['score']:.4f}]\n"
            f"{doc['text']}") 

    context = "\n\n".join(context_blocks) if context_blocks else "no context retrieved."

    prompt = f"""

You are a grounded question-answering assistant. 

Instructions:
- Answer the question using only information within <CONTEXT>
- Do not make up any information.
- Do not use any outside information.
- Cite the chunk number when using information in the context.
- If the answer isn't in the context say "I don't know from the context given".
- Keep the answer concise.

<QUESTION>
{question}
</QUESTION>

<CONTEXT>
{context}
</CONTEXT>

ANSWER:
    """.strip()
    return prompt


def build_prompt(query: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
    """
    Assemble a grounded RAG prompt.

    Requirements hit:
    - includes question
    - includes retrieved context
    - uses explicit delimiters
    - gives grounding instructions
    - tells model what to do when answer is missing
    """
    context_blocks = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_blocks.append(
            f"[Chunk {i} | score={chunk['score']:.4f}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_blocks) if context_blocks else "No context retrieved."

    prompt = f"""
You are a grounded question-answering assistant.

Instructions:
- Answer the user question using only the information inside <CONTEXT>.
- Do not use outside knowledge.
- If the answer is not present in the context, say: "I don't know based on the provided context."
- Cite the chunk number when you use information from the context.
- Keep the answer concise.

<CONTEXT>
{context}
</CONTEXT>

<QUESTION>
{query}
</QUESTION>

Answer:
""".strip()

    return prompt



# answer_with_mock_rag
























































def answer_with_mock_rag(question: str, chunks: List[str], top_k: int = 3) -> str:

    # retrieve docs for the question
    # build & return prompt from retrieved docs

    retrieved_docs = retrieve(question, chunks, top_k)
    prompt = build_prompt(question, retrieved_docs)

    return prompt


def answer_with_mock_rag(query: str, chunks: List[str], top_k: int = 3) -> str:

    # retrieve documents for query
    # build prompt using retrieved documents and return it

    retrieved_docs = retrieve(query, chunks, top_k)
    prompt = build_prompt(query, retrieved_docs)

    return prompt

def answer_with_mock_rag(query: str, chunks: List[str], top_k: int = 3) -> str:

    # retrieve documents from chunks
    # build prompt from retrieved documents & return

    retrieved_docs = retrieve(query, chunks, top_k)
    prompt = build_prompt(query, retrieved_docs)

    return prompt

def answer_with_mock_rag(query: str, chunks: List[str], top_k: int = 3) -> str:

    # retrieve relevant documents
    # build prompt & return it

    retrieved_docs = retrieve(query, chunks, top_k)
    prompt = build_prompt(query, retrieved_docs)

    return prompt


def answer_with_mock_rag(query: str, chunks: List[str], top_k: int = 3) -> str:

    # retrieve documents for query, build prompt from retrieved documents & return prompt

    retrieved_docs = retrieve(query, chunks, top_k)
    prompt = build_prompt(query, retrieved_docs)

    return prompt


def answer_with_mock_rag(question: str, chunks: List[str], top_k: int = 3) -> str:

    # retrieve docs from chunks, build & return prompt
    retrieved_docs = retrieve(question, chunks, top_k)
    prompt = build_prompt(question, retrieved_docs)

    return prompt

def answer_with_mock_rag(question: str, chunks: List[str], top_k: int = 3) -> str:

    retrieved_docs = retrieve(question, chunks, top_k)
    prompt = build_prompt(question, retrieved_docs)

    return prompt

    # answer = llm(prompt)
    # return answer


def answer_with_mock_rag(query: str, chunks: List[str], top_k: int = 3) -> str:
    """
    Full mock RAG pipeline.
    """
    retrieved = retrieve(query, chunks, top_k)
    return build_prompt(query, retrieved)


if __name__ == "__main__":
    chunks = [
        "Python is commonly used for backend development, data science, and automation.",
        "RAG systems retrieve relevant context before assembling a prompt for an LLM.",
        "Cosine similarity measures the angle between two vectors.",
        "Vector databases use indexes to efficiently search millions of embeddings.",
        "Caching embeddings avoids recomputing them for the same documents or queries.",
    ]

    query = "How does a RAG system find relevant information?"

    results = retrieve(query, chunks, top_k=3)

    print("Retrieved chunks:")
    for result in results:
        print(result)

    print("\nPrompt:")
    print(answer_with_mock_rag(query, chunks, top_k=3))






# notes:

























































# if this were a real production system, we would probably want to use a better embedding scheme than md5, a neural network with more than 16 dimensions would capture semantic meaning better.
# if this were scaled up, we would NOT want to calculate embeddings at run-time for every query/request. That would be too much computation.
# instead you'd want to pre-compute embeddings and store them on disk (they don't change). 10M vectors made up of 100's or more floats is way too much memory.
# Also you wouldn't want to check the cosine similarity between the query and every chunk, you'd want to use a vector-indexing scheme such as Approximate Nearest Neighbor. 
# There are cheap, commercial products/platforms out there (such as Qdrant) which will do all of this for you: store your chunks, embeddings, and perform optimized vector-search.
# you may also want to cache the query embeddings, if they are re-used often enough.

# if this were a real production system, you'd want to use a better embedding scheme than hashlib.md5, a neural-network would be best. Also more dimensions would capture better semantic meaning.
# if this were a large-scale production system, you would NOT want to calculate the embedding every single request. 
# instead you'd want to pre-calculate all of the embeddings & store them on-disk since they don't change. 10M vectors each with hundreds of flots or more, is a ton of memory.
# Also you would not want to calculate cosine similarity with every chunk, for every request, that's too much. You can use a vector-indexing scheme such as Approximate Nearest Neighbor (or others).
# there are commercial vector databases such as Qdrant which will do all of this for you - store your embeddings, and perform optimized vector search. 
# you may also want to cache the embeddings of actual queries, if they are repeated often enough. 


# if this were a real production system, we would want to use a better embedding strategy than md5, to capture semantic meaning better.
# if this were a real production system, or just scaled up, we would definitely not want to re-calculate the embeddings for every request.
# instead we would want to pre-compute the embeddings, and store them on-disk because 10M floats is a huge amount of memory.
# instead of checking cosine similarity with every single doc, we would want to use a vector-indexing scheme such as Approximate Nearest Neighbor.
# There are commercial vector databases which can handle all of this for us such as Qdrant; storing embeddings, and performing an optimized vector search.
# if the same queries are used often enough, it might even be good to cache those too, instead of recomputing every request.


# If this were a real PRD system, scaled up to 10M+ then you would not want to (re)calculate the embeddings every query - only the query (and maybe cache those if the same things are searched often enough).
# Instead you'd want to pre-compute the embeddings, and probably store them on disk (since 10m floats is a lot of memory).
# You'd want to use a vector-indexing scheme such as Approximate Nearest Neighbor (there are others) instead of comparing every single chunk against the query.
# Also you would want to use a better embedding scheme, hashlib.md5 is a crude bag-of-word approach but a higher-dimensional Neural Network would capture semantics meaning better. 
# A proper solution would probably use a vector database SaaS platform such as Qdrant. It would assist with each of these problems, providing different indexing methods, storing embeddings, and performing vector search.


# if this were a real rag system, scaled up, we would use a better embedding model than the first few digits of a md5 hash, to better capture the semantics of the queries/docs
# also we would definitely not want to calculate the embeddings every time there is a query. 
# The embeddings should be pre-calculated & stored on-disk because the computation of calculating them everytime is a huge waste, and storing them requires a lot of memory (plus they do not change).
# possibly also want to cache the queries/questions, if they are repeated often enough
# to quickly search through a huge number of embeddings, use an Approximate Nearest Neighbor method, or some other sort of vector-indexing scheme. 
# vector database products such as Qdrant provide all of these features: higher-dimensional embeddings, and easily usable vector indexes.



# if this were a real system, you would definitely not want to calculate the chunk embeddings at run-time like this, for every question. 
# You would want to pre-calculate it once and cache it (preferrably on-disk because millions of floats is a lot of memory)
# possibly even cache the queries/questions too, if they are repeated often enough
# you would want to use a proper vector database SaaS platform (such as Qdrant) which utilizes a vector-indexing system (Approximate Nearest Neighbor)
# There are several distinct ways of doing ANN, we'd just have to pick one based on the use-case








































