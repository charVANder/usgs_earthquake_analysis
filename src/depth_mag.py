'''
This script takes the combined/merged dataset, finds the minimum and maximum depth, then splits the data into 10 chunks. Used to create the merged graph image.
'''
import pandas as pd
import geopandas as gpd
import geojson

df = gpd.read_file(f"../data/merged_data.geojson")

for i in range(0, int(max(df.get_coordinates(include_z=True).z)) + 20,
               int((max(df.get_coordinates(include_z=True).z) + 20) / 40)):
    indexes = []
    for index in range(len(df.iloc[:])):
        if i <= df.iloc[index].geometry.z <= (max(df.get_coordinates(include_z=True).z) / 40 + i):
            indexes.append(index)
    new_df = df.iloc[indexes]
    if not new_df.empty:
        with open(f'../data/depth{i}_{i + int((max(df.get_coordinates(include_z=True).z) + 20) / 40)}.geojson', 'w') as f:
            geojson.dump(new_df, f)
