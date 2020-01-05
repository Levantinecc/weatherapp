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

print(longitude)
print(latitude)