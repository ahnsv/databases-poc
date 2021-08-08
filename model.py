from database import Base
from typing import List
import sqlalchemy
from sqlalchemy.orm import backref, mapper, relationship


class Ticket(Base):
    __tablename__ = "tickets"
    id: str = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name: str = sqlalchemy.Column(sqlalchemy.String)
    user_id: str = sqlalchemy.Column(sqlalchemy.ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id: str = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name: str = sqlalchemy.Column(sqlalchemy.String)
    email: str = sqlalchemy.Column(sqlalchemy.String)
    password: str = sqlalchemy.Column(sqlalchemy.String)
    tickets: List[Ticket] = relationship("Ticket")
