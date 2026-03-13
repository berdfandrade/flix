from beanie import Document
from pydantic import EmailStr
from datetime import datetime, timezone
from pydantic import Field


class User(Document):
    name: str
    email: EmailStr
    password_hash: str

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "users"
        indexes = ["email"]
