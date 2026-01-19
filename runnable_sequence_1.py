from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1=PromptTemplate(
    template="write a joke about {joke}",
    input_variables=['joke']
)


prompt2=PromptTemplate(
    template="explain about the {text}",
    input_variables=['text']
)
parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({"joke":"ai"}))