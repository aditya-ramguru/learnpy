import requests
import os    # rq
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient  #rq

# rq = required to run in pythonanywhere found the extra stuff in google.

api_key = 'afc47202adc94044dd1b39385527c870'
account_sid = 'ACccc504cf132dbb585b78830ac90d9562'
auth_token = '8032487fbe9465d08d824fbd029e51b7'

parameters = {
    'lat': 4.938000,
    'lon': -52.335049,
    'exclude': 'current,minutely,daily',
    'appid': api_key,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()['hourly']
weather_id = [item['weather'][0]['id'] for item in weather_data]
weather_id_12 = weather_id[:12]

will_rain = False
for item in weather_id_12:
    if item < 600:
        will_rain = True

# noinspection PyUnboundLocalVariable
if will_rain:
    proxy_client = TwilioHttpClient() # rq
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}  # rq

    client = Client(account_sid, auth_token, http_client=proxy_client)  # rq, http_client
    message = client.messages \
        .create(
        body="it is going to rain today bring an umbrella!",
        from_='+16165046589',
        to='+918884230038'
    )
    print(message.status)

# env
# export {variable name}= the api id or number with no quotes
# import os
# os.environ.get('{variable name}')

