from pydantic import BaseModel
from datetime import datetime
from typing import Literal, TypedDict

#1.zadatak

class Izdavac(BaseModel):
    naziv:str
    adresa:str

class Knjiga(BaseModel):
    naslov:str
    ime_autora:str
    prezime_autora:str
    godina_izdavanja:int = datetime.now().year
    broj_stranica:int
    izdavac:Izdavac

#2.zadatak

class Admin(BaseModel):
    ime:str
    prezime:str
    korisnicko_ime:str
    email:str
    ovlasti:Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"] = []

#3.zadatak

class stol(TypedDict):
    broj:int
    lokacija:int

class RestaurantOrder(BaseModel):
    id:int
    ime_kupca:str
    stol_info:stol
    lista_jela:list
    ukupna_cijena:float


#4.zadatak

class CCTV_frame(BaseModel):
    id:int
    vrijeme_snimanja:datetime
    koordinate:tuple[float, float]=(0.0,0.0)