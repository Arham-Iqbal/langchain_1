from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"

)

result = model.invoke("What is the capital of India?")
result2=model.invoke("what is ai answer in 10 words")

print(result.content)
print(result2.content)



