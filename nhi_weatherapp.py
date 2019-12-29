import requests
import json

x = 39.7456
y = -97.0892

#x = input("Enter first coordinate : ")
#y = input("Enter second coordinate : ")

response = requests.get("https://api.weather.gov/points/" + str(x) + ',' + str(y))
print(response.json())
forecast_url = response.json()['properties']['forecast']
print(forecast_url)
requests = requests.get(forecast_url)
print(requests.json())