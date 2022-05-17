# Python Crash Course
# Exercise 10-2
# March 14, 2022

# Learning C
# Using the program from 10-1, use replace() method to replace the word 
#  "Python" with another language, such as "C". Print each modified line.

filename = 'chapters/10-files-and-exceptions/learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	new_line = line.replace("Python", "Ruby")
	print(new_line.strip())
