import requests
import json
x = "39.7456"
y = "-97.0892"
#x = input("Enter X coordinates: ")
#y = input("Enter Y Coordinates: ")

request = requests.get('https://api.weather.gov/points/' + str(x) + ',' + str(y))
forecast_url = request.json()['properties']['forecast']
request = requests.get(forecast_url)
print(request.json())