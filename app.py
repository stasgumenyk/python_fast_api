from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import uvicorn

app = FastAPI()

class EditMovie(BaseModel):
    title: str
    description: str
    yearOfRelease: str

class CreateMovie(BaseModel):
    title: str
    description: str
    yearOfRelease: str

class Movie(BaseModel):
    id: int
    title: str
    description: str
    yearOfRelease: str

movies = [
    {
        'id': 1,
        'title': 'Once upon a time in Hollywood...',
        'description': 'Brand new movie by Quentin Tarantino',
        'yearOfRelease': '2019'
    },
    {
        'id': 2,
        'title': 'The Witcher',
        'description': 'Netflix original series based on a series of novel by Andrzej Sapkovsky',
        'yearOfRelease': '2019'
    }
]

movies_list: List[Movie] = movies

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/movies", response_model=List[Movie])
def read_movies():
    return movies_list

@app.get("/movies/{id}", response_model=Movie)
def save_movie(id: int):
    movie = list(filter(lambda t: t['id'] == id, movies))[0]
    return movie

@app.post("/movies", response_model=Movie, status_code=201)
def create_movie(t: CreateMovie):
    movie = {
        'id': movies[-1]['id'] + 1,
        'title': t.title,
        'description': t.description,
        'yearOfRelease': t.yearOfRelease
    }
    movies.append(movie)
    return movie

@app.put("/movies/{id}", response_model=Movie)
def edit_movie(id: int, t: EditMovie):
    edited_movie = {
        'id': id,
        'title': t.title,
        'description': t.description,
        'yearOfRelease': t.yearOfRelease
    }
    return edited_movie

@app.delete("/movies/{id}", response_model=List[Movie], status_code=201)
def delete_movie(id: int):
    movie = list(filter(lambda t: t['id'] != id, movies))[0]
    return movie
