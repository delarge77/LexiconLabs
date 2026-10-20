from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY not found. Check your .env file.")

app = FastAPI()

def check_key(x_api_key: str | None = Header(default=None)):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

movies = [
    {"id": 1, "title": "The GodFather", "director": "Francis Ford Coppola", "year": 1972},
    {"id": 2, "title": "Neuromancer", "director": "William Gibson", "year": 1984},
    {"id": 3, "title": "The Hobbit", "director": "J.R.R. Tolkien", "year": 1937},
    {"id": 4, "title": "Foundation", "director": "Isaac Asimov", "year": 1951},
]

class Movie(BaseModel):
    title: str
    director: str
    year: int

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

def find_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie Not Found")

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    if director:
        return [movie for movie in movies if director.lower() in movie["director"].lower()]
    elif year:
        return [movie for movie in movies if year == movie["year"]]
    return movies

@app.get("/movies/{movie_id}", dependencies=[Depends(check_key)])
def get_movies_by_id(movie_id: int):
    return find_movie(movie_id)

@app.post("/movies/", status_code=201, dependencies=[Depends(check_key)])
def add_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id":new_id, "title":movie.title, "director":movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie

@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)

@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie: Movie, movie_id: int):
    existing = find_movie(movie_id)
    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year
    return existing

@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie_optionals(movie_id: int, new_movie: MovieUpdate):
    movie = find_movie(movie_id)
    movie.update(new_movie.model_dump(exclude_unset=True))
    return movie

