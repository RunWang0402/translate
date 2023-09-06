import os
from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from constants import APIKEY, p_English, count
from langchain import OpenAI
from fpdf import FPDF
import random
import string
import warnings
warnings.filterwarnings("ignore", message="cmap value too big/small")
import base64


#set up environment, source: https://www.youtube.com/watch?v=nAmC7SoVLd8
def set_API(user_API):
    os.environ['OPENAI_API_KEY'] = user_API
    llm = OpenAI(temperature = 0,max_tokens=3000)

#extract text from pdf, split text, source: https://www.youtube.com/watch?v=O5C0wfsen98
def extract_pdf(raw_docs):
    doc_loader = PyPDFLoader(raw_docs)
    extraction = doc_loader.load()
    docs = ""
    number = len(extraction)
    for i in range(number):
        docs += extraction[i].page_content
    return docs




def split_text_to_chunks(text, token_limit):
    """
    将文本切割为指定token数的块
    """
    words = text.split(".")
    chunks = []
    current_chunk = []

    current_length = 0
    for word in words:
        # 假设每个word是一个token，这是一个简化的处理
        if current_length + len(word) <= token_limit:
            current_length += len(word)
            current_chunk.append(word)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_length = len(word)

    # 添加剩余的部分
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


def translate(chunks):
    final = ""
    for i in range(len(chunks)):
        prompt = p_English+chunks[i]+"'"
        addition = llm(prompt=prompt).strip()
        final += addition
    return final



def create_PDF(text):
    pdf = FPDF()

    pdf.add_font("Chinese", style="", fname="ch2.ttf", uni=True)
    pdf.set_font("Chinese", size = 9)
    pdf.set_margins(25.4, 25.4, 25.4)
    
    pdf.add_page()
    pdf.write(9,text)
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "Translation")
    return html
    #pdf.output("translation" + "trial" +".pdf")  -Directly output a pdf

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


def compiler(text):
    chunks = split_text_to_chunks(text, 800)
    translation = translate(chunks)
    return translation
    
