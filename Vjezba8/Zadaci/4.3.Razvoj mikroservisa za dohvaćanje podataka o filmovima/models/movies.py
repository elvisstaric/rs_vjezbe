from pydantic import BaseModel, Field
from typing import Literal, Optional

class Film(BaseModel):
    Title: str
    Year:str
    Rated:str
    Released: Optional[str]="Release date unknown"
    Runtime: str
    Genre: str
    Director:Optional[str]="Director unknown"
    Writer:str
    Actors:str
    Plot:str
    Language:str
    Country:str
    Awards:Optional[str]="Awards unknows"
    Poster:Optional[str]="Poster unavailable"
    Metascore:Optional[str]="0"
    imdbRating:Optional[str]
    imdbVotes:Optional[str]
    imdbId:Optional[str]="id unknown"
    Type:Optional[Literal["movie", "series"]]="type unknown"
    Response:Optional[bool]="Response unknown"
    Images:Optional[list[str]]="Images unavailable"