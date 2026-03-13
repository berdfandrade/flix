from pydantic import BaseModel


class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None
    synopsis: str | None = None
    poster_url: str | None = None
    video_url: str | None = None
