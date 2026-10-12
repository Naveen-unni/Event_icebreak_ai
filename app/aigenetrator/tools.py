from langchain.tools import tool

@tool
def understanding_questions()->str:
    """Generate question to understand the situation and what type of environment so agent can understand and adapt to the situation and give direction
    
    Don Not Use:Do not use this tool to get the personal details of user like phone number,email,password and not ask question that against user personal things
    
    """

    return