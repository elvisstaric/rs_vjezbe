from pydantic import BaseModel

class BaseCar(BaseModel):
    marka:str
    model:str
    godina_proizvodnje:int
    cijena:float
    boja:str

class AutomobilResponse(BaseCar):
    id:int
    cijena_pdv:float

