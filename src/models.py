import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from eralchemy2 import render_er
from typing import List

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
  
    favorite: Mapped[List["Favorite"]] = relationship()

class Favorite(Base):
    __tablename__ = 'favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('user.id'))
    people_id : Mapped[int] = mapped_column(ForeignKey('people.id'))
    planets_id : Mapped[int] = mapped_column(ForeignKey('planets.id'))
    starships_id: Mapped[int] = mapped_column(ForeignKey('starships.id'))
   

class People(Base):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    gender : Mapped[str] = mapped_column(nullable=False)
    eye_color : Mapped[str] = mapped_column(nullable=False)
    skin_color : Mapped[str] = mapped_column(nullable=False)
    favorite: Mapped[List["Favorite"]] = relationship()

class Planets(Base):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    papulation: Mapped[str] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    favorite: Mapped[List["Favorite"]] = relationship()


class Starships(Base):
    __tablename__ = 'starships'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    passanger: Mapped[str] = mapped_column(nullable=False)
    cargo_capacity: Mapped[str] = mapped_column(nullable=False)
    favorite: Mapped[List["Favorite"]] = relationship()

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')