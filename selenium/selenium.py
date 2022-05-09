## to be edited!

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass
import datetime

# Init:
gecko_path = '/Users/karolina.szczesna/.Trash/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)

url = 'https://www.eobuwie.com.pl/'

LIMIT_PAGES = False

def __init__(self, pages=500, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if LIMIT_PAGES:
        self.pages = 100
    else:
        self.pages = pages

# Actual program:
driver.get(url)

#time.sleep(5)

omit_cookies = driver.find_element(By.XPATH, '//button[@type="button"]')
omit_cookies.click()

time.sleep(5)

#omit_ad = driver.find_element(By.XPATH, '/html/body/aside/div/button')
#omit_ad.click()

#damskie = driver.find_element(By.XPATH, '/html/body/header/nav/ul/li[2]/a')
#damskie.click()

damskie = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.eobuwie.com.pl/damskie.html']").click()))

time.sleep(5)

#chat = driver.find_element(By.XPATH, '/html/body/div[1]/div/aside[1]/div/div[1]/ul[1]/li[2]/button')
#chat.click()

#time.sleep(5)

#bot_test_chat = driver.find_element(By.XPATH, '/html/body/div[1]/div/aside[2]/div[3]/ul[1]/li[3]/div[2]/h5')
#bot_test_chat.click()

#time.sleep(5)

#element = driver.find_element(By.XPATH, '//div/button/input[@type="file"]')
#element.send_keys("/Users/karolina.szczesna/Desktop/its.py")

#time.sleep(0.3)
