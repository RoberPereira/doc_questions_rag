DOC_PATH = 'data/raw/'
CHROMA_PATH = 'data/chroma'

MODEL = 'gpt-3.5-turbo'

CHUNK_SIZE = 800
CHUNK_OVERLAP = 400

# FILE_NAME = 'xLSTM_paper.pdf'
# FILE_NAME = 'AttentionIsAllYouNeed.pdf'
FILE_NAME = 'VIT.pdf'

TEMPLATE = """USE ONLY the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, NEVER MAKE UP AN ANSWER or 
give opinions out side the context.
Summarize in bullet point format. Keep the answer as concise as possible.
{context}
Question: {question}
Helpful Answer:"""
