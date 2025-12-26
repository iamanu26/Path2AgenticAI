from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate , load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

messages = [
    SystemMessage(content="You are a helpful assistance"),
    HumanMessage(content="Tell me about langchain")
]
result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)