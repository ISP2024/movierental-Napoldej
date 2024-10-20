from typing import Collection, List
from dataclasses import dataclass
import csv
import logging

logger = logging.getLogger(__name__)
@dataclass(frozen= True)
class Movie:
    """
    A movie available for rent, with title, year, and genre.
    Immutable dataclass for Movie.
    """
    title : str
    year : int
    genre : Collection[str]

    def is_genre(self, genre_name: str) -> bool:
        """
        Check if the movie's genre matches the provided genre name.
        Case insensitive.
        """
        return genre_name.lower() in (g.lower() for g in self.genre)

    def get_title(self):
        return self.title

    def __str__(self) -> str:
        """
        Return a string representation of the Movie in the format "Title (year)".
        """
        return f"{self.title} ({self.year})"


class MovieCatalog:
    _instance = None
    _movies = []

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def get_movie(self, title: str, year=None):
        """Search for a movie by title and year while reading the file line by line."""
        with open("movies_data1.csv", mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            line_number = 0
            next(csv_reader)
            for row in csv_reader:
                line_number += 1
                try:
                    movie_title = row[1]
                    movie_year = int(row[2])
                    genres = row[3].split('|')

                    if movie_title == title and (year is None or movie_year == year):
                        return Movie(movie_title, movie_year, genres)

                except (ValueError, IndexError) as e:
                    logger.error(f"Line {line_number}: Unrecognized format \"{','.join(row)}\"")
                    continue
            return None









