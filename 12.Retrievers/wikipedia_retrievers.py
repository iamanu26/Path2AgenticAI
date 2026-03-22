from langchain_community.retrievers import WikipediaRetriever

# Initialize the retriever (optional: set language and top_k)
retriever = WikipediaRetriever(top_k_results=2 , lang="en")

#Define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

#get relevent ocumnt from wikipdia

docs = retriever.invoke(query)

print(docs)