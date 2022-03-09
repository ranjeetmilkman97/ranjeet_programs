from urllib import response
import requests

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']-273)

    print ("Weather:", weather)
    print("Temperature: " + str(temperature) + "C")

else:
    print("Error with code: %s" %(response.status_code))

