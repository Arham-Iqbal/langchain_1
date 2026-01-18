from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]


query="tell me about kohli"

doc_embed=embedding.embed_documents(documents)
query_embed=embedding.embed_query(query)

scores = cosine_similarity([query_embed], doc_embed)[0]

best_index = scores.argmax()
best_score = scores[best_index]

print(query)
print(documents[best_index])
print("similarity score is:", best_score)
