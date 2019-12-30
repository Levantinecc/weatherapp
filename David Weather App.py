import requests
import json
x = 39.7456
y = -97.0892
#x = input('First Coordinate: ')
#y = input('Second Coordinate: ')
r = requests.get('https://api.weather.gov/points/' + str(x) + ',' + str(y))
#print(r.json()['properties']['forecast']) - used to check if the data is worked
weather = r.json()['properties']['forecast']
output = requests.get(weather)
#print(output.json()['properties']['periods']) - used to check if logic works
for forecast in output.json()['properties']['periods']:
    if  forecast['isDaytime'] == True:
        print(forecast['name'])
        print('current temperature'+ ' ' + str(forecast['temperature'])+' '+forecast['temperatureUnit'])
        print(forecast['detailedForecast'])
        print('')
    else:
        continue

    #print(forecast['name'])

