from beanie import Document
from pydantic import Field
from datetime import datetime, timezone
from pymongo import IndexModel


class Movie(Document):

    title: str = Field(max_length=200)
    director: str = Field(max_length=120)

    year: int = Field(ge=2013)

    synopsis: str | None = Field(default=None, max_length=2000)

    poster_url: str | None = None
    video_url: str | None = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    updated_at: datetime | None = None

    class Settings:
        name = "movies"
        indexes = [
            IndexModel([("title", 1)]),
            IndexModel([("year", -1)]),
        ]
