# Python Crash Course
# Chapter 16 (Page 343)
# May 16, 2022

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Extract data from csv file
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Print column indexes and headers for reference
    # for index, header in enumerate(header_row):
    #     print(index, header)

    # Get dates and high and low temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {date}. This date will be excluded.")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

# Plot the temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=0.75)
ax.plot(dates, lows, c='blue', linewidth=0.75)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title('Death Valley, CA - 2018 - Daily High & Low Temperatures', fontsize=16)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=14)

plt.show()
