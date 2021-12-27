import requests
from datetime import datetime

NUTRITIONX_API_ID = '9357bc0b'
NUTRITIONX_API_KEY = '8ae55d3627eddf242829f0f121f120ed'
NUTRITIONX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/bf5d8afbe2f141875718715b54479390/"workoutTracking"/workouts'

exercise_text = input('Tell me which exercises you did: ')
headers = {
    'x-app-id': NUTRITIONX_API_ID,
    'x-app-key': NUTRITIONX_API_KEY,
    'Content-Type': 'application/json'
}

nutriotionix_parameters = {
    'query': exercise_text,
    'gender': 'Male',
    'weight_kg': 75,
    'height_cm': 180,
    'age': 18,
}

response = requests.post(url=NUTRITIONX_ENDPOINT, json=nutriotionix_parameters, headers=headers)
response.raise_for_status()
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime('%X')


# basic authentication
# sheet_response = requests.post(url,json,auth=(username,password))
# bearer authentication
sheety_header = {
    "authorization": "Bearer kfajf;Iahf284u210R"
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_header)
    print(sheet_response.text)


