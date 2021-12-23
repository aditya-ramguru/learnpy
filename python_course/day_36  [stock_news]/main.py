import requests
import datetime as dt
# import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api = "8JHN4CVWFTF2RV9K"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api = "b7bbf21eb65d4e73958ce292b804bd37"
account_sid = 'ACccc504cf132dbb585b78830ac90d9562'
auth_token = '8032487fbe9465d08d824fbd029e51b7'

yesterday_date = dt.date.today() - dt.timedelta(1)
day_before_date = yesterday_date - dt.timedelta(1)

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': stock_api
}

news_parameters = {
    'q': COMPANY_NAME,
    'from': day_before_date,
    'to': dt.date.today(),
    'sortBy': 'popularity',
    'apiKey': news_api
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
opening_price = float(data[str(yesterday_date)]['1. open'])
closing_price = float(data[str(day_before_date)]['4. close'])
percentage = round(((opening_price-closing_price)/closing_price)*100)

significant_change = False

if percentage > 0 or percentage < 0:
    significant_change = True

if percentage > 0:
    percentage = f'🔼{percentage}'
else:
    percentage = f'🔽{percentage}'

if significant_change:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]
    news = {item['title']: item['description'] for item in news_data}
    print(news)
    # proxy_client = TwilioHttpClient()  # rq
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}  # rq
    client = Client(account_sid, auth_token,)  # rq, http_client
    for key in news:
        message = client.messages \
            .create(
            body=f'{STOCK}:{percentage}\n\nHeadline:{key}\n\nBrief:{news[key]}',
            from_='+16165046589',
            to='+918884230038'
        )
        print(message.status)






## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

