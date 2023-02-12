import requests
from shapely.geometry import Polygon, Point
from rtree import index
import reverse_geocoder as rg
geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
data = requests.get(geo_request_url).json()
print(data['latitude'])
print(data['longitude'])
latitude = data['latitude']
longitude = data['longitude']
print(data)
print("https://www.google.co.jp/maps/@"+latitude+","+longitude+",14z")

coordinates = (latitude,longitude)

results = rg.search(coordinates) # default mode = 2

print (results)