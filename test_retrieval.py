from rag import load_vectorstore


# Load the existing vector database
vectorstore = load_vectorstore()


# Ask a question
question = "What is the main contribution of this paper?"


# Retrieve the most relevant chunks
results = vectorstore.similarity_search(
    question,
    k=4
)


print("\nQuestion:")
print(question)

print("\n" + "=" * 80)
print("RETRIEVED DOCUMENTS")
print("=" * 80)


for i, document in enumerate(results):

    print(f"\n--- Result {i + 1} ---")

    print("Page:", document.metadata.get("page"))

    print("\nContent:")
    print(document.page_content[:1000])
