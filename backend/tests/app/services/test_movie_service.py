import pytest
from app.services.movie import MovieService
from app.schemas.movie import MovieCreate, MovieUpdate
from app.models.movie import Movie


@pytest.mark.asyncio
async def test_movie_service(test_db):

    service = MovieService()

    movie = await service.create_movie(
        MovieCreate(
            title="Interstellar",
            director="Christopher Nolan",
            year=2014,
        )
    )

    assert movie.id is not None
    assert movie.title == "Interstellar"

    found = await service.get_movie(movie.id)

    assert found is not None
    assert found.id == movie.id

    movies = await service.list_movies()

    assert len(movies) == 1

    updated = await service.update_movie(
        movie.id, MovieUpdate(title="Interstellar Updated")
    )

    assert updated is not None
    assert updated.title == "Interstellar Updated"

    result = await service.delete_movie(movie.id)

    assert result is True

    deleted = await Movie.get(movie.id)

    assert deleted is None
