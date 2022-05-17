"""Simple demonstration of plotting a single data point using scatter()."""

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(
	x_values, y_values, s=10, marker="*", c=y_values, cmap=plt.cm.prism)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=16)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)
ax.set_frame_on(False)
ax.grid(visible=True, c='gray', linestyle='--')


# Set the range for each axis.
ax.axis([0, 1100, 0, 1000**2+100**2])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')
