from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    tittle = Column(String, index=True)
    descreption = Column(String)
    genre = Column(String)
    rating = Column(Float)