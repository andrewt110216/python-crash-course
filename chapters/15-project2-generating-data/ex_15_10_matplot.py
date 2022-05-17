# Python Crash Course
# Exercise 15-10
# April 6, 2022

# Practicing with Both Libraries
# Practice using Matplotlib and Plotly libraries
# Part 1
# Try using Matplotlib (instead of Plotly) to visualize die rolling

# Plan
#  1. Set up the die and store the results
#  2. Figure out how to create a bar graph in Matplotlib

import matplotlib.pyplot as plt
from die import Die

# Set up the game
die1 = Die(6)
die2 = Die(6)
die3 = Die(6)
rolls = 100_000
max_result = die1.num_sides + die2.num_sides + die3.num_sides
min_result = 3

# Play the game
results = [die1.roll() + die2.roll() + die3.roll() for _ in range(rolls)]

# Evaluate the frequency of each result
frequencies = [results.count(n) for n in range(min_result, max_result+1)]

# Visualize
x_values = list(range(min_result, max_result+1))
y_values = frequencies
fig, ax = plt.subplots()
ax.bar(x_values, y_values, width=0.7, edgecolor='none', color='green')
ax.set_xticks(x_values)
ax.set_title(f'Analysis of rolling 3 6-sided dice {rolls:,} times')
ax.set_xlabel('Sum of Rolls')
ax.set_ylabel('Frequency of Result')
yticks = ax.get_yticks()
plt.show()

# Data checks
print('---DATA CHECKS---')
print('Possible results:', x_values)
print('Number of unique results:', len(frequencies))
print('Frequencies of results:', frequencies)
print(f'Total rolls captured in frequencies: {sum(frequencies):,}')
