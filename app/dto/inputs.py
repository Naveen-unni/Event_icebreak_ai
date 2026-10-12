from pydantic import BaseModel

class User(BaseModel):
   question:str 

class Answer(BaseModel):
   ans:str