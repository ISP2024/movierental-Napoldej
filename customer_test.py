import re
import unittest 
from customer import Customer
from rental import Rental
from pricing import *

class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class """

	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", 2024, ["Adventure"])
		self.regular_movie = Movie("CitizenFour", 2022, ["Adventure"])
		self.childrens_movie = Movie("Frozen", 2021, ["Children"])
    	

	def test_billing(self):
		# no convenient way to test billing since its buried in the statement() method.
		self.c.add_rental(Rental(self.new_movie,4))
		self.c.add_rental(Rental(self.childrens_movie,6))
		self.c.add_rental(Rental(self.regular_movie, 7))
		total = self.c.total_charge()
		self.assertEqual(total, 27.5)

	def test_rental_points(self):
		self.c.add_rental(Rental(self.new_movie, 4))
		self.c.add_rental(Rental(self.childrens_movie, 5))
		self.c.add_rental(Rental(self.regular_movie, 10))
		total_points = self.c.total_rental_points()
		self.assertEqual(total_points, 6)
	
	def test_statement(self):
		stmt = self.c.statement()
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
