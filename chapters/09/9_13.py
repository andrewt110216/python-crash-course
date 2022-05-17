# Python Crash Course
# Exercises 9-13
# 03/14/2022
# Andrew Tracey

# Make a class Die with one attribute called sides, which has a default value
#  of 6. Write a method to roll the die and print a random number.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

import random


class Die:
	"""A simple representation of an n-sided die."""

	def __init__(self, sides=6):
		self.sides = sides
		self.name = f"{self.sides}-sided die"

	def __repr__(self):
		return self.name

	def roll_die(self, rolls=1):
		"""Simulate rolling of the die x number of times."""
		print("-------------------------------------")
		print(f"Rolling the {self.name}...")
		for x in range(1, rolls + 1):
			result = random.randint(1, self.sides)
			print(f"  Round {x}: rolled a {result}")
		print("-------------------------------------")


die10 = Die(10)
die20 = Die(20)

die10.roll_die(10)
die20.roll_die(10)
