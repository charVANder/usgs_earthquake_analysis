# Imports
import requests
import json
from datetime import datetime, timedelta

# Function to request data for a specific month
def request_month(start_date, end_date, min_latitude, max_latitude, min_longitude, max_longitude):
    ''' This function calls the`request_data` function to fetch earthquake data based on the provided date range and geographical bounds.

    Parameters:
        start_date (str): Start date of the period to fetch data for (in 'YYYY-MM-DD' format).
        end_date (str): End date of the period to fetch data for (in 'YYYY-MM-DD' format).
        min_latitude (float): Minimum latitude of the bounding box.
        max_latitude (float): Maximum latitude of the bounding box.
        min_longitude (float): Minimum longitude of the bounding box.
        max_longitude (float): Maximum longitude of the bounding box.

    Returns:
        data: The data containing earthquake data in JSON format if the request is successful, or None if the request fails.
    '''
    # Make the data request using the specified parameters
    data = request_data(start_date, end_date, min_latitude, max_latitude, min_longitude, max_longitude)
    return data

# Created a rough draft function to make data request flexible
def request_data(start_date, end_date, min_latitude, max_latitude, min_longitude, max_longitude):
    '''This function requests earthquake data within a specified date range and geographic bounds from the USGS Earthquake API. The response is expected to be in GeoJSON format.

    Parameters:
        start_date (str): Start date for data retrieval (in 'YYYY-MM-DD' format).
        end_date (str): End date for data retrieval (in 'YYYY-MM-DD' format).
        min_latitude (float): Southernmost latitude of the bounding box.
        max_latitude (float): Northernmost latitude of the bounding box.
        min_longitude (float): Westernmost longitude of the bounding box.
        max_longitude (float): Easternmost longitude of the bounding box.

    Returns:
        dict: A dictionary containing earthquake data in GeoJSON format, or None if the request fails.
    '''
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    parameters = {
        'format': 'geojson',
        'starttime': start_date,
        'endtime': end_date,
        'orderby': 'time',
        'minlatitude': min_latitude,
        'maxlatitude': max_latitude,
        'minlongitude': min_longitude,
        'maxlongitude': max_longitude
    }
    response = requests.get(url, params=parameters)

    # Make sure the request is successful and return the data
    if response.status_code == 200:
        return response.json()
    
    # Raise error message if the request is unsuccessful
    else:
        print(f"Data requesting error: {response.status_code}. {response.text}")
        return None
    
def save_data(data, filename='data.geojson'):
    '''This function saves the earthquake data to a GeoJSON file. Writes the provided seismic data to a file in GeoJSON format.

    Parameters:
        data (dict): Earthquake data to save, typically in GeoJSON format.
        filename (str): The name of the file to save the data to (default is 'data.geojson').

    Returns: None, saves the data to the specified file.
    '''
    with open(filename, 'w') as file:
        json.dump(data, file, indent=1)
    print(f"GeoJSON data saved to {filename}")

def main():
    # Specify date range of request
    start_date = '2023-01-31'
    end_date = '2024-01-31'

    # Specify the geographical area (default SA area)
    min_latitude = -37
    max_latitude = -16
    min_longitude = -75
    max_longitude = -64

    # Data chunk counter
    chunk = 1

    # Iterate over each month in the date range
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    while current_date <= datetime.strptime(end_date, '%Y-%m-%d'):
        # Calculate end of current month
        next_month = current_date.replace(day=28) + timedelta(days=4)
        end_of_month = next_month - timedelta(days=next_month.day)

        # Request data for the current month
        data = request_month(
            current_date.strftime('%Y-%m-%d'),
            end_of_month.strftime('%Y-%m-%d'),
            min_latitude,
            max_latitude,
            min_longitude,
            max_longitude
        )

        # This line is to get rid of the extra data file error
        if data and len(data.get('features', [])) > 0:
            filename = f"../data/data{chunk}.geojson"
            save_data(data, filename)
            chunk += 1

        # Move on to the next month
        current_date = end_of_month + timedelta(days=1)

if __name__ == "__main__":
    main()
