##################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas
import datetime as dt

my_email = 'pythonsmtp58@gmail.com'
password = '8884230038'



# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_day = now.day
current_month = now.month
file = pandas.read_csv('birthdays.csv')
month = file['month'].to_list()
day = file['day'].to_list()
is_day = False
for i in day:
    if i == current_day:
        for j in month:
            if j == current_month:
                person_data = file[file['day'] == i].values.flatten().tolist()
                p_name = person_data[0]
                p_email = person_data[1]
                is_day = True

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if is_day:
    template_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    letter = random.choice(template_list)
    with open(f'./letter_templates/{letter}') as letter:
        l1 = letter.read()
        x = l1.replace('[NAME]', f'{p_name}')
        # print(x)
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=p_email, msg=f'Subject:Happy birthday!\n\n'
                                                                          f'{x}')


# 4. Send the letter generated in step 3 to that person's email address.




