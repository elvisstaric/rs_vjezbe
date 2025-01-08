from fastapi import FastAPI
from models import CreateProizvod, ResponseProizvod

proizvodi=[{"id":1, "naziv":"Miš", "cijena":100},{"id":2, "naziv":"Tipkovnica", "cijena":200}]



app=FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello"}

@app.get("/proizvod/{proizvod_id}")
def get_proizvodi(proizvod_id:int, min_cijena:float):
    trazeni_proizvod = next((proizvod for proizvod in proizvodi if proizvod["id"]==proizvod_id and proizvod["cijena"]>=min_cijena),None )
    return {"trazeni_proizvod":trazeni_proizvod}

@app.post("/proizvod", response_model=ResponseProizvod)
def post_proizvodi(proizvod:CreateProizvod):
    new_id=len(proizvodi)+1
    proizvod_sa_id=ResponseProizvod(id=new_id, **proizvod.model_dump())
    return ({"status":proizvod_sa_id})
