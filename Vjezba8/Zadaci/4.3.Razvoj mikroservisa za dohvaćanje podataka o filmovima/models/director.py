from pydantic import BaseModel

class Director(BaseModel):
    name:str
    surname:str