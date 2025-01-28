from fastapi import APIRouter, HTTPException
from models.movies import Film

import json

with open('Film.JSON') as file:
    filmovi = json.load(file)
    

router=APIRouter(prefix="/movies")

@router.get("/", response_model=list[Film])
def get_all(min_year:str, max_year:str, min_rating:str, max_rating:str, type:str):
    return filmovi

@router.get("/{id}")
def get_all(id:str):
    for film in filmovi:
        if film["imdbID"]==id:
            return film
    raise HTTPException(status_code=404, detail="Movie not found")

@router.get("/title/{title}")
def get_all(title:str):
    for film in filmovi:
        if film["Title"]==title:
            return film
    raise HTTPException(status_code=404, detail="Movie not found")


    