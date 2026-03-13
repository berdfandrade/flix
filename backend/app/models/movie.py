from beanie import Document
from pydantic import Field
from datetime import datetime, timezone


class Movie(Document):
    title: str
    director: str
    year: int
    synopsis: str | None = None

    poster_url: str | None = None
    video_url: str | None = None

    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "movies"
