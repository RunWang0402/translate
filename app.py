import streamlit as st
import translator4 as translator
from PyPDF2 import PdfReader


User_API = st.text_input (label = "API KEY")
if User_API is not None:
    translator.set_API(User_API)

file_name = ""

uploaded_file = st.file_uploader(label= "To Translate", accept_multiple_files=False, type='pdf')


if uploaded_file is not None:
    file_name = uploaded_file.name
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    translation = translator.compiler(text)
    

#---------------------------------------Export Buttom---------------------------------#    

export_as_pdf = st.button("Translate")    #the buttom

if export_as_pdf:
    html = translator.create_PDF(translation)
    st.markdown(html, unsafe_allow_html=True)