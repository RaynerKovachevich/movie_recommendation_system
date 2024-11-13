from fastapi import FastAPI, Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session
from . import models, crud
from .database import sessionLocal, engine, Base
from .models import MovieCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

       

@app.post("/movies/")
def create_movie(tittle: str, description: str, genre: str, rating: float, user_id: int, db: Session = Depends(get_db)):
    user_id = 1
    movie = models.Movie(tittle=tittle, description=description, genre=genre, rating=rating)
    return crud.create_movie(db=db, movie=movie, user_id=user_id)


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.post("/register")
def register_user(username: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username alredy taken")
    return crud.create_user(db, username, password)

@app.get("/movies/recommendations/{user_id}")
def get_recommendations(user_id: int, db: Session = Depends(get_db)):
    movies = crud.recommend_movies(db, user_id)
    if not movies:
        raise HTTPException(status_code=404, detail="No recommendations found")
    return movies