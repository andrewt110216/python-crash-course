# Python Crash Course
# Exercise 10-11 - Part 1
# March 21, 2022

# Write a program to ask the user for their favorite number and store it.
import json

directory = 'chapters/10-files-and-exceptions/'
filename = 'favorite_number.json'
favorite_number = input('What is your favorite number? ')

with open(directory + filename, 'w', encoding='utf-8') as f:
	json.dump(favorite_number, f)
