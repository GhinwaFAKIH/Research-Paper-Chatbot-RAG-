import os
import shutil
import streamlit as st

from utils import load_pdf, split_documents
from rag import create_vectorstore, ask_question


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Research Paper Chatbot",
    page_icon="📚",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("📚 Research Paper Chatbot")

st.write(
    "Upload a research paper and ask questions about its content."
)


# -----------------------------
# Upload PDF
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload your research paper",
    type=["pdf"]
)


# -----------------------------
# Process PDF
# -----------------------------

if uploaded_file is not None:

    os.makedirs("data/papers", exist_ok=True)

    pdf_path = os.path.join(
        "data/papers",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    if st.button("Process Paper"):

        with st.spinner("Processing paper..."):

            # Load PDF
            documents = load_pdf(pdf_path)

            # Split into chunks
            chunks = split_documents(documents)

            # Create vector database
            create_vectorstore(chunks)

        st.success(
            f"Paper processed successfully! "
            f"{len(chunks)} chunks created."
        )


# -----------------------------
# Ask questions
# -----------------------------

st.divider()

st.subheader("💬 Ask a question")

question = st.text_input(
    "Your question",
    placeholder="What is the main contribution of this paper?"
)


if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    elif not os.path.exists("vectorstore"):
        st.warning("Please upload and process a paper first.")

    else:

        with st.spinner("Searching the paper..."):

            answer, documents = ask_question(question)

        # -----------------------------
        # Answer
        # -----------------------------

        st.subheader("🤖 Answer")

        st.write(answer)

        # -----------------------------
        # Sources
        # -----------------------------

        st.subheader("📖 Sources")

        for i, document in enumerate(documents):

            page = document.metadata.get("page")

            if page is not None:
                page = page + 1

            with st.expander(
                f"Source {i + 1} — Page {page}"
            ):

                st.write(document.page_content)
