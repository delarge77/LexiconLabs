from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/movies/{movie_id}")
def get_movies_by_id(movie_id: int):
    return find_movie(movie_id)

@app.post("/movies/", status_code=201)
def add_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id":new_id, "title":movie.title, "director":movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie

@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)

@app.put("/movies/{movie_id}")
def update_movie(movie: Movie, movie_id: int):
    existing = find_movie(movie_id)
    existing["title"] = movie.title,
    existing["director"] = movie.director, 
    existing["year"] = movie.year
    return existing


