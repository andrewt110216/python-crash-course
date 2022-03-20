# Python Crash Course
# Exercises 9-5
# 03/11/2022
# Andrew Tracey

# Start with program from 9.3
# Add an attribute called login_attempts.
# Write a method that increments the value of attempts by 1.
# Write another method that resets the value of attempts to 0.
# Make an instance of User class, increment login attempts several times and
# print the value to make sure it was incremented.
# Then reset login attempts and print again to make sure it was reset to 0.

class User():
	"""Store information for individual user profile"""

	def __init__(self, first_name, last_name, **kwargs):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
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

	def increment_login_attempts(self):
		"""Increment the number of login attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset the number of login attempts to 0"""
		self.login_attempts = 0


andrew = User("andrew", "tracey", age=30, location="Santa Monica")
andrew.greet_user()

andrew.increment_login_attempts()
andrew.increment_login_attempts()
andrew.increment_login_attempts()
andrew.describe_user()

andrew.reset_login_attempts()
andrew.describe_user()
