# PDF Q&A Assistant

## Introduction

The PDF Q&A Assistant is a Python application that allows you to upload a PDF document and ask questions about its content using natural language. The app processes the PDF, extracts the text, and utilizes a language model to generate accurate responses to your queries. Please note that the app will only respond to questions related to the content of the uploaded PDF.

## How It Works

The application follows these steps to provide responses to your questions:

### 1. PDF Uploading:
The app allows you to upload a single PDF document. The content of the PDF is then extracted for processing.

### 2. Text Extraction:
The text is extracted from the uploaded PDF document using the `PyPDF2` library.

### 3. Text Chunking:
The extracted text is divided into smaller chunks to make it more manageable for processing.

### 4. Language Model:
The app utilizes a language model to generate vector representations (embeddings) of the text chunks using `HuggingFaceInstructEmbeddings`.

### 5. Similarity Matching:
When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones using FAISS.

### 6. Response Generation:
The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDF.

## Dependencies and Installation

To install the PDF Q&A Assistant, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an API key from Hugging Face and add it to the `.env` file in the project directory:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
   ```

## Usage

To use the PDF Q&A Assistant, follow these steps:

1. Ensure that you have installed the required dependencies and added the Hugging Face API key to the `.env` file.

2. Run the application using the Streamlit CLI. Execute the following command:
   ```bash
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Upload a PDF document into the app by following the provided instructions.

5. Ask questions in natural language about the loaded PDF using the provided text input.

## Contributing

This repository is intended for educational purposes and does not accept further contributions. 
