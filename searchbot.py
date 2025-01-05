import fitz
import os
from langchain_ollama import OllamaLLM



llm = OllamaLLM(model="llama3.2")



def extract_text_from_pdf(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    try:
        pdf_document = fitz.open(file_path)
    except fitz.FileDataError as e:
        raise Exception(f"Failed to open PDF file: {e}")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text

def Recieve_prompts(text):
    response = llm.invoke(text)
    return response


def process_pdf(question):
    file_path = "sample.txt"
    text = extract_text_from_pdf(file_path)
    context = f"Here is the content from the PDF:\n{text}\n\nNow, please answer the following question:\n{question}"
    answer = Recieve_prompts(context)
    return answer


def get_prompts(question):
    answer = process_pdf(question)
    return answer