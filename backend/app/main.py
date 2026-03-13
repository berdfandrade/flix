from fastapi import FastAPI
from app.routes.health import router as health_router
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.core.config import settings, logger
from app.core.config import LogMessages as Log


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(Log.mongo_start)
    await init_db(uri=settings.mongo_url, db_name=settings.db_name)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(health_router)
