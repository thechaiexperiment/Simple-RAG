# retriever.py

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

class SimpleRetriever:
    def __init__(self, documents):
        # Initialize the retriever with a list of documents and an embedding model
        self.documents = documents
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # You can choose any suitable embedding model
        self.document_embeddings = self.embed_documents(documents)

    def embed_documents(self, documents):
        # Generate embeddings for each document in the list
        return self.model.encode(documents)

    def retrieve(self, query, top_k=3):
        # Generate embeddings for the query
        query_embedding = self.model.encode([query])
        # Calculate cosine similarity between query and document embeddings
        similarities = cosine_similarity(query_embedding, self.document_embeddings).flatten()
        # Get indices of top-k similar documents
        top_k_indices = np.argsort(similarities)[-top_k:][::-1]
        # Return the top-k documents
        return [(self.documents[idx], similarities[idx]) for idx in top_k_indices]
