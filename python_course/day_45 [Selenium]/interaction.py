from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.get(url='https://en.wikipedia.org/wiki/Main_Page')
#
# articles = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
# articles.click()
# all_portal = driver.find_element(By.LINK_TEXT, 'All portals')
# all_portal.click()
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
driver.get(url='http://secure-retreat-92358.herokuapp.com/')
fname = driver.find_element(By.NAME,'fName')
fname.send_keys('Aditya')

lname = driver.find_element(By.NAME, 'lName')
lname.send_keys('Ramguru')

email = driver.find_element(By.NAME, 'email')
email.send_keys('aditya.ramguru@gmail.com')

sign_up = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-block')
sign_up.click()