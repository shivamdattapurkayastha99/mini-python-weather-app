import requests
import json

city=input("Enter city")
url=f'http://api.weatherapi.com/v1/current.json?key=304471f8cd314496887153943232212&q={city}'
r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])





