# code/embed.py

import os
import pickle
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer

def extract_text_from_pdfs(data_directory):
    texts = []
    for filename in os.listdir(data_directory):
        if filename.endswith('.pdf'):
            doc = fitz.open(os.path.join(data_directory, filename))
            text = ""
            for page in doc:
                text += page.get_text()
            texts.append(text)
    return texts

def embed_texts(texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # You can choose other models too
    embeddings = model.encode(texts)
    return embeddings

def save_embeddings(embeddings, output_file):
    with open(output_file, 'wb') as f:
        pickle.dump(embeddings, f)

def main():
    data_directory = '../data/'
    output_file = 'embeddings.pkl'

    # Extract texts from PDFs
    texts = extract_text_from_pdfs(data_directory)

    # Embed the texts
    embeddings = embed_texts(texts)

    # Save the embeddings
    save_embeddings(embeddings, output_file)

if __name__ == "__main__":
    main()
