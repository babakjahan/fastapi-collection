from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str
    year: int
    storyline: str | None  # Field(default=None, max_length=200,)


class ConvertItem:
    @staticmethod
    def make_dict_movie(movie: tuple) -> dict:
        time_keys = ("id_movies", "title", "year", "storyline")
        return dict((x, y) for x, y in zip(time_keys, movie))
