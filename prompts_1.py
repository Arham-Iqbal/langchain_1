from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chattemplate=ChatPromptTemplate(
[
    ("system","you are a helpful {domain} expert"),
    ("human","explain in easy terms the {topic}")
])

prompt=chattemplate.invoke({"domain":"cricket","topic":"spin"})
print(prompt)
result=model.invoke(prompt)
print(result.content)