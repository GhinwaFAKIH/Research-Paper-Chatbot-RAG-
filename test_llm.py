from dotenv import load_dotenv
from rag import ask_question


# Load environment variables
load_dotenv()


question = "What is the main contribution of this paper?"


print("Question:")
print(question)

print("\nGenerating answer...\n")


answer, documents = ask_question(question)


print("=" * 80)
print("ANSWER")
print("=" * 80)

print(answer)


print("\n")
print("=" * 80)
print("SOURCES")
print("=" * 80)


for i, document in enumerate(documents):

    page = document.metadata.get("page")

    print(f"Source {i + 1} - Page: {page}")
