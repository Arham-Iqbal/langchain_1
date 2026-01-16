from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chathistory=[

    SystemMessage(content="you are a history expert")

]
chathistory.append(HumanMessage(content="tell us about akbar in 5 words"))

response=model.invoke(chathistory)

chathistory.append(AIMessage(content=response.content))

print("ai message :",response.content)

chathistory.append(HumanMessage(content="what expert you are and what did i asked you aout akbar"))

response2=model.invoke(chathistory)

chathistory.append(AIMessage(content=response2.content))

print("ai again ", response2.content)
