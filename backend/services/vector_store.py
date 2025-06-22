
import chromadb
from llama_index.embeddings.openai import OpenAIEmbedding

db = chromadb.Client()
collection = db.get_or_create_collection("docs")
embedder = OpenAIEmbedding(model="text-embedding-ada-002")

def store_vectors(chunks):
    for i, chunk in enumerate(chunks):
        embedding = embedder.get_text_embedding(chunk)
        collection.add(documents=[chunk], ids=[str(i)], embeddings=[embedding])

def query_vectors(question):
    embedding = embedder.get_text_embedding(question)
    results = collection.query(query_embeddings=[embedding], n_results=3)
    return results["documents"][0]
