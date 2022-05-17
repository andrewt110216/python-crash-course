# Python Crash Course
# Exercises 8-12
# 03/10/2022
# Andrew Tracey

# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the
# function call provides, and print a summary of the sandwich.

# Call the function 3 times, using a different number of arguments each time.
def make_sandwich(*args):
	"""
	Accept a list of items a person wants on a sandwich.
	Print a summary of the sandwich being ordered.
	"""
	print(args)
	print("The sandwich being made will include the following:")
	for topping in args:
		print(f" - {topping}")


make_sandwich('cheese')
make_sandwich('ham', 'cheese')
make_sandwich(
	'turkey', 'salami', 'ham', 'cheese', 'lettuce', 'onion', 'tomato', 'mayo'
	)
