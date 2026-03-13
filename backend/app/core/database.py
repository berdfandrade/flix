from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from typing import cast
from pymongo.asynchronous.database import AsyncDatabase
from app.models import ALL_MODELS


async def init_db(uri: str, db_name: str):
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    await init_beanie(database=cast(AsyncDatabase, db), document_models=ALL_MODELS)
    return client
