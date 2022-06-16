# Python Crash Course
# Exercise 9-3
# March 11, 2022

# Users
# Make a class called User with attributes first name and last name, then
# create several other attributes for the user profile.
# Make a method to describe the user that prints a summary.
# Make another method t greet the user.
# Create several instances and call both methods for each.

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


andrew = User("andrew", "tracey", age=30, location="Santa Monica")
andrew.greet_user()
andrew.describe_user()

lisa = User("lisa", "cappucino", age=29, location="Santa Monica")
lisa.greet_user()
lisa.describe_user()

ben = User("ben", "tracey", age=25, location="Chicago", salary=240000)
ben.greet_user()
ben.describe_user()
