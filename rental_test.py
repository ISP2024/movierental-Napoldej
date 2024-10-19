import unittest
from customer import Customer
from rental import Rental
from pricing import *

class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", 2024, ["Adventure"])
		self.regular_movie = Movie("Air", 2023, ["Adventure"])
		self.childrens_movie = Movie("Frozen", 2021, ["Children"])

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", 2023, ["Adventure"])
		self.assertEqual("Air", m.get_title())



	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 6)
		self.assertEqual(rental.get_price(), 8.0)
		rental = Rental(self.childrens_movie, 10)
		self.assertEqual(rental.get_price(), 12.0)


	def test_rental_points(self):
		rental = Rental(self.new_movie, 3)
		self.assertEqual(rental.rental_points(), 3)
		rental = Rental(self.regular_movie, 4)
		self.assertEqual(rental.rental_points(), 1)
		rental = Rental(self.childrens_movie, 6)
		self.assertEqual(rental.rental_points(), 1)
