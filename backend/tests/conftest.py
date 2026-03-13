import pytest
import pytest_asyncio
from testcontainers.mongodb import MongoDbContainer
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.movie import Movie


@pytest.fixture(scope="session")
def mongo_container():
    container = MongoDbContainer("mongo:7")
    container.start()
    yield container
    container.stop()


@pytest_asyncio.fixture
async def test_db(mongo_container):
    uri = mongo_container.get_connection_url()
    client = AsyncIOMotorClient(uri)
    db = client["test_db"]
    await init_beanie(database=db, document_models=[Movie])  # type: ignore
    return db
