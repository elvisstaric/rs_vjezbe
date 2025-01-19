from fastapi import FastAPI

from datetime import datetime
from models import CreateProizvod, ResponseProizvod

proizvodi=[{"id":1, "naziv":"Miš", "cijena":100},{"id":2, "naziv":"Tipkovnica", "cijena":200}]

app=FastAPI()

@app.post("/proizvod", response_model=ResponseProizvod)
def post_proizvodi(proizvod:CreateProizvod):
    new_id=len(proizvodi)+1
    proizvod_sa_id: ResponseProizvod={"id":new_id, **proizvod.model_dump()}
    print(type(proizvod_sa_id))
    proizvodi.append(proizvod_sa_id)
    return proizvod_sa_id

