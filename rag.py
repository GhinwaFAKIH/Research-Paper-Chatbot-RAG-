from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# -----------------------------
# Embeddings
# -----------------------------

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


# -----------------------------
# Create vector store
# -----------------------------

def create_vectorstore(chunks):

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./vectorstore"
    )

    return vectorstore


# -----------------------------
# Load vector store
# -----------------------------

def load_vectorstore():

    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory="./vectorstore",
        embedding_function=embeddings
    )

    return vectorstore


# -----------------------------
# Local LLM
# -----------------------------

def get_llm():

    return ChatOpenAI(
        model="qwen2.5-3b-instruct",
        base_url="http://localhost:8080/v1",
        api_key="not-needed",
        temperature=0
    )


# -----------------------------
# Ask question
# -----------------------------

def ask_question(question):

    # Load vector database
    vectorstore = load_vectorstore()

    # Retrieve the 4 most relevant chunks
    documents = vectorstore.similarity_search(
        question,
        k=4
    )

    # DEBUG: display retrieved documents
    print("\n--- RETRIEVED DOCUMENTS ---")

    for i, document in enumerate(documents):
        print(f"\n--- Document {i + 1} ---")
        print(document.page_content[:1000])

    # Combine retrieved documents
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # Prompt
    prompt = ChatPromptTemplate.from_template(
        """
You are an assistant specialized in answering questions
about research papers.

Answer the question using ONLY the information provided
in the context below.

If the answer cannot be found in the context, say:
"I could not find the answer in the provided paper."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    # Local Qwen model through llama.cpp
    llm = get_llm()

    # Create chain
    chain = prompt | llm

    # Generate answer
    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content, documents
