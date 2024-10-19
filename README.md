## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources
See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

1. what refactoring signs (code smells) suggest this refactoring?
- Answer: The refactoring signs is MiddleMan because the movie class serves as a middle man for the rental class 
which requires access to the price_code to determine rental pricing. By moving price_code to Rental, we eliminate unnecessary interactions with the Movie class, allowing Rental to directly use its own attributes for pricing decisions.
2. what design principle suggests this refactoring? Why?
- Answer: The design principle of this refactoring suggests Single Responsibility Principle (SRP) 
because each class should have one responsibility to deal. In this case, Movie should responsible
for holding movie-related data such as title and year. While rental should be responsible for rental behavior, including pricing
by moving price_code from movie into rental.

3. Write your answer in README.md, in a section named Rationale. Describe where you implement this method and the reasons for your choice. Include one or more of these design principles to justify your design and how it applies:
- Answer: I have implemented price_code_for_movie in PriceStrategy class because it does not violate the Single Responsibility Principle (SRP). In other words, This class has a clear responsibility to handle pricing strategies.
Implementing price_code_for_movie in PriceStrategy is good with SRP since Movie is handle about movie related data and rental is handle about pricing.

