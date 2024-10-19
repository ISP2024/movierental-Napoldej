import re
import unittest
from customer import Customer
from rental import Rental
from pricing import *

class PricingTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie("new_movie", 2024, ["Adventure"])
        self.children_movie = Movie("children_movie", 2021, ["Children"])
        self.regular_movie = Movie("regular_movie", 2022, ["Adventure"])

    def test_price_strategy(self):
        price_code = PriceStrategy.price_code_for_movie(self.new_movie)
        self.assertEqual(NewRelease(), price_code)
        price_code = PriceStrategy.price_code_for_movie(self.children_movie)
        self.assertEqual(ChildrensPrice(), price_code)
        price_code = PriceStrategy.price_code_for_movie(self.regular_movie)
        self.assertEqual(RegularPrice(),price_code)


