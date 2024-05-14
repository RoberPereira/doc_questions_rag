from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import (TokenTextSplitter,
                                     RecursiveCharacterTextSplitter,
                                     CharacterTextSplitter)
from typing import List
from config import DOC_PATH, FILE_NAME


def load_pdf(file_name=FILE_NAME, doc_path=DOC_PATH):
    print(f'Loading file {file_name} ...')
    loader = PyPDFLoader(doc_path+file_name)
    pages = loader.load()

    print(f'File load correctly. Contains {len(pages)} pages')
    return pages


def split_document(pages, chunk_size=500, chunk_overlap=200, strategy='recursive') -> List[str]:

    print(f'Document spliting. Chunk size {chunk_size} - Chunk overlap {chunk_overlap} - Strategy {strategy}')

    if (strategy == 'recursive'):
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    elif (strategy == 'character'):
        splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    else:
        splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    text_splits = splitter.split_documents(pages)
    print(f'Splits generated {len(text_splits)}')
    return text_splits
