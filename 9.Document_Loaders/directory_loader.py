from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

loader = DirectoryLoader(
    path= r"C:\Users\HP\OneDrive\Desktop\SIH MAIN WORKING - Copy",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()
# when we have large number of document to load then we use lazy load; 
docs = loader.lazy_load()

# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)

for document in docs:
    print(document.metadata)