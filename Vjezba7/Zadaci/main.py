from fastapi import FastAPI
from models import ResponseFilmovi, CreateFilm

filmovi = [
{"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
{"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
{"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
{"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]



app=FastAPI()

@app.get("/filmovi", response_model=list[ResponseFilmovi])
def get_filmovi(genre:str=None, min_goodina:int=2000):
   if(genre):
      trazeni_filmovi = [film for film in filmovi if film["genre"]==genre and film["godina"]>=min_goodina]
   else:
      trazeni_filmovi = [film for film in filmovi if film["godina"]>=min_goodina]
   return trazeni_filmovi

@app.get("/filmovi/{id}", response_model=ResponseFilmovi)
def get_filmovi(id:int):
   trazeni_film = next((film for film in filmovi if film["id"]==id ),None )
   return trazeni_film

@app.post("/filmovi", response_model=ResponseFilmovi)
def post_film(film:CreateFilm):
    new_id=len(filmovi)+1
    film_sa_id=ResponseFilmovi(id=new_id, **film.model_dump())
    return film_sa_id
