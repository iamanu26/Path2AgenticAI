import random

class Demo_LLM_Nakali:
    def __init__(self):
        print("LLM created")

    def predict(self , prompt):

        response_list = [
            'Delhi is the capital of India',
            'IPL is a criket league',
            'AI stand for Artificial Intelligence'
        ]

        return {'response' : random.choice(response_list)}
    
class Demo_prompt_templete:
    def __init__(self , template , input_variable):
        self.template = template
        self.input_variable = input_variable

    def format(self , input_dict):
        return self.template.format(**input_dict)
    
class DemoLLMchain:
    def __init__(self , llm , prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self , input_dict):
        final_prompt = self.prompt.format(input_dict)
        self.llm.predict(final_prompt)

template = Demo_prompt_templete(
    template='Write a poem about {topic}',
    input_variable=['topic']
)

prompt = template.format({'topic':'india'})

llm = Demo_LLM_Nakali()

chain = DemoLLMchain(llm , template)
chain.run({'topic' : 'india'})
