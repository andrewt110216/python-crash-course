# Python Crash Course
# Exercise 9-4
# March 11, 2022

# Number Served
# Start with program from 9.1
# Add an attribute called number_served with default value of 0.
# Create an instance of this class and print the number of customers the
# restaurant has served, then change this value and reprint.

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


restaurant = Restaurant("Colapasta", "Italian")
print("Customers served:", restaurant.number_served)
restaurant.number_served = 15
print("Customers served:", restaurant.number_served)

# Add a method to set the number of customers served. Call this method.
restaurant.set_number_served(25)
print("Customers served:", restaurant.number_served)

# Add a method to increment the number of customers served. Call this method.
restaurant.increment_number_served(5)
print("Customers served:", restaurant.number_served)
