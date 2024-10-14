from abc import ABC, abstractmethod



class PriceStrategy(ABC):
    _instance = None

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

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = RegularPrice()
    NEW_RELEASE = NewRelease()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        self.price_strategy = price_code


    def get_price(self, days):
        return self.price_strategy.get_price(days)


    def get_rental_points(self, days):
        return self.price_strategy.get_rental_points(days)


    def get_title(self):
        return self.title

    def __str__(self):
        return self.title


