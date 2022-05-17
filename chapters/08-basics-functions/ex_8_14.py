# Python Crash Course
# Exercise 8-14
# March 10, 2022

# Cars
# Write a function that stores informaiton about a car in a dictionary
# The function should always receive a manufacturer and a model name.
# It should then accept an arbirtary number of keyward arguments.

import pprint


def make_car(make: str, model: str, **kwargs) -> dict:
	"""Return a dictionary of information about a car"""
	kwargs['make'] = make
	kwargs['model'] = model
	return kwargs

car = make_car('mazda', 'CX-5', color='blue', sport_package=True, miles=1000)
pp = pprint.PrettyPrinter(indent=2, sort_dicts=False)
pp.pprint(car)
