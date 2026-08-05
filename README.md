# 📚 Research Paper Chatbot using RAG

An AI-powered chatbot that allows users to ask questions about research papers and receive accurate answers based on the uploaded documents. The project uses Retrieval-Augmented Generation (RAG) to combine document retrieval with Large Language Models (LLMs), reducing hallucinations and providing context-aware responses.

## 🚀 Overview

Reading and understanding multiple research papers can be time-consuming. This project provides an intelligent assistant that allows users to upload PDF documents and interact with them using natural language.

The system:
- Extracts text from research papers
- Splits documents into meaningful chunks
- Generates vector embeddings
- Stores embeddings in a vector database
- Retrieves relevant information based on user queries
- Uses an LLM to generate answers grounded in the retrieved context

## ✨ Features

- 📄 Upload research papers in PDF format
- 🔎 Semantic search over document content
- 🤖 LLM-based question answering
- 📚 Support for multiple documents
- 🔗 Context-aware responses using RAG
- 📌 Source retrieval for answer verification
- 🖥️ Interactive interface using Streamlit


## 🛠️ Technologies

- Python
- LangChain
- OpenAI API / Llama models
- Sentence Transformers
- FAISS Vector Database
- PyPDF
- Streamlit

  
## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/username/paper-chatbot.git
cd paper-chatbot

Create a virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
🔑 Configuration

Create an environment file:

OPENAI_API_KEY=your_api_key

▶️ Run the Application

Start the Streamlit app:

streamlit run app.py

Open your browser:

http://localhost:8501

👩‍💻 Author

Ghinwa Fakih

PhD in Computer Science
Research interests: Knowledge Graphs, Semantic Web, NLP, and Large Language Models
