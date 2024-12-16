from pathlib import Path
import geojson
import pandas as pd
import geopandas as gpd
'''
This script reads all the GeoJSON files from the data directory, filters the files based on their names and extensions, and merges them into a single GeoDataFrame. The GeoDataFrame is saved as a new GeoJSON file to be used for the rest of the project.
'''
collection = [] # list of content to merge
my_path = Path('../data/') # the directory path

# Grab all the files in the directory
files_list = [str(file) for file in my_path.glob('*') if file.is_file()
              and file.name.lower().startswith("data")
              and file.name.endswith('geojson')]

# Iterating through the geojson files
for file in files_list:
    with open(file) as f:
        data = gpd.read_file(f)
        collection.append(data)

# saving the newly concatenated file
with open('../data/merged_data.geojson', 'w') as f:
    geojson.dump(pd.concat(collection), f)
