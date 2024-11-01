# Simple RAG
## Introduction to Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is an innovative approach that combines the strengths of both information retrieval and natural language generation. By integrating a retrieval component with a generative model, RAG systems can effectively answer queries by pulling relevant information from a knowledge base, improving the quality and accuracy of generated responses.

In a typical RAG setup, when a user poses a question, the system first retrieves relevant documents or pieces of information from a database (such as text files, PDFs, or other structured data). It then uses these retrieved texts as context for a language model, enabling the generation of responses that are not only coherent but also grounded in actual data. This process significantly reduces the likelihood of hallucination (generating false information) by ensuring that the responses are based on verified sources.

---
This diagram illustrates the basic flow of the RAG system:

![Basic RAG System](assets/11.png)
---

## Project Overview

This project provides a minimal setup for building your own RAG systems, including embedding and retrieval modules. It consists of two main components:

1. **Embedding Code (`embed.py`)**: This script reads PDF files from the `data/` directory, extracts their text content, and creates embeddings using a pre-trained model. The embeddings are then saved to a `.pkl` file for later retrieval.

2. **Main Code (`main.py`)**: This script loads the embeddings, accepts a user query, retrieves the most relevant documents based on the query, and utilizes a generative language model to produce a coherent response.
   
---

## How to Use This Project

This project can be run as-is for educational purposes or can be adapted to suit your needs. You can enhance the code by:
- Adding more PDF documents to the `data/` directory to expand the knowledge base.
- Fine-tuning the embedding model or generative model to improve performance on your specific data.
- Implementing additional features such as multi-document retrieval, query processing, and advanced response generation.

By following the steps outlined in this README, you can set up a functional RAG system that demonstrates the power of combining retrieval and generation in AI applications.

---

## Table of Contents

- [Introduction to Retrieval-Augmented Generation (RAG)](#introduction-to-retrieval-augmented-generation-rag)
- [Project Overview](#project-overview)
- [How to Use This Project](#how-to-use-this-project)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Project](#running-the-project)
- [License](#license)


---

## Project Structure

```perl
project-root/ ├── data/ # Directory for input PDF documents │ ├── document1.pdf # Example document 1 │ ├── document2.pdf # Example document 2 │ └── document3.pdf # Example document 3 ├── code/ # Directory containing the main code files │ ├── embed.py # Script to read PDFs, create embeddings, and save them │ └── main.py # Script to handle user queries and generate responses ├── requirements.txt # List of dependencies for the project └── README.md # Project documentation and instructions
```
---

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package installer, which is usually included with Python installations.

### Installation

1. **Clone the repository**:
   Open your terminal or command prompt and run the following command to clone the project:

   ```bash
   git clone https://github.com/thechaiexperiment/Simple-RAG.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Simple-RAG
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
## Running the Project
1. **Prepare your data**: Place your PDF documents in the data/ directory. Ensure that the documents contain relevant information for your queries.
2. **Create embeddings**:
   ```bash
   python code/embed.py
3. **Interact with the RAG system**:
   ```bash
   python code/main.py
 
## License
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.
