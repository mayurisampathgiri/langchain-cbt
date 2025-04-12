from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt = PromptTemplate.from_template("""
You are a compassionate CBT therapist helping a client analyze their automatic thought.

Use the CBT framework: identify cognitive distortions (if any), challenge the thought, and offer a balanced reframe.

Thought: {user_input}

Respond like a therapist gently guiding the client.
""")

chain = prompt | llm

async def analyze_thought(text: str) -> str:
    print("📥 Inside analyze_thought with:", text)
    result = chain.invoke({"user_input": text})
    return result.content
