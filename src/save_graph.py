import pandas as pd
import geopandas as gpd
import contextily as cx
import matplotlib.pyplot as plt


def save_graph(filename, savefile, title=False):
    ''' This function generates and saves a plot of the geospatial data from the generated GeoJSON files. It transforms the coordinate system, plots the data with a color scale, and overlays a basemap. The plot is then saved as a PNG file.

    Parameters:
        filename (str): Name of the input GeoJSON file to read (located in the data directory).
        savefile (str): Name of the output file to save the plot in the figs directory.
        title (str, optional): The title of the plot.

    Returns:
        None: Saves the plot as a PNG
    '''
    df = gpd.read_file(f"../data/{filename}")
    df_wm = df.to_crs(epsg=4979) # coordinate system
    ax = df_wm.plot(figsize=(12, 15), alpha=0.75, edgecolor="k", column=df.geometry.z,
                    legend=True, vmin=0, vmax=600,
                    legend_kwds={"label": "Depth"},
                    cmap="gist_earth")

    # Limit bounds
    ax.set_xlim(-77, -60)
    ax.set_ylim(-39, -14)
    if title:
        plt.title(title, fontsize=24, pad=25)

    # Adding maps
    cx.add_basemap(ax, crs=df.crs) # adding map behind the plots
    plt.savefig(f"../figs/{savefile}.png")  # saves to the figs folder