from sqlalchemy.orm.scoping import ScopedSession
from sqlalchemy.sql.expression import delete, insert, select, update
from container import AppContainer, AppSetting
from model import Ticket, User
from databases.core import Database
from dependency_injector.wiring import Provide, inject
from sqlalchemy.exc import IntegrityError


@inject
async def main(
    database_conn: Database = Provide[AppContainer.database_conn],
):
    await database_conn.connect()

    q = """
    select u.id, u.name, t.name from users u 
    inner join tickets as t on t.user_id = u.id 
    """    
    [*found_user]  = await database_conn.fetch_all(query=q)
    print(found_user)

    await database_conn.disconnect()


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
