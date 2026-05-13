from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model =  ChatGroq(
    model="llama-3.1-8b-instant"
)


messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)