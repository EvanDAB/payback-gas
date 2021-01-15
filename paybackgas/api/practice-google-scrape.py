import requests
from urllib.parse import urlencode

api_key = 'AIzaSyCNyQlXhkdhJQ4iczZl79qrzPf8EJXhzL8'

def extract_lat_lng(address_or_postalcode, data_type='json'):
    endpoint= f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {'address': address_or_postalcode, 'key': api_key}
    url_params = urlencode(params)
    url = f'{endpoint}?{url_params}'
    r = requests.get(url)
    print(url)
    if r.status_code not in range(200, 299):
        return {}
    return r.json()

print(extract_lat_lng('1600 Ampitheatre Parkway, Mountain View, CA'))

print('Goodbye World')