from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

chat_template = ChatPromptTemplate([
    SystemMessage(content="Ypu are a helpful {domain} expert"),
    
])