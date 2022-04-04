# Python Crash Course
# Exercises 10-11 - Part 1
# 03/21/2022
# Andrew Tracey

# Write a program to ask the user for their favorite number, and store it.
import json


filename = 'favorite_number.json'
favorite_number = input('What is your favorite number? ')

with open(filename, 'w', encoding='utf-8') as f:
	json.dump(favorite_number, f)
