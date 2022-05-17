# Python Crash Course
# Exercises 10-11 - Part 2
# March 21, 2022

# Favorite Number
# Write a program to get the user's favorite number, from Part 1 of this Q.

import json

directory = 'chapters/10-files-and-exceptions/'
filename = 'favorite_number.json'

with open(directory + filename, encoding='utf-8') as f:
	fav_number = json.load(f)

print(f"I know your favorite number! It's {fav_number}.")
