from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Init:
gecko_path = '/Users/karolina.szczesna/.Trash/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)

url = 'https://www.eobuwie.com.pl/damskie.html'

LIMIT_PAGES = False

def __init__(self, pages=500, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if LIMIT_PAGES:
        self.pages = 100
    else:
        self.pages = pages

driver.get(url)
time.sleep(5)

# Accepting cookies
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div/div[2]/button[1]'))).click()
time.sleep(5)

# Actual program:
# Extracting first names of shoes on the page. First names include two parts:
# 1) 1st word indicates the category of shoes e.g. sneakers, flip-flops etc.
# 2) 2nd, 3rd, 4th words describe the brand of shoes of certain category.
first_names = driver.find_elements(By.CLASS_NAME, 'products-list__name-first')
for name in first_names:
    try:
        first_name = name.text
        print(first_name)
    except:
        pass

# Extracting second names of shoes, which are ID's of each product on webpage.
second_names = driver.find_elements(By.CLASS_NAME, 'products-list__name-second')
for id in second_names:
    try:
        second_name = id.text
        print(second_name)
    except:
        pass

print(#####)

# Extracting regular prices for shoes, which are not on sale.
regular_prices = driver.find_elements(By.CLASS_NAME, 'products-list__regular-price')
for i in regular_prices:
    try:
        regular_price = i.text
        print(regular_price)
    except:
        pass

# Extracting old prices for shoes, which are currently on sale.
old_prices = driver.find_elements(By.CLASS_NAME, 'products-list__regular-price')
for ii in old_prices:
    try:
        old_price = ii.text
        print(old_price)
    except:
        pass

# Extracting special prices for shoes, which are currently on sale.
special_prices = driver.find_elements(By.CLASS_NAME, 'products-list__special-price')
for iii in special_prices:
    try:
        special_price = iii.text
        print(special_price)
    except:
        pass
