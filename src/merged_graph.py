'''
This script takes the merged_data geojson file and creates the combined graph from 1/31/2023-1/31/2024. Title with the start/end dates is customizable, although the generated graphs are made to match the default dates.
'''
from save_graph import save_graph
import argparse

# Setup for argparse
parser = argparse.ArgumentParser(description="Graph has an optional customizable date range.")
parser.add_argument(
    "--start_date",
    type=str,
    default="1/31/2023",  # default start date to match collected data
    help="Start date in MM/DD/YYYY format (default is 1/31/2023)."
)
parser.add_argument(
    "--end_date",
    type=str,
    default="1/31/2024",  # default end date to match collected data
    help="End date in MM/DD/YYYY format (default is 1/31/2024)."
)

args = parser.parse_args()
start_date = args.start_date
end_date = args.end_date
title = f"Earthquakes ({start_date} - {end_date})"
save_graph("merged_data.geojson", "merged_graph", title=title)
