# Python Crash Course
# Exercises 9-14 & 15
# 03/14/2022
# Andrew Tracey

# 9-14 Lottery
# Make a list or tuple containing a series of 10 numbers and five letters.
# Randomly select four numbers or letters and print a message saying that 
#  any ticket matching these four numbers wins a prize

import random

lotto_balls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'e', 'h']
picks = [str(random.choice(lotto_balls)) for _ in range(4)]
winning_ticket = "-".join(picks)

print(f"The winning lottery ticket number is!...{winning_ticket}")
print(f"If your ticket is an exact match, "
		"please come in to collect your prize!")

# 9-15 Lottery Analysis
# You can use a loop to see how hard it might be to win this lottery.
# Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give you
#  a winning ticket.


my_ticket = random.choices(lotto_balls, k=3)
pulls = 0

while True:
	winning_ticket = random.choices(lotto_balls, k=3)
	pulls += 1
	if my_ticket == winning_ticket:
		break

print(f"It took {pulls:,} pulls to get a winning ticket.")
