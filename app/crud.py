from sqlalchemy.orm import Session
from . import models

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie, user_id:int):
    movie.owner_id = user_id
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def create_user(db: Session, username: str, password: str):
    hashed_password = models.hash_password(password)
    db_user = models.User(username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User). filter(models.User.username == username). first()

def recommend_movies(db: Session, user_id: int):
    liked_movies = db.query(models.Movie).filter(models.Movie.owner_id == user_id).all()
    genres = [movie.genre for movie in liked_movies]