__author__ = 'madevelasco'

import geojson

with open('milano-grid.geojson') as f:
    data = geojson.load(f)

for feature in data['features']:
    print feature['geometry']['type']
    print feature['geometry']['coordinates']
    print feature['properties']['cellId']