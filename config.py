DOC_PATH = 'data/raw/'
CHROMA_PATH = 'data/chroma'

MODEL = 'gpt-3.5-turbo'

CHUNK_SIZE = 800
CHUNK_OVERLAP = 500

FILE_NAME = 'xLSTM_paper.pdf'
# FILE_NAME = 'AttentionIsAllYouNeed.pdf'

TEMPLATE = """Use ONLY the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, NEVER make up an answer.
Summarize in bullet point format. Keep the answer as concise as possible.
{context}
Question: {question}
Helpful Answer:"""
