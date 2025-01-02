import os
import gc
import tempfile
import uuid
import pdfplumber
import streamlit as st

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core import PromptTemplate
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.readers.docling import DoclingReader
from llama_index.core.node_parser import MarkdownNodeParser

if "session_id" not in st.session_state:
    st.session_state.session_id = uuid.uuid4()
    st.session_state.doc_cache = {}

user_session_id = st.session_state.session_id
llm_client = None

@st.cache_resource
def initialize_llm():
    initialized_llm = Ollama(model="llama3.2", request_timeout=120.0)
    return initialized_llm

def clear_chat_history():
    st.session_state.chat_messages = []
    st.session_state.chat_context = None
    gc.collect()

def show_pdf_preview(uploaded_file):
    st.markdown("### PDF Preview")
    with pdfplumber.open(uploaded_file) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        st.write(text)
