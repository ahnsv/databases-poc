from databases.core import Database
from dependency_injector.wiring import Provide, inject
from sqlalchemy.engine.base import Engine
from container import AppContainer, AppSetting
from model import metadata, users


@inject
async def main(
    engine: Engine = Provide[AppContainer.engine],
    database_conn: Database = Provide[AppContainer.database_conn],
):
    metadata.create_all(bind=engine)

    await database_conn.connect()

    query = users.insert()
    values = {"id": "test3", "name": "humphrey"}
    await database_conn.execute(query=query, values=values)


if __name__ == "__main__":
    import asyncio
    import sys

    container = AppContainer()
    container.config.from_pydantic(AppSetting())
    container.wire([sys.modules[__name__]])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
