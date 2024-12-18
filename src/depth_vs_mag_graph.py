'''
This script creates the depth vs magnitude scatter plot of the earthquakes in the data collected in merged_data.geojson. Then it saves that plot to the figs directory.
'''
import geopandas as gpd
import matplotlib.pyplot as plt

df = gpd.read_file(f"../data/merged_data.geojson")
depth = []
magnitude = []
for item in df.geometry:
    depth.append(item.z)
for item in df.mag:
    magnitude.append(item)

plt.scatter(depth, magnitude)
plt.title("Depth vs. Magnitude")
plt.xlabel("Depth")
plt.ylabel("Magnitude")
plt.savefig(f"../figs/mag_depth.png")