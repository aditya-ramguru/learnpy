from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time


class InstaFollower:
    def __init__(self,username,password,similar_account):
        chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver"
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.username = username
        self.password = password
        self.simaccount = similar_account

    def login(self):
        self.driver.get(url='https://www.instagram.com/')
        time.sleep(5)
        user = self.driver.find_element(By.NAME, 'username')
        user.send_keys(self.username)
        time.sleep(5)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(self.password)
        time.sleep(5)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_in.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(url=f'https://www.instagram.com/{self.simaccount}/')
        time.sleep(5)
        following = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        time.sleep(60)
        element_inside = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]/ul/div/li[13]/div/div[1]/div[2]/div[1]/span')
        element_inside.send_keys(Keys.END)


    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, '.sqdOP.L3NKy.y3zKF')
        for button in buttons:
            try:
               button.click()
            except ElementClickInterceptedException:
                continue