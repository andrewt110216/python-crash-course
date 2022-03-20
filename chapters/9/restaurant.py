# Python Crash Course
# restaurant.py (Exercise 9-10)
# 03/14/2022
# Andrew Tracey

# Practice storing class definitions in a module for import.


"""A set of classes to represent Restaurants."""


class Restaurant():
	"""A simple respresentation of a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes of the Restaurant object."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Print the known information about the restaurant."""
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"The cusine type is {self.cuisine_type}.")

	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		print(f"{self.restaurant_name} is now open!")

	def set_number_served(self, n):
		"""Update the number of customers served."""
		self.number_served = n

	def increment_number_served(self, increment):
		"""Increment the number of customers served."""
		self.number_served += increment


class IceCreamStand(Restaurant):
	"""A simple representation of an ice cream stand restuarant."""
	def __init__(self, restaurant_name, cuisine_type, flavors):
		"""
		Initialize attributes of the Restaurant parent class.
		Then, initialize attributes of IceCreamStand.
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def display_flavors(self):
		"""Display all available flavors of ice cream at the stand"""
		print(f"{self.restaurant_name} has the following flavors of ice cream:")
		for flavor in self.flavors:
			print(f"\t- {flavor}")
