import requests
import json
x = "39.7456"
y = "-97.0892"
#x = input("Enter X coordinates: ")
#y = input("Enter Y Coordinates: ")

request = requests.get('https://api.weather.gov/points/' + str(x) + ',' + str(y))
forecast_url = request.json()['properties']['forecast']
request = requests.get(forecast_url)
for days in request.json()['properties']['periods']:
    if days['isDaytime'] != True:
        continue
    print(" ====== For " + days['name'] + " " + days['startTime'] + " ======")
    print("The Current temperature is: " + str(days['temperature']) + "F")
    print(days['detailedForecast'])
    print("        ")