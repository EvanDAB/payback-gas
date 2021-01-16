import requests
from urllib.parse import urlencode, urlparse, parse_qsl

def listToUrlString(s):
    str1 = "|"
    return (str1.join(s))

def determine_distance(*dest, data_type='json'):
    api_key = 'AIzaSyCNyQlXhkdhJQ4iczZl79qrzPf8EJXhzL8'
    endpoint = f'https://maps.googleapis.com/maps/api/distancematrix/{data_type}'
    stops = []
    for i in range(len(dest)):
        stops.append(dest[i])

    origins = stops.copy()
    destinations = stops.copy()
    del destinations[0]
    del origins[-1]

    origins_str = listToUrlString(origins).replace(', ', '+').replace(' ', '+')
    destinations_str = listToUrlString(destinations).replace(', ', '+').replace(' ', '+')
    
    print(data_type)
    print('origins: ', origins_str)
    print('destinations: ', destinations_str)
    url = f'{endpoint}?origins={origins_str}&destinations={destinations_str}&key={api_key}&units=imperial'
    print(url)
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    # return r.json()
    dest_details = {}
    try:
        length_of_rows = len(r.json()['rows'])
        # print(length_of_rows)
        for i in range(length_of_rows):
            row = r.json()['rows'][i]['elements']
            # print('ROW ', i, ' ', row)
            # print(len(row))
            for j in range(len(row)):
                if i == j:
                    print('(i==j): ', row[j]['distance']['text'])
        # dest_details = r.json()['rows'][0]
        # return dest_details
    except:
        pass

print(determine_distance('5112 Gorham Ct, Sacramento, CA', '674 23rd St, Oakland, CA', 'San Francisco, CA', 'Vallejo, CA'))    

# def extract_lat_lng(address_or_postalcode, data_type='json'):
#     endpoint= f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
#     params = {'address': address_or_postalcode, 'key': api_key}
#     url_params = urlencode(params)
#     url = f'{endpoint}?{url_params}'
#     r = requests.get(url)
#     print(url)
#     if r.status_code not in range(200, 299):
#         return {}
#     latlng = {}
#     try:
#         latlng = r.json()['results'][0]['geometry']['location']
#     except:
#         pass
#     return latlng.get('lat'), latlng.get('lng')
#     # return r.json()

# print(extract_lat_lng('1600 Ampitheatre Parkway, Mountain View, CA'))
# to_parse = 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Ampitheatre+Parkway%2C+Mountain+View%2C+CA&key=AIzaSyCNyQlXhkdhJQ4iczZl79qrzPf8EJXhzL8'
# urlparse(to_parse)
# query_string = urlparse(to_parse).query
# print(query_string)
print('Goodbye World')