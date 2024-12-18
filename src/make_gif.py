import imageio.v2 as iio
import os
import re # regex for string matching

def create_gif(filenamesave):
    ''' This function creates a GIF by reading the list of PNG images from the specified folder, sorting them by depth, and saving them as a GIF file.

    Parameters:
        filenamesave (str): the name of the file to save.

    Returns:
        None: GIF is saved to figs directory
    '''
    images = []
    input_folder = '../figs'

    def extract_depth(filename):
        ''' This helper function extracts the depth value from a filename using regex.
    
        Parameters:
            filename (str): the name of the file from which to extract the depth value.

        Returns (int):
            The depth value extracted from the filename or 0 if no match is found.
        '''
        match = re.search(r'depth(\d+)_', filename)
        return int(match.group(1)) if match else 0 # Return the depth if found, else return 0
    
    sorted_files = sorted(os.listdir(input_folder), key=extract_depth) # Sort the files based on the depth
    
    for filename in sorted_files: # Loop through the files in the folder
        if filename.endswith('.png') and 'depth' in filename and not filename == 'merged_graph.png' and not filename == 'mag_depth.png':
            f = os.path.join(input_folder, filename)
            im = iio.imread(f)
            images.append(im)

    iio.mimsave(os.path.join(input_folder, filenamesave), images, duration=1, loop=0, fps = 7.5)

def main():
    create_gif('combined.gif')  # Saves output in the figs directory'
if __name__ == "__main__":
    main()