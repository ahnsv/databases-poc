import sqlalchemy
import databases

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from pydantic import BaseSettings
from pydantic.fields import Field


class AppSetting(BaseSettings):
    db_uri: str = Field(default="sqlite:///./mem.db", env="db_uri")


class AppContainer(DeclarativeContainer):
    config = providers.Configuration()
    engine = providers.Singleton(sqlalchemy.create_engine, config.db_uri)
    database_conn = providers.Singleton(databases.Database, config.db_uri) 
