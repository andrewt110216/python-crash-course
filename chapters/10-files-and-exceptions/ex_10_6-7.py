# Python Crash Course
# Exercises 10-6 and 10-7
# March 21, 2022

# 10-6 Addition
# Write a program to allow the user to add two numbers.
# Use a try-except to catch the possible ValueError if the user inputs
#  a letter or character that cannot be converted to a number

# 10-7
# Wrap your code from 10-6 in a while loop so the user can continue entering
#  numbers even if they make a mistake and enter text instead of a number
# Well, I wrote it that way the first time because I'm an over-achiever.

# Initialize variables
a, b = None, None
quit = False

print("Let's do some addition. You will be prompted to input 2 numbers.")
print("Please only input numbers. Type 'q' at any time to quit.")

while quit == False:
	# Take first input, check for quit value and try to convert to float
	input1 = input(">>Input the first number: ")
	if input1.lower() == 'q':
		quit == True
		break
	try:
		a = float(input1)
	except ValueError:
		print(f"{input1} is not a number. Please try again.")
	else:
		# Take second input, check for quit value and try to convert to float
		# Use second while loop to allow user to try again, but keep input 'a'
		while True:
			input2 = input(">>Input the second number: ")
			if input2.lower() == 'q':
				quit == True
				break
			try:
				b = float(input2)
			except ValueError:
				print(f"{input2} is not a number. Please try again.")
			else:
				print(f"The result of adding your numbers is: {a + b}")
				go_again = input("Would you like to go again? (Y/N): ")
				if go_again.lower() == "n":
					quit = True
					break
				else:
					break
