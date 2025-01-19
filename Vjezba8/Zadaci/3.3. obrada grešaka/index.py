from fastapi import FastAPI, HTTPException, Query
from models import BaseCar, AutomobilResponse

automobili=[
    {"id":1, "marka":"VW", "model":"Golf", "godina_proizvodnje":2020, "cijena":30000.00, "boja":"crna"}
]

app=FastAPI()

@app.get("/automobil/{id}", response_model=BaseCar)
def get_automobil(id:int, max_cijena:float, max_godina:int, min_cijena:float=Query(gt=0),  min_godina:int=Query(gt=1960)):
    if min_cijena>max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena veća od maksimalne")
    elif min_godina>max_godina:
        raise HTTPException(status_code=400, detail="Minimalna godina veća od maksimalne")
    for auto in automobili:
        if auto["id"]==id and auto["cijena"]>=min_cijena and auto["cijena"]<=max_cijena and auto["godina_proizvodnje"]>=min_godina and auto["godina_proizvodnje"]<=max_godina:
            return auto
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")


@app.post("/automobil", response_model=AutomobilResponse)
def post_automobil(noviAutomobil:BaseCar):
    podaci=noviAutomobil.model_dump()
    for auto in automobili:
        if auto["marka"]==podaci["marka"] and auto["model"]==podaci["model"] and auto["godina_proizvodnje"]==podaci["godina_proizvodnje"] and auto["cijena"]==podaci["cijena"] and auto["boja"]==podaci["boja"]:
            raise HTTPException(status_code=400, detail="Automobil već postoji u bazi!")
    auto_id_pdv:AutomobilResponse={"id":len(automobili)+1, "cijena_pdv":podaci["cijena"]*1.25, **noviAutomobil.model_dump()}
    automobili.append(auto_id_pdv)  
    return auto_id_pdv