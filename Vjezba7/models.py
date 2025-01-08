from pydantic import BaseModel

class CreateProizvod(BaseModel):
    naziv:str
    cijena:float
class ResponseProizvod(CreateProizvod):
    id:int
    