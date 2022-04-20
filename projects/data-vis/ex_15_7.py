# Python Crash Course
# Exercise 15-7
# 04/06/2022

# Create a simulation showing what happens when you roll three 6-sided dice

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Generate two 8-sided die
die1 = Die(6)
die2 = Die(6)
die3 = Die(6)

# Roll the dice many times and record the sum of the rolls
results = []
rolls = 1_000_000
interval = rolls * 0.1
for roll_num in range(1, rolls+1):
    results.append(die1.roll() + die2.roll() + die3.roll())
    if roll_num % interval == 0:
        percent_completed = int(roll_num / rolls * 100)
        print(f'{percent_completed}% completed...'.rjust(18))

# Calculate the frequencies of each roll in results
frequencies = []
min_result = 3  # Equal to the number of die being rolled
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for number in range(min_result, max_result + 1):
    frequency = results.count(number)
    frequencies.append(frequency)

# Print the frequencies
print(frequencies)
print('Sum of all frequencies:', f"{sum(frequencies):,}")

# Visualize
x_values = list(range(min_result, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result (Sum)', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title=f'Results of rolling three 6-sided dice {rolls:,} times',
    title_xanchor='left', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='ex_15_7.html')
