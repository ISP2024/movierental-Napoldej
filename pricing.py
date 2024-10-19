from abc import ABC, abstractmethod
from movie import Movie


class PriceStrategy(ABC):
    _instance = None

    @staticmethod
    def price_code_for_movie(movie : Movie):
        if movie.year == 2024:
            return NewRelease()
        elif any(genre.lower() in ["children", "childrens"] for genre in movie.genre):
            return ChildrensPrice()
        else:
            return RegularPrice()

    @abstractmethod
    def get_price(self, days: int) -> float:
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        pass

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

class NewRelease(PriceStrategy):

    def get_price(self, days: int) -> float:
        return 3 * days

    def get_rental_points(self, days: int) -> int:
        return days


class RegularPrice(PriceStrategy):

    def get_price(self, days: int) -> float:
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1


class ChildrensPrice(PriceStrategy):

    def get_price(self, days: int) -> float:
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1