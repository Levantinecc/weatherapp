import requests
import mysql.connector

cityName = "San Jose"
State = "CA"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="weather"
)
mycursor = mydb.cursor()
mycursor.execute('SELECT lat, lng FROM weather.uscities where city = "' +cityName +'" AND state_id = "' + State+'";')
myresult = mycursor.fetchall()

for x in myresult:
  longitude=(x[0])
  latitude=(x[1])

response = requests.get("https://api.weather.gov/points/" + str(longitude) + ',' + str(latitude))
print(response.json())
forecast_url = response.json()['properties']['forecast']
requests = requests.get(forecast_url)
detail_forecast = requests.json()['properties']['periods']

for n in detail_forecast:
    if n['isDaytime'] == True:
        print("====For ", n['name'], " ", n['startTime'], "=====")
        print("Temperature is: ", n['temperature'])
        print("Predicted forecast: ", n['detailedForecast'])
        print("")