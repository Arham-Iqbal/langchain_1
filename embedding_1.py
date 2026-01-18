from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",dimensions=32)  #dimensions dont work in gemini
result=embedding.embed_query("delhi is capital of india")

# print(str(result))
print(len(result))