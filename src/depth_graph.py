'''
This script creates the static images that will later be combined into the GIF that shows the earthquake subduction under the Andes.
'''
from save_graph import save_graph
from pathlib import Path

collection = [] # Will hold the content to merge
my_path = Path('../data/')

# Grab all the necessary files in directory
files_list = [str(file) for file in my_path.glob('*') if file.is_file()
              and file.name.lower().startswith("depth")
              and file.name.endswith('geojson')]

for file in files_list:
    print(file)
    save_graph(file, file[8:-8], "Subduction Under the Andes")