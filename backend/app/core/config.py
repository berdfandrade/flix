from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import logging

BASE_DIR = Path(__file__).parent.parent
logger = logging.getLogger("uvicorn.error")


class LogMessages:
    mongo_start: str = "Starting [MongoDB] 🍃"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    mongo_url: str = "mongodb://localhost:27017"
    db_name: str = "flix"
    domain: str = "http://localhost:8000"
    bucket: str = "my-bucket"
    region: str = "us-east-1"


settings = Settings()
