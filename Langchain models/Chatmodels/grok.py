import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

result = model.invoke("who is dipak mazumdar in iitk")

print(result.content)