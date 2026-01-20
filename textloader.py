from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()


prompt1=PromptTemplate(
    template="write summary of the poem {poem}",
    input_variables=['poem']

)


loader=TextLoader("cricket.txt",encoding="utf-8")
docs=loader.load()
chain=prompt1|model|parser

print(chain.invoke({"poem":docs[0]}))