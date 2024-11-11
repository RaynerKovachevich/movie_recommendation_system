from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud
from .database import sessionLocal, engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/movies/")
def create_movie(tittle: str, description: str, genre: str, rating: float, db: Session = Depends(get_db)):
    movie = models.Movie(tittle=tittle, description=description, genre=genre, rating=rating)
    return crud.create_movie(db=db, movie=movie)


@app.get("/movies/{movie_id}")
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie