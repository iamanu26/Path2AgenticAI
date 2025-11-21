from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv

model = ChatOpenAI(model='gpt-4', temperature=1.5 , max_completion_tokens=10 )
# temprature vary from 0-2 and it is use for the creative output , 0 is for simple


result = model.invoke("What is the capital of India?")

print(result.content)