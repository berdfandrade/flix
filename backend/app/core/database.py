from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from typing import cast
from pymongo.asynchronous.database import AsyncDatabase
from app.models.movie import Movie


async def init_db(uri: str, db_name: str):

    client = AsyncIOMotorClient(uri)

    db = client[db_name]

    await init_beanie(database=cast(AsyncDatabase, db))

    return client
