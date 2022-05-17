# Python Crash Course
# Exercise 9-1
# March 10, 2022

# Restaurant
# Make a Restaurant class that sores two attributes: name and cuisine_type.
# Make a method that prints these two pieces of information, and a method
# that prints a message indicating that the restaurant is open.

# Make an instance of your class and print the attributes and call the methods.

class Restaurant():
	"""A simple respresentation of a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes of the Restaurant object."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Print the known information about the restaurant."""
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"The cusine type is {self.cuisine_type}.")

	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant("Colapasta", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
Restaurant.describe_restaurant(restaurant)
Restaurant.open_restaurant(restaurant)
