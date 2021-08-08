import sqlalchemy
from model import metadata, users
from databases import Database


async def main():
    uri = "sqlite:///./mem.db"
    engine = sqlalchemy.create_engine(uri)
    metadata.create_all(bind=engine)

    database = Database(uri)
    await database.connect()

    query = users.insert()
    values = {"id": "test", "name": "humphrey"}
    await database.execute(query=query, values=values)


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
