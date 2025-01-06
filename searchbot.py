import fitz
import os
from langchain_ollama import OllamaLLM

#i downloaded an ollama model locally. you dont need to download , you can use the python module for it instead.
#check out ollama with python on google.
llm = OllamaLLM(model="llama3.2")


def extract_text_from_pdf(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    try:
        pdf_document = fitz.open(file_path)
    except fitz.FileDataError as e:
        raise Exception(f"Error opening PDF file: {e}")
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text



#sending prompt to LLM
def recieve_prompts(text):
    response = llm.invoke(text)
    return response


#process pdf and ask questions

def process_pdf(question):
    #this can be dynamically gotten, twek it to your needs!!! :)
    file_path = "sample.txt"
    text = extract_text_from_pdf(file_path)
    #context building
    context = f"Here is the content from the PDF:\n{text}\n\nNow, please answer the following question:\n{question}"
    #there are better way of doing this but lets go with this for a quick demo :)
    answer = recieve_prompts(context)
    return answer


#this is the main function that will be called from the assistant.py.
def get_prompts(question):
    response = process_pdf(question)
    return response

