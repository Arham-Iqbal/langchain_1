from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv


load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

documents=[
     "Inception is a sci-fi movie about dreams within dreams and mind-bending reality.",
    "Titanic is a romantic movie about love and tragedy on a sinking ship.",
    "Avengers is a superhero movie where heroes unite to save the world.",
    "Interstellar is a science fiction movie about space travel and time dilation.",
    "Joker is a psychological drama about the origin of a troubled villain."
]
# query="movie about space and time"
query=input("enter your query:  ")

doc_embed=embedding.embed_documents(documents)
query_embed=embedding.embed_query(query)

scores=cosine_similarity([query_embed],doc_embed)[0]

best_index=scores.argmax()
best_score=scores[best_index]

print(documents[best_index])
print("similarity is : ", best_score)

