import requests
import datetime as dt

PIXELA_END = 'https://pixe.la/v1/users'
USERNAME = "adityaramguru"
TOKEN = "k342h3rvbq3wiyrg"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# user creation
# response = requests.post(url=PIXELA_END, json=user_parameters)
# print(response.text)


graph_endpoint = f'{PIXELA_END}/{USERNAME}/graphs'

graph_parameters = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# for graph
# response1 = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response1.text)

# any_day = dt(year=2021, month=7, day=23)
today = dt.date.today()

posting_parameters = {
    "date": today.strftime("%Y%m$d"),
    "quantity": '10.5',
}

posting_pixel_endpoint = f'{graph_endpoint}/{graph_parameters["id"]}'

# posting a pixel
# response2 = requests.post(url=posting_pixel_endpoint, headers=headers, json=posting_parameters)
# print(response2.text)

yesterday = today - dt.timedelta(1)
update_endpoint = f"{graph_endpoint}/{yesterday}"

updating_parameter = {
    "quantity": "4.5"
}

response3 = requests.put(url=update_endpoint, json=updating_parameter, headers=headers)

# same for delete
# just put requests.delete(url,json,header
