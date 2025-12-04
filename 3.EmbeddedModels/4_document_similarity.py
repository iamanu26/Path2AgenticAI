from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
document = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

query = 'tell me about the delhi'

doc_embedding = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding] , doc_embedding)[0]

index , score = sorted(list(enumerate(score)),key = lambda x:x[1])[-1]
print(document[index])
print("similarity score is:" , score)