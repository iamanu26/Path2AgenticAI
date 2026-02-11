from langchain_community.document_loaders import PyPDFLoader
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

loader = PyPDFLoader(r"C:\Users\HP\OneDrive\Desktop\LangChain\9.Document_Loaders\Project Overview.pdf")

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)