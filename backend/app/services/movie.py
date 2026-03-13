from typing import List
from beanie import PydanticObjectId
from app.models.movie import Movie
from app.schemas.movie import MovieUpdate, MovieCreate


class MovieService:

    async def create_movie(self, data: MovieCreate) -> Movie:
        movie = Movie(**data.model_dump())
        await movie.insert()
        return movie

    async def get_movie(self, movie_id: PydanticObjectId) -> Movie | None:
        return await Movie.get(movie_id)

    async def list_movies(
        self,
        skip: int = 0,
        limit: int = 20,
    ) -> List[Movie]:

        return await Movie.find_all().skip(skip).limit(limit).to_list()

    async def update_movie(
        self,
        movie_id: PydanticObjectId,
        data: MovieUpdate,
    ) -> Movie | None:

        movie = await Movie.get(movie_id)

        if not movie:
            return None

        update_data = data.model_dump(exclude_unset=True)

        await movie.set(update_data)

        return movie

    async def delete_movie(self, movie_id: PydanticObjectId) -> bool:

        movie = await Movie.get(movie_id)

        if not movie:
            return False

        await movie.delete()

        return True
