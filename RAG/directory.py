from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='RAG/PDF_Folder',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
# print(docs[33].metadata)

for document in docs:
    print(document.metadata)