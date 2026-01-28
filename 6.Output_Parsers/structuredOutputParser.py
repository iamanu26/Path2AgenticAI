from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema



load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name='fact_1' , description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2' , description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3' , description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give three fact about {topic} \n {formate_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instruction()}
)

chain = template | model | parser

result = model.invoke({'topic':'black hole'})


print(result)