# Python Crash Course
# Exercise 15-8
# April 6, 2022

# Multiplication
# Create a simulation showing what happens when you roll two 6-sided dice,
#  and the result is the product of the two rolls

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Generate the required dice and set the number of rolls
die1 = Die(6)
die2 = Die(6)
rolls = 1_000_000

# Determine and set the minimum and maximum results of each turn
min_result = 1
max_result = die1.num_sides * die2.num_sides

# Roll the dice many times and record the result
results = []
interval = rolls * 0.1
for cur_roll in range(1, rolls+1):
    results.append(die1.roll() * die2.roll())
    if cur_roll % interval == 0:
        percent_completed = int(cur_roll / rolls * 100)
        print(f'{percent_completed}% completed...'.rjust(18))

# Calculate the frequencies of each roll in results
frequencies = []
for number in range(min_result, max_result + 1):
    frequency = results.count(number)
    frequencies.append(frequency)

# Print the frequencies
print(frequencies)
print('Sum of all frequencies:', f"{sum(frequencies):,}")

# Visualize
x_values = list(range(min_result, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result (Product)', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling two 8-sided die {rolls:,} times',
                    title_xanchor='left',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout},
    filename='chapters/15-project2-generating-data/ex_15_8.html')
