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


## 📂 Project Structure

```
paper-chatbot/
│
├── app.py                 # Streamlit user interface
├── rag.py                 # RAG pipeline implementation
├── utils.py               # PDF processing utilities
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
├── data/                  # PDF documents
└── README.md              # Documentation
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/paper-chatbot.git
cd paper-chatbot
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace:

```
your_api_key_here
```

with your OpenAI API key.

---

# ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

If it does not open automatically, visit:

```
http://localhost:8501
```

---

# 💡 Example Questions

After uploading a research paper, you can ask:

- What is the main contribution of this paper?
- Explain the proposed methodology.
- What are the limitations of this approach?
- Summarize the key findings.
- Compare two research papers.
- Explain this concept in simple terms.

---

# 📈 Future Improvements

- Add conversation memory for multi-turn discussions
- Support additional formats (DOCX, HTML, Markdown)
- Add automatic research paper summarization
- Generate citations with page references
- Compare multiple papers automatically
- Integrate local LLMs such as Llama 3 or Mistral
- Add evaluation metrics for RAG performance

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Text Embeddings
- Vector Databases
- Semantic Search
- Document Processing
- Building AI applications with Python

---

# 👩‍💻 Author

**Ghinwa Fakih**

PhD in Computer Science

Research interests:
- Knowledge Graphs
- Semantic Web
- Natural Language Processing (NLP)
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
