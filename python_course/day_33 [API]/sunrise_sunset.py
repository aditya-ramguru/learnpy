import requests
import datetime as dt

MY_LAT = 12.953880
MY_LNG = 12.953880

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1]
sunset = data['results']['sunset'].split('T')[1]
sunrise_hour = sunrise.split(':')[0]
sunset_hour = sunset.split(':')[0]


now = dt.datetime.now().hour
print(now)
print(sunrise_hour)
print(sunset_hour)