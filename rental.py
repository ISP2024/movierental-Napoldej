import logging
from movie import Movie
from pricing import *

class Rental:
   """
   A rental of a movie by customer.
   From Fowler's refactoring example.

   A realistic Rental would have fields for the dates
   that the movie was rented and returned, from which the
   rental period is calculated.
   For simplicity of this application only days_rented is recorded.
   """
   REGULAR = RegularPrice()
   NEW_RELEASE = NewRelease()
   CHILDRENS = ChildrensPrice()

   def __init__(self, movie, days_rented, price_code):
      """
      Initialize a new movie rental object for
      a movie with known rental period (daysRented).
      """
      self.movie = movie
      self.days_rented = days_rented
      self.price_strategy = price_code

   def get_price(self):
        return self.price_strategy.get_price(self.days_rented)

   def rental_points(self):
       return self.price_strategy.get_rental_points(self.days_rented)

   def get_price_code(self):
      return self.price_strategy

   def get_movie(self):
      return self.movie

   def get_days_rented(self):
      return self.days_rented
