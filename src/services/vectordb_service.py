from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from config import CHROMA_PATH


class ChromaDB():

    vectorstore: Chroma = None

    # Singleton Class
    def __new__(cls, text_splits):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChromaDB, cls).__new__(cls)
        return cls.instance

    def __init__(self, text_splits):
        self.clean_db()
        self.create_chromadb(text_splits)

    def create_chromadb(self, text_splits):
        print(f'Creating a local embedding vector DB on directory {CHROMA_PATH}')

        self.embedding = OpenAIEmbeddings()
        self.vectorstore = Chroma.from_documents(
            documents=text_splits,
            embedding=self.embedding,
            persist_directory=CHROMA_PATH
        )
        print(f'DB created successfuly. Collection count: {self.vectorstore._collection.count()} \n')

    def clean_db(self):
        if (self.vectorstore is not None):
            print('Cleaning Chroma DB')
            self.vectorstore.delete_collection()

    def get_vectorstore(self) -> Chroma:
        return self.vectorstore
