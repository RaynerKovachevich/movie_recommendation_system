from sqlalchemy.orm import Session
from . import models

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie):
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie