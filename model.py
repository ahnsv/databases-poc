import sqlalchemy
from sqlalchemy.orm import mapper

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column(
        "name",
        sqlalchemy.String,
    ),
    sqlalchemy.Column(
        "email",
        sqlalchemy.String,
    ),
    sqlalchemy.Column(
        "password",
        sqlalchemy.String,
    ),
)


class User:
    id: str
    name: str
    email: str
    password: str

mapper(User, users)