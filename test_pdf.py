from utils import load_pdf, split_documents

pdf_path = "data/papers/paper.pdf"

documents = load_pdf(pdf_path)

print("Number of pages:", len(documents))

print("\nFirst page:")
print(documents[0].page_content[:1000])

chunks = split_documents(documents)

print("\nNumber of chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0].page_content[:500])
