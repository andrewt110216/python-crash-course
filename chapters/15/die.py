# Python Crash Course
# Chapter 15 (Page 324)
# 04/05/2022

from random import randint


class Die:
    """A simple representation of an n-sided die"""
    def __init__(self, num_sides=6):
        """Initialize the die with n sides, defaulting to 6"""
        self.num_sides = num_sides

    def roll(self):
        """Return the result of a single roll of the die."""
        return randint(1, self.num_sides)
