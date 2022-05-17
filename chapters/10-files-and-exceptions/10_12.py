# Python Crash Course
# Exercise 10-12
# 03/21/2022
# Andrew Tracey

# Combine the two files from Exercise 10-11
# If the number is already stored, then report it. If not, ask the user to 
#  input it and store it in a file.

import json


def get_favorite_number(store_file):
	"""Report the user's favorite number, or store it to file."""
	try:
		with open(filename, encoding='utf-8') as f:
			fav_number = json.load(f)
	except FileNotFoundError:
		favorite_number = input('What is your favorite number? ')
		with open(filename, 'w', encoding='utf-8') as f:
			json.dump(favorite_number, f)
		print("Thanks. I'll remember that for next time.")
	else:
		print(f"I know your favorite number! It's {fav_number}.")


filename = 'favorite_number_2.json'
get_favorite_number(filename)
