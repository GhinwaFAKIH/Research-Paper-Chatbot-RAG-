from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOllama
from langchain_core.prompts import ChatPromptTemplate 

def create_vectorstore(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./vectorstore"
    )

    return vectorstore


def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory="./vectorstore",
        embedding_function=embeddings
    )

    return vectorstore

def ask_question(question):

    vectorstore = load_vectorstore()

    # Retrieve the 4 most relevant chunks
    documents = vectorstore.similarity_search(
        question,
        k=4
    )

    # Combine retrieved documents
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # Create the prompt
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

    # Create the LLM
    llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

    # Create the chain
    chain = prompt | llm

    # Generate answer
    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content, documents
