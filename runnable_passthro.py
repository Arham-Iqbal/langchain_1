from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser=StrOutputParser()

prompt1=PromptTemplate(
    template="write a joke on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="explain the joke {text}",
    input_variables=['text']
)

joke_gen=prompt1|model|parser

parallel_chain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "text":prompt2|model|parser
    }
)

merge_chain=joke_gen|parallel_chain
result=merge_chain.invoke({"topic":"phones"})

print(result)