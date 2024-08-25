from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFaceHub

def main():
    load_dotenv()
    st.set_page_config(page_title="PDF Q&A Assistant")

    # Sidebar
    st.sidebar.header("📄 PDF Q&A Assistant")
    st.sidebar.write("""
        **How It Works:**

        1. **Upload Your PDF**: Use the file uploader to select and upload your PDF document.
        2. **Processing**: The application extracts the text from your PDF and processes it.
        3. **Ask a Question**: Enter a question related to the content of your PDF. The application will search for relevant sections and provide an answer based on the document.

        This tool leverages language models to understand and answer questions about your uploaded PDF document.
    """)

    # Main content
    st.title("PDF Q&A Assistant")
    st.write("Upload your PDF and ask questions about its content below.")

    # Upload file
    pdf = st.file_uploader("📂 Upload your PDF", type="pdf", key="file_uploader")

    if pdf is not None:
        # Extract the text
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Create embeddings
        #embeddings = OpenAIEmbeddings()
        embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Show user input
        user_question = st.text_input("❓ Ask a question about your PDF:", key="text_input")
        if user_question:
            docs = knowledge_base.similarity_search(user_question, k=3)
            # st.write(docs)
            #llm = OpenAI()
            llm = HuggingFaceHub(
                repo_id="google/flan-t5-small",
                model_kwargs={"temperature":0.5, "max_length":512},
                task="text2text-generation"
            )

            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=user_question)
            if response:
                st.write("🗨️ **Answer:**")
                st.write(response)

if __name__ == '__main__':
    main()
