import json
import math

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Load data from json file
directory = 'chapters/16-project2-downloading-data/'
filename = 'data/eq_data_30_day_m1.json'
with open(directory + filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
data_title = all_eq_data['metadata']['title']

# Extract data
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3*m for m in mags],
        'color': mags,
        'colorscale': 'YlOrRd',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title=data_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
