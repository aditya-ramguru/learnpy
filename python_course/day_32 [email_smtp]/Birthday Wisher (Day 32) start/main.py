import smtplib
import datetime as dt
import random

my_email = 'pythonsmtp58@gmail.com'
password = '8884230038'
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open(file='quotes.txt', mode='r') as file:
        quote_list = file.readlines()
        quote = random.choice(quote_list)
    print(quote)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()  # makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f'Subject:motivation\n\n'
                                f'{quote}'
                            )

