from sqlalchemy.orm import Session
from . import models
from.models import MovieCreate

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie: MovieCreate):
    new_movie = models.Movie(
        title=movie.title,  # Update this to use 'title'
        description=movie.description,
        genre=movie.genre,
        rating=movie.rating,
        owner_id=movie.user_id  # Correct field name here too
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

def create_user(db: Session, username: str, password: str):
    hashed_password = models.hash_password(password)
    db_user = models.User(username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def recommend_movies(db: Session, user_id: int):

    liked_movies = db.query(models.Movie).filter(models.Movie.owner_id == user_id).all()

    if not liked_movies:
        return None
    
    genres = [movie.genre for movie in liked_movies]

    recommend_movies = db.query(models.Movie).filter(models.Movie.genre.in_(genres)).all()

    return recommend_movies