import requests
import datetime as dt
import smtplib
import time

MY_LAT = 12.977600
MY_LNG = 77.693008
email = 'pythonsmtp@gmail.com'
password = '8884230038'


def is_iss_overhead():
    """checks if iss is overhead"""

    # iss api
    response_iss = requests.get(url='http://api.open-notify.org/iss-now.json')
    response_iss.raise_for_status()

    # iss location
    data_iss = response_iss.json()
    iss_longitude = float(data_iss['iss_position']['longitude'])
    iss_latitude = float(data_iss['iss_position']['latitude'])

    if MY_LAT + 5 >= iss_latitude >= MY_LAT-5 and MY_LNG + 5 >= iss_longitude >= MY_LNG-5:
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }

    # sunrise and sunset
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    # sunrise and sunset in bangalore
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1]
    sunset = data['results']['sunset'].split('T')[1]
    sunrise_hour = int(sunrise.split(':')[0])
    sunset_hour = int(sunset.split(':')[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs='adi34mvp@gmail.com',
                                msg='Subject:LOOK UP!\n\nISS is passing by!')

