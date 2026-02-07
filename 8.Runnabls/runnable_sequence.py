from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Expalin the following jokes - {text}',
    input_variables=['text']
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

chain = RunnableSequence(prompt1 , model  , parser , prompt2 , model , parser)

print(chain.invoke({'topic' : 'AI'}))


