from langchain_community.document_loaders import TextLoader
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

prompt = PromptTemplate(
    template='Write the summry about the {poem}',
    input_variables=['poem']
)


loader = TextLoader( r"C:\Users\HP\OneDrive\Desktop\LangChain\9.Document_Loaders\cricket.txt")

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))