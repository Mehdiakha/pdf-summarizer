📄 PDF Summarizer

🚀 Project Overview

PDF Summarizer is a Python-based tool that processes PDF files, extracts text, and generates concise summaries using AI-powered language models. It leverages LangChain for natural language processing.

✨ Features

📝 Extracts text from PDF files

🤖 Summarizes content using an LLM (GPT, Llama, or Mistral)

💾 Stores and retrieves summaries from a database (PostgreSQL)

🔍 Supports search functionality for quick retrieval

🌐 REST API for easy integration

## How to use it:

'''sh

git clone https://github.com/Mehdiakha/pdf-summarizer.git
cd pdf-summarizer

python -m venv .venv
source .venv/bin/activate # On Windows, use .venv\Scripts\activate
pip install -r requirements.txt

set up your mistralaikey
MISTRAL_API_KEY=your_mistral_api_key

place your pdf file inside the project and run the summarizer
python main.py

'''
