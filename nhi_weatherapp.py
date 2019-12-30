import requests
import json

x = 39.7456
y = -97.0892
#x = input("Enter first coordinate : ")
#y = input("Enter second coordinate : ")

response = requests.get("https://api.weather.gov/points/" + str(x) + ',' + str(y))
print(response.json())
forecast_url = response.json()['properties']['forecast']
#print(forecast_url)
requests = requests.get(forecast_url)
#print(requests.json())
detail_forecast = requests.json()['properties']['periods']
#print(detail_forecast)

for n in detail_forecast:
    if n['isDaytime'] == True:
        print("====For ", n['name'], " ", n['startTime'], "=====")
        print("Temperature is: ", n['temperature'])
        print("Predicted forecast: ", n['detailedForecast'])
        print("")

#temperature = requests.json()['properties']['periods']['temperature']

#detailedForecast = requests.json()['properties']['periods']['detailedForecast']


