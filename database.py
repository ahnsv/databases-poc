import logging
from typing import Callable, ContextManager
from sqlalchemy import orm
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from contextlib import AbstractContextManager, contextmanager

Base = declarative_base()
logger = logging.getLogger(__name__)


class SqlAlchemyDatabase:
    def __init__(self, engine: Engine) -> None:
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=engine,
            ),
        )

    def create_database(self, engine: Engine) -> None:
        Base.metadata.create_all(engine)

    @contextmanager
    def session(self) -> Callable[..., ContextManager[orm.Session]]:
        session: orm.Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
