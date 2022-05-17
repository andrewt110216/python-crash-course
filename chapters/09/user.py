# Python Crash Course
# user.py (Exercises 9-11)
# 03/14/2022
# Andrew Tracey

# Store the classes created in Exercise 9-8 in a separate module

"""A set of classes to describe an employee as user of the computer network."""

class User():
	"""Store information for individual user profile"""

	def __init__(self, first_name, last_name, **kwargs):
		self.first_name = first_name
		self.last_name = last_name
		for k, v in kwargs.items():
			setattr(self, k, v)

	def describe_user(self):
		"""Print all attributes of the user"""
		for attribute, value in vars(self).items():
			print(f"{attribute}: {value}")
		print("--------------------------")


	def greet_user(self):
		"""Greet the user with a personalized message"""
		print("--------------------------")
		print(f"Hello, {self.first_name.title()}")
		print("--------------------------")
