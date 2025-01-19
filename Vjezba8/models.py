from pydantic import BaseModel
from typing import Literal, Optional, TypedDict

class CreateProizvod(BaseModel):
    naziv:str
    cijena:float
class ResponseProizvod(CreateProizvod):
    id:int
    
class snagaMotora(TypedDict):
    kW:int
    KS:int
    
class cijena(TypedDict):
    osnovna:int
    sa_pdv:int

class Automobil(BaseModel):
    id: int
    marka:str
    model:str
    boja: Literal["crvena", "plava"]
    godina:Optional[int]
    snaga:snagaMotora
    cijena:cijena