from typing import Collection, List
from dataclasses import dataclass

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

    def __str__(self) -> str:
        """
        Return a string representation of the Movie in the format "Title (year)".
        """
        return f"{self.title} ({self.year})"