from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")


chatHistory=[
    SystemMessage(content="You are a helpful ai assistant")
]

while True:
    user_input=input("You :   ")
    chatHistory.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    else:
        result=model.invoke(chatHistory)
        chatHistory.append(AIMessage(content=result.content))
        print("ai :",result.content)

print("chat history is ", chatHistory)


    
