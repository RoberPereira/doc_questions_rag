
def pretty_print_docs(docs):
    print(f"\n{'-' * 100}\n".join([f"Document {i+1} page {d.metadata['page']} from {d.metadata['source']}:\n\n" + d.page_content for i, d in enumerate(docs)]))
