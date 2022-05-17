# Python Crash Course
# Exercise 15-1 and 2
# 3/25/2022

# 15.1
# Plot the first 5,000 cubic numbers
# 15.2
# Apply a colormap to your cubes plot

import matplotlib.pyplot as plt


x_values = range(1, 5_001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.spring, s=10)

# Set up the title and axis labels
ax.set_title("Cubic Numbers", fontsize=16)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cube of Value", fontsize=12)

# Set axis ranges
ax.axis([0, 5_000*1.1, 0, 5_000**3*1.1])

# Save plot to file as PNG
plt.savefig('cubes_plot.png')
plt.show()
