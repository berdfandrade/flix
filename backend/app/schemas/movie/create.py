from pydantic import BaseModel


class MovieCreate(BaseModel):
    title: str
    director: str
    year: int
    synopsis: str | None = None
    poster_url: str | None = None
    video_url: str | None = None
