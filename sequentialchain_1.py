from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(
    template="write a detail 100 words report on {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

prompt2=PromptTemplate(
    template="write  a summary of the report in 20 words {text}",
    input_variables=['text']
)

chain=prompt1|model|parser|prompt2|model|parser

print(chain.invoke({"topic":"football"}))
chain.get_graph().print_ascii()