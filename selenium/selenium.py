from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import time
from timeit import default_timer as timer

start = timer()

# init
gecko_path = '/Users/karolina.szczesna/.Trash/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False

# creating empty dataframe
first_name_list = []
second_name_list = []
price_list = []

LIMIT_PAGES = False

# setting range of subpages to scrape 100 in total subpages from main url 
for page in range(0, 101):

    url = "https://www.eobuwie.com.pl/damskie.html?p=" + str(page)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)

    time.sleep(3)

    # accepting cookies
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div/div[2]/button[1]'))).click()
    except:
        pass
    time.sleep(3)

    # extracting first names of shoes on the page; first names include two parts:
    # 1) 1st word indicates the category of shoes e.g. sneakers, flip-flops etc.
    # 2) 2nd, 3rd, 4th words describe the brand of shoes of certain category.
    first_names = driver.find_elements(By.CLASS_NAME, 'products-list__name-first')
    for name in first_names:
        try:
            first_name = name.text
            print(first_name)
        except:
            pass
        first_name_list.append(first_name.strip())

    # extracting second names of shoes, which are ID's of each product on webpage
    second_names = driver.find_elements(By.CLASS_NAME, 'products-list__name-second')
    for id in second_names:
        try:
            second_name = id.text
            print(second_name)
        except:
            pass
        second_name_list.append(second_name.strip())

    # extracting all prices for shoes (regular price, special price and regular price in case of discount)
    prices = driver.find_elements(By.CLASS_NAME, 'products-list__price-box')
    for i in prices:
        try:
            price = i.text
            print(price)
        except:
            pass
        price_list.append(price.replace('zł', '').replace(' ', '').replace(',', '.').replace('\n', ',').strip())

# putting data from lists into dataframe
d = pd.DataFrame({
    'First name': first_name_list,
    'Second name': second_name_list,
    'Regular price': price_list
})

# closing driver's actions on a webpage
driver.close()

# dataframe transformations
# adding new column for shoes special price in case of a discount (lower price than the regular one) and spliting prices to two columns
d[['Regular price','Special price']] = d['Regular price'].str.split(',', expand=True)

end = timer()
print(end - start)

# saving data to csv
d.to_csv('shoes.csv')
