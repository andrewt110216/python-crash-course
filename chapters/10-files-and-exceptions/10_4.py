# Python Crash Course
# Exercises 10-4
# 03/18/2022
# Andrew Tracey

# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a line
#  recording their visit in a file called guest_book.txt. Make sure each entry
#  appears on a new line in the file

import datetime


while True:
	name = input("Hello! Please tell me your name (or 'q' to exit)? ")
	if name == 'q' or name == 'Q':
		break
	else:
		print(f"Hello, {name.title()}!")
		now = datetime.datetime.now()
		guest_book_entry = f"{now.date()} {now.time()}: Visit from {name}.\n"

	with open('guest_book.txt', 'a') as myfile:
		myfile.write(guest_book_entry)

	option = input("Would you like to add another user (Y/N)? ")
	if option.lower() == 'n':
		break
