import os
from dotenv import load_dotenv
from llama_index.llms.groq import Groq

load_dotenv()


class LLM:
    @staticmethod
    async def query(text):
        model = Groq(
            model="llama3-70b-8192", 
            api_key=os.getenv('GROQ_API_SECRET')
        )
        return model.complete(text)
    

    @staticmethod
    async def builder(text):
        model = Groq(
            model="llama3-70b-8192", 
            api_key=os.getenv('GROQ_API_SECRET')
        )
        return model.complete(text)
