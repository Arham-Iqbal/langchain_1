from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")


template1=PromptTemplate(
    template="write a detail eassay about {topic}",
    input_variables=["topic"]
)


template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. \n {text}',
    input_variables=['text']
)


parser=StrOutputParser()

prompt1=template1.format(topic="black hole")

response1=model.invoke(prompt1)

prompt2=template2.format(text=response1.content)

response2=model.invoke(prompt2)

print("summary is ",response2.content)


