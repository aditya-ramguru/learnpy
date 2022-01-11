from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver"
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.down = 300
        self.up = 300
        self.up_speed_val = 0
        self.down_speed_val = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        start_button = self.driver.find_element(By.CSS_SELECTOR, '.js-start-test.test-mode-multi')
        start_button.click()
        time.sleep(60)
        btotest = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        btotest.click()
        down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up_speed_val = float(up_speed.text)
        self.down_speed_val = float(down_speed.text)
        if self.up_speed_val < self.up or self.down_speed_val < self.down:
            time.sleep(10)
            self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get(url='https://mobile.twitter.com/i/flow/login')
        time.sleep(10)
        name = self.driver.find_element(By.NAME,'text')
        name.send_keys('pythonsmtp58@gmail.com')
        name.send_keys(Keys.ENTER)
        time.sleep(5)
        verification = self.driver.find_element(By.NAME,'text')
        verification.send_keys('Python_bot58')
        verification.send_keys(Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys('superman2')
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f'@myInternetProvider i was promised a up and down speed of 300 and 300 but i get {self.down_speed_val} and {self.up_speed_val}.')
        time.sleep(2)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(3)
        self.driver.quit()




