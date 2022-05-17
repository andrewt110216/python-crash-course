# Python Crash Course
# Exercises 10-2
# 03/14/2022
# Andrew Tracey

# Using the program from 10-1, use replace() method to replace the word 
#  "Python" with another language, such as "C". Print each modified line.

filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	new_line = line.replace("Python", "Ruby")
	print(new_line.strip())
