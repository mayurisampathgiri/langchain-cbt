from pydantic import BaseModel

class ThoughtInput(BaseModel):
    text: str

class CBTResponse(BaseModel):
    advice: str