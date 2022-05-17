"""Simple line graph plotting square numbers."""
import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('dark_background')  # Solarize_Light2
fig, ax = plt.subplots()
ax.plot(x_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of Value", fontsize=14)

# Set size of tick label.
ax.tick_params(axis='both', labelsize=14)

plt.show()
