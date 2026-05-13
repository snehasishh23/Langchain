import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model =  ChatGroq(
    model="llama-3.1-8b-instant"
)

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='''
Generate the name, age and city of a fictional {place} person.

Return ONLY valid JSON.
Do not include explanation, markdown, or code.

{format_instructions}
''',
    input_variables=['place'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

chain = template | model | parser

final_result = chain.invoke({'place':'indian'})

print(final_result)