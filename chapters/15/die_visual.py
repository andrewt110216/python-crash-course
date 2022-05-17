# Python Crash Course
# Chapter 15 (Pages 325-330)
# 04/05/2022

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Generate a 6-sided die
die = Die(6)

# Roll the die 1,000 times and track the results in a list
results = []
for _ in range(1_000):
    results.append(die.roll())

# Calculate the frequencies of each roll in results
frequencies = []
for side in range(1, die.num_sides + 1):
    frequency = results.count(side)
    frequencies.append(frequency)

# Display the results and frequencies
print(results)
print(frequencies)
print('Sum of all frequencies:', f"{sum(frequencies):,}")

# Visualize the results and frequencies
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of 1,000 Rolls of a 6-Sided Die',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
