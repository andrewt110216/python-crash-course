# Python Crash Course
# Exercises 16-2, 3, and 4
# May 16, 2022

# 16-2 Sitka-Death Valley Comparison
# Compare the daily high-low temperature ranges of Sitka and Death Valley,
# making sure that the data aligns with the appropriate dates

# 16-3 San Francisco
# Add San Francisco to the plot for comparison. Download its data first.

# 16-4 Automatic Indexes
# Instead of hard coding the indexes used for date, high, low, etc., use the
# header row to find those indexes for each location

import csv
import matplotlib.pyplot as plt
from datetime import datetime


class Location:
    def __init__(self, name, filepath, date_format):
        self.name = name
        self.filepath = filepath
        self.date_format = date_format
        self.data = {}
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

# Create location objects, and load them into list of locations to be included in visual
directory = 'chapters/16-project2-downloading-data/'
sitka = Location('Sitka, AK', 'data/sitka_weather_2018_simple.csv', '%Y-%m-%d')
death_valley = Location('Death Valley, CA', 'data/death_valley_2018_simple.csv', '%Y-%m-%d')
san_francisco = Location('San Francisco, CA', 'data/san_francisco_weather_2018.csv', '%m/%d/%y')
santa_monica = Location('Santa Monica, CA', 'data/santa_monica_weather_2018.csv', '%m/%d/%y')
locations = [san_francisco, santa_monica]

# Extract data from csv file
for loc in locations:
    with open(directory + loc.filepath) as f:
        # Initialize reader and extract indexes from header row
        reader = csv.reader(f)
        header_row = next(reader)
        date_index = high_index = low_index = None
        for index, header in enumerate(header_row):
            if header == 'DATE':
                date_index = index
            elif header == 'TMAX':
                high_index = index
            elif header == 'TMIN':
                low_index = index
        if not (date_index and high_index and low_index):
            raise IndexError(f'One of the required columns (DATE, TMAX, TMIN) was not found for {loc.name}.')

        # Add data to the loc object's data attribute as key-value pairs - 'date': (high, low)
        for row in reader:
            try:
                date = datetime.strptime(row[date_index], loc.date_format)
            except ValueError:
                print(f"Unable to read date ({row[date_index]}) for {loc.name} using format {loc.date_format}. Quitting application.")
                quit()

            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {date} in {loc}. This date will be excluded.")
            else:
                loc.data[date] = (high, low)

# Identify dates for which all locations have complete temperature data
date_sets = []
for loc in locations:
    date_sets.append(set(loc.data.keys()))
common_dates = sorted(list(set.intersection(*date_sets)))

# Create the plot
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Plot the data for each city, using varying colors for visual effect
colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']
patterns = ['', '\\\\', 'o']
for index, loc in enumerate(locations):
    highs = [loc.data[date][0] for date in common_dates]
    lows = [loc.data[date][1] for date in common_dates]
    ax.plot(common_dates, highs, c=colors[index], linewidth=0.75,)
    ax.plot(common_dates, lows, c=colors[index], linewidth=0.75,)
    hatch_index = index // len(colors)
    ax.fill_between(common_dates, highs, lows,
                    facecolor=colors[index],
                    alpha=0.1,
                    label=loc.name,
                    hatch=patterns[hatch_index])

# Format plot
ax.set_title('Comparing Daily High & Low Temperatures (2018)', fontsize=16)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=14)
plt.legend()

plt.show()
