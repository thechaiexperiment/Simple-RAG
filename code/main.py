# code/main.py

import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

def load_embeddings(embeddings_file):
    with open(embeddings_file, 'rb') as f:
        embeddings = pickle.load(f)
    return embeddings

def get_user_query():
    return input("Enter your query: ")

def retrieve_documents(embeddings, user_query, texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Same model used for embeddings
    user_embedding = model.encode([user_query])
    
    # Compute cosine similarity
    similarities = cosine_similarity(user_embedding, embeddings)
    relevant_index = np.argmax(similarities)
    
    return texts[relevant_index], similarities[0][relevant_index]

def generate_response(retrieved_text, user_query):
    generator = pipeline('text-generation', model='gpt2')  # Use any LLM you prefer
    prompt = f"User query: {user_query}\nRelevant information: {retrieved_text}\nResponse:"
    response = generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text']

def main():
    embeddings_file = 'embeddings.pkl'
    
    # Load the embeddings
    embeddings = load_embeddings(embeddings_file)

    # Load the original texts for reference (you can modify this to fit your structure)
    texts = extract_text_from_pdfs('../data/')

    # Get user query
    user_query = get_user_query()

    # Retrieve relevant documents based on the user query
    retrieved_text, similarity_score = retrieve_documents(embeddings, user_query, texts)
    
    # Generate a response
    response = generate_response(retrieved_text, user_query)
    print("Response:", response)

if __name__ == "__main__":
    main()
