from pricing import RegularPrice, NewRelease, ChildrensPrice

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


