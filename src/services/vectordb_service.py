from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import shutil
import os

from config import CHROMA_PATH


class ChromaDB():
    instance = None
    vectorstore: Chroma = None

    # Singleton Class
    def __new__(cls, text_splits):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.clean_db()
            cls.instance.create_empty_directory()
            cls.instance.create_chromadb(text_splits)
        return cls.instance

    def create_chromadb(self, text_splits):
        print(f'Creating a local embedding vector DB on directory {CHROMA_PATH}')

        self.embedding = OpenAIEmbeddings()
        self.vectorstore = Chroma.from_documents(
            documents=text_splits,
            embedding=self.embedding,
            persist_directory=CHROMA_PATH
        )
        print(f'DB created successfuly. Collection count: {self.vectorstore._collection.count()} \n')

    def create_empty_directory(self):
        if not os.path.exists(CHROMA_PATH):
            os.makedirs(CHROMA_PATH)

    def clean_db(self):
        if (self.vectorstore is not None):
            print('Cleaning Chroma DB')
            self.vectorstore.delete_collection()
        self.remove_directory()

    def remove_directory(self):
        if os.path.exists(CHROMA_PATH):
            shutil.rmtree(CHROMA_PATH)
            print(f"Directory '{CHROMA_PATH}' removed successfully.")
        else:
            print(f"Directory '{CHROMA_PATH}' does not exist.")

    def get_vectorstore(self) -> Chroma:
        return self.vectorstore
