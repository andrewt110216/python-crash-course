# Python Crash Course
# Exercise 2-3
# September 10, 2021

# Personal Message
# Use a variable to represent a person's name, and print a message to that person.
# Your message should be simple.

first_name = "Tom"
last_name = "Brady"
full_name = f"The oldest player in the leageu is {first_name} {last_name}."
print(full_name)

# Practice using the tab and new line characters in a string
print("\tIndent")
print("Players:\n\tLeonard Fournette\n\tRonald Jones II\n\tAntonio Brown")

# Practicue using the strip method on strings to remove whitespace
dumb_input = "  Answer   "
print(dumb_input.rstrip() + "See?")
print(dumb_input.lstrip() + "See?")
print(dumb_input.strip())
