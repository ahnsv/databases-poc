from contextlib import asynccontextmanager

from dependency_injector.wiring import Provide, inject

from container import AppContainer, AppSetting
from databases.core import Database
from sql import SqlFile


@asynccontextmanager
async def async_session(conn: Database):
    try:
        yield await conn.connect()
    finally:
        await conn.disconnect()


@inject
async def main(
    database_conn: Database = Provide[AppContainer.database_conn],
):
    async with async_session(conn=database_conn):
        with open(SqlFile.ALL_USERS_INNER_JOINED) as sql:
            [*found_user] = await database_conn.fetch_all(
                query=sql.read(), values={"id": "0004"}
            )
        print(found_user)


if __name__ == "__main__":
    import asyncio
    import sys

    app_container = AppContainer()
    app_container.config.from_pydantic(AppSetting())
    app_container.wire([sys.modules[__name__]])
    db = app_container.sqlalchemy_db()
    db.create_database(app_container.engine())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
