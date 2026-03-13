import pytest
import pytest_asyncio
from testcontainers.mongodb import MongoDbContainer
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import ALL_MODELS


@pytest.fixture(scope="session")
def mongo_container():
    container = MongoDbContainer("mongo:7")
    container.start()
    yield container
    container.stop()


@pytest_asyncio.fixture(scope="function")
async def test_db(mongo_container):
    uri = mongo_container.get_connection_url()
    client = AsyncIOMotorClient(uri)
    db = client["test_db"]
    await init_beanie(database=db, document_models=ALL_MODELS)  # type: ignore
    yield db
    await client.drop_database("test_db")
    client.close()
