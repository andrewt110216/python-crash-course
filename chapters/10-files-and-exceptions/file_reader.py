# Python Crash Course
# Chapter 10 - Page 184
# March 14, 2022

# Practice reading in text from a file

with open('chapters/10-files-and-exceptions/pi_digits.txt') as file_object:
	contents = file_object.read()

filename = 'chapters/10-files-and-exceptions/pi_million_digits.txt'
pi_string = ''
with open(filename) as file_object:
	for line in file_object:
		pi_string += line.strip()

print(pi_string[:52],"...")
print("Length of pi_string:", f"{len(pi_string):,}")

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	found = pi_string.index(birthday)
	print(f"Your birthday appears starting at decimal place # {found - 1:,}!")
else:
	print("Your birthday does NOT appear in the first million digits of pi.")
