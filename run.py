from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.text_splitter import TokenTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from config import OPENAI_API_KEY
import pprint
import os
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


file_name = "data/raw/xLSTM_paper.pdf"
print(f'Loading file {file_name} ...')
loader = PyPDFLoader(file_name)
pages = loader.load()

print(f'File load correctly and contains {len(pages)} pages \n')


chunk_size = 400
chunk_overlap = 200
splitter_policy = 'recursive'
print(f'Document spliting. Chunk size {chunk_size} - Chunk overlap {chunk_overlap} - Policy {splitter_policy}')

if (splitter_policy == 'recursive'):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
elif (splitter_policy == 'character'):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
else:
    splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

split_texts = splitter.split_documents(pages)
print(f'Amount of splits generated {len(split_texts)} \n')


# !rm -R 'data/chroma/'  Check first if exist
persist_directory = 'data/chroma/'
print(f'Creating a local embedding vector DB on directory {persist_directory}')

embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(
    documents=split_texts,
    embedding=embedding,
    persist_directory=persist_directory
)

print(f'DB created successfuly. Collection count: {vectordb._collection.count()} \n')
