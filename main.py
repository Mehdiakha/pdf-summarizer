import os
import json
from dotenv import load_dotenv

from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_mistralai import ChatMistralAI

load_dotenv()

anthropic_key = os.getenv("ANTHROPIC_API_KEY")
mistral_key = os.getenv("MISTRAL_API_KEY")
langchain_key = os.getenv("LANGCHAIN_API_KEY")


def summarize_pdf(file_path):
    try:
        loader = PyPDFLoader(file_path)
        docs = loader.load_and_split()
        llm = ChatMistralAI(model="mistral-large-latest", temperature=0)
        chain = load_summarize_chain(llm, chain_type='map_reduce')
        summary = chain.invoke(docs)

        return summary
    except Exception as e:
        print(f"an error occured: {e}")
        return None


if __name__ == "__main__":
    summary = summarize_pdf('test.pdf')
    
    print('Summary:')
    print('\n')
    print(summary['output_text'])

