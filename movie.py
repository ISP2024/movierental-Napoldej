import logging
from abc import ABC, abstractmethod
class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    
    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code
        self.price_strategy = self.set_strategy(price_code)

    def set_strategy(self,price_code):
        if price_code == Movie.REGULAR:
            return RegularPrice()
        elif price_code == Movie.CHILDRENS:
            return ChildrensPrice()
        elif price_code == Movie.NEW_RELEASE:
            return NewRelease()

    def get_price(self, days):
        return self.price_strategy.get_price(days)


    def get_rental_points(self, days):
        return self.price_strategy.get_rental_points(days)

    def get_price_code(self):
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title



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



