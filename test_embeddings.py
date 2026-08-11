from utils import load_pdf, split_documents
from rag import create_vectorstore


pdf_path = "data/papers/paper.pdf"

print("Loading PDF...")

documents = load_pdf(pdf_path)

print(f"Pages loaded: {len(documents)}")

print("Splitting document...")

chunks = split_documents(documents)

print(f"Chunks created: {len(chunks)}")

print("Creating embeddings and vector database...")

vectorstore = create_vectorstore(chunks)

print("Vector database created successfully!")
