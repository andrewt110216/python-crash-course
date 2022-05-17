# Python Crash Course
# Exercise 10-3
# March 18, 2022

# Guest
# Write a program that prompts the user for their name. When they respond,
#  write their name to a file called guest.txt

name = input("Hello. Please tell me your name? ")

with open('chapters/10-files-and-exceptions/guest.txt', 'w') as myfile:
	myfile.write(f"{name}")
