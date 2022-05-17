# Python Crash Course
# Exercises 10-3
# 03/18/2022
# Andrew Tracey

# Write a program that prompts the user for their name. When they respond,
#  write their name to a file called guest.txt

name = input("Hello. Please tell me your name? ")

with open('guest.txt', 'w') as myfile:
	myfile.write(f"{name}")
