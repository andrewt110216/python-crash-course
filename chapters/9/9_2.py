# Python Crash Course
# Exercises 9-2
# 03/11/2022
# Andrew Tracey

# Start with your class from 9.1
# Create 3 different instances and call describe_restaurant for each.

class Restaurant():
	"""A simple respresentation of a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes of the Restaurant object."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Print the known information about the restaurant."""
		print("------------------------------------")
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"The cusine type is {self.cuisine_type}.")
		print("------------------------------------")

	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		print("------------------------------------")
		print(f"{self.restaurant_name} is now open!")
		print("------------------------------------")


colapasta = Restaurant("Colapasta", "Italian")
sunda = Restaurant("Sunda", "Asian Fusion")
nui = Restaurant("Nui", "Japanese")
Restaurant.describe_restaurant(colapasta)
Restaurant.describe_restaurant(sunda)
Restaurant.describe_restaurant(nui)
