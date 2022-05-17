# Python Crash Course
# Exercise 10-13
# 03/21/2022
# Andrew Tracey

# Modify the latest version of remember_me.py to first ask the user if the
#  retrieved username is correct. If not, let them re-enter it.

import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def welcome_user(name):
	"""Print a message welcoming the user."""
	print(f"We'll remember you when you come back, {name}!")

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		correct_user = input(f"Hi. Is this {username}? (Y/N): ")
		if correct_user.lower() == 'y':
			print(f"Welcome back, {username}!")
		else:
			username = get_new_username()
			welcome_user(username)
	else:
		username = get_new_username()
		welcome_user(username)

greet_user()
