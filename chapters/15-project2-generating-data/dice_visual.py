# Python Crash Course
# Chapter 15 (Pages 328)
# 04/05/2022

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Generate two 6-sided die
die1 = Die(6)
die2 = Die(10)

# Roll the dice many times and record the sum of the rolls
results = []
for _ in range(50_000):
    results.append(die1.roll() + die2.roll())

# Calculate the frequencies of each roll in results
frequencies = []
min_result = 2
max_result = die1.num_sides + die2.num_sides
for number in range(min_result, max_result + 1):
    frequency = results.count(number)
    frequencies.append(frequency)

# Display the results and frequencies
#print(results)
print(frequencies)
print('Sum of all frequencies:', f"{sum(frequencies):,}")

# Visualize the results and frequencies
x_values = list(range(min_result, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50,000 times',
                    title_xanchor='left',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='two_die.html')
