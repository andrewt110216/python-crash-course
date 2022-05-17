# Python Crash Course
# Exercise 15-3
# April 4, 2022

"""Use Matplotlib to visualize a Random Walk on an x-y scatter plot"""

# 15-3
# Modify rw_visual.py by replacing ax.scatter() with ax.plot()
# To simulate the path of a pollen grain on the surface of a drop of water,
# pass in the rw.x_values and rw.y_values and include a linewidth argument.
# Use 5,000 instead of 50,000 points.

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	# Set up the random walk instance
	rw = RandomWalk(5_000)
	rw.fill_walk()

	# Set up pyplot plot
	plt.style.use('seaborn-dark')
	fig, ax = plt.subplots(figsize=(15, 9))
	
	# Plot all points
	ax.plot(rw.x_values, rw.y_values, color='orange', linewidth=1)
	
	# Plot start and end points with unique formatting
	ax.scatter(0, 0, c='green', edgecolors='none', s=40)
	ax.scatter(rw.x_values[-1], rw.y_values[-1],
		c='red', edgecolors='none', s=40)

	# Remove axes
	# ax.get_xaxis().set_visible(False)
	# ax.get_yaxis().set_visible(False)

	plt.show()

	# Allow the user to create a new random walk or exit
	keep_going = input('Make another random walk? (y/n): ')
	if keep_going.lower() == 'n':
		break
