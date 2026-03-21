from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document




# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

#step 2 : Initilize embedding model

embedding = HuggingFaceEmbeddings(
     model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# step3 : create chroma vector space

vectorStore = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    collection_name="my_collection"
)

retriever = vectorStore.as_retriever(search_kwargs={"k":2})

query = "What is Chroma used for?"

results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

# below method do sementic search which work like vector search but when we need different stat. to do serch it fails , thats why we use retriever that is just before this line


results = vectorStore.similarity_search(query, k=2)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)