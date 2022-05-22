# Python Crash Course
# Chapter 16 - Page 351
# 05/17/2022

import json

# Explore the structure of the data
directory = 'chapters/16-project2-downloading-data/'
filename = 'data/eq_data_1_day_m1.json'
with open(directory + filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(directory + readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extract earthquake data
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
