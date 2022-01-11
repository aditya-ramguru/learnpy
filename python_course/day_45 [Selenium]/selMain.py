from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url='https://www.python.org/')

# method 1
# upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div')
# text = upcoming_events.text.split('\n')[2:]
# dates = [text[i] for i in range(0, len(text), 2)]
# events = [text[i] for i in range(1, len(text), 2)]
# events = driver.find_elements(By.CSS_SELECTOR,'.medium-widget event-widget last a')
# dict1 = {}
# for i in range(int(len(dates)/2)):
#     dict1[i] = {'time': dates[i], 'event': events[i]}
#
# print(dict1)

# method 2
dates = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last time")
event_dates = []
for item in dates:
    event_dates.append(item.text)


event_name = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last li a")
event_names = []
for item in event_name:
    event_names.append(item.text)


dict2 = {}
for i in range(len(event_names)):
    dict2[i] = {'date': event_dates[i], 'name': event_names[i]}
print(dict2)

driver.quit()