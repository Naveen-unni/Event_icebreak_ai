import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm=ChatPromptTemplate(model="gemini-2.5-flash",temperature=0.7)

prompt = ChatPromptTemplate.from_template("""
You are an AI agent running a multiplayer game.

Here are ALL participants:

{participants}

Analyze the entire group.

Generate ONE personalized response for EVERY participant.

Rules:
- Every user must get exactly one response.
- Use their own answer.
- Compare their answer with other users.
- Create interesting connections.
- Give them a challenge.
- target_user_id should be another participant when relevant.
- Do not give everyone the same response.
""")

chain = prompt | llm

result = chain.invoke({
    
})

print(result)

