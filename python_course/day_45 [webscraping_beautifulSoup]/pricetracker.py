from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

my_email = 'pythonsmtp58@gmail.com'
password = '8884230038'

amazon_url ='https://www.amazon.in/Sony-PS4-Dualshock-Controller-Green/dp/B0742MXX86/' \
            'ref=sr_1_2?keywords=dual+shock4+controller+ps4&qid=1640955684&sprefix=dual+shock%2Caps%2C302&sr=8-2'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": 'en-US,en;q=0.9',
    "Accept-encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive",
}

response = requests.get(url=amazon_url, headers=headers)
response.raise_for_status()
webpage = response.text
# print(webpage.encode("utf-8"))
soup = BeautifulSoup(webpage, 'lxml')
name_object = soup.find(name='span', id="productTitle").text.strip()
price = soup.find(name='span', class_="a-offscreen")
numerical_price = float(price.text[1:].replace(',',''))
# print(numerical_price)
if numerical_price < 6000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f'Subject:Amazon price alert!\n\n'
                                f'{name_object} is now rupees {numerical_price}\n{amazon_url}'
                            )



