import requests
import json
import os

def get_distance(origin: tuple, dest: tuple) -> dict:
    """Method to determine the distance by Public Transport between an origin and destination.
    Args:
        origin - tuple of latitude and longitude
        dest - tuple of latitude and longitude
    
    Returns:
        json-object converted to dict of distance data
    """
    API_KEY = os.getenv('API_KEY')
    BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    origin = str(origin[0]) + ',' + str(origin[1])
    origin_qs = 'origins=' + origin

    dest = str(dest[0]) + ',' + str(dest[1])
    dest_qs = '&destinations=' + dest

    mode = '&mode=transit&departure_time=1587223538' # time is 16:25

    url = BASE_URL + origin_qs + dest_qs + mode + '&key=' + API_KEY
    return requests.get(url).json()

def parse_request_data(response: dict) -> int:
    """Parse API response from Google Distance Matrix API.
    Args:
        response - response from Google Distance Matrix API

    Returns:
        time - time taken to travel between origin and destination in seconds.
    """
    return response['rows'][0]['elements'][0]['duration']['value']


def geocode_location(location: str) -> tuple:
    """Geocode location name into coordinates.
    Args:
        location - name of location

    Returns:
        location coordiantes
    """
    API_KEY = os.getenv('API_KEY')
    BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'

    location = 'address=' + location.replace(' ', '+')

    components = '&components=locality:paris|country:FR'

    url = BASE_URL + location + components + '&key=' + API_KEY
    response = requests.get(url).json()
    geo = response['results'][0]['geometry']['location']
    return (geo['lat'], geo['lng'])
    