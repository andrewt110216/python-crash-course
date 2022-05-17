# Python Crash Course
# Exercise 8-15 - Separate Module for Printing Functions
# March 10, 2022

def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model:", current_design)
		completed_models.append(current_design)


def show_completed_models(completed_models):
	"""Show all models that were printed."""
	print("\nThe following models have been printed.")
	for completed_model in completed_models:
		print(f"\t{completed_model}")
