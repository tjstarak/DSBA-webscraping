from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time

# init:
gecko_path = '/Users/karolina.szczesna/.Trash/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False

first_name_list=[]
second_name_list=[]
regular_price_list=[]
special_price_list=[]
old_price_list=[]

LIMIT_PAGES = False

#if LIMIT_PAGES:
    #last_page = 100
#else:
    #last_page = int(max)

for page in range(1, 3):

    url = "https://www.eobuwie.com.pl/damskie.html?p=" + str(page)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)

    time.sleep(5)

    # accepting cookies
    WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div/div[2]/button[1]'))).click()
    time.sleep(5)

    # extracting first names of shoes on the page. First names include two parts:
    # 1) 1st word indicates the category of shoes e.g. sneakers, flip-flops etc.
    # 2) 2nd, 3rd, 4th words describe the brand of shoes of certain category.
    first_names = driver.find_elements(By.CLASS_NAME, 'products-list__name-first')
    for name in first_names:
        try:
            first_name = name.text
            print(first_name)
        except:
            pass

    # extracting second names of shoes, which are ID's of each product on webpage.
    second_names = driver.find_elements(By.CLASS_NAME, 'products-list__name-second')
    for id in second_names:
        try:
            second_name = id.text
            print(second_name)
        except:
            pass

    # extracting regular prices for shoes, which are not on sale.
    regular_prices = driver.find_elements(By.CLASS_NAME, 'products-list__regular-price')
    for i in regular_prices:
        try:
            regular_price = i.text
            print(regular_price)
        except:
            pass

    # extracting old prices for shoes, which are currently on sale.
    old_prices = driver.find_elements(By.CLASS_NAME, 'products-list__regular-price')
    for ii in old_prices:
        try:
            old_price = ii.text
            print(old_price)
        except:
            pass

    # extracting special prices for shoes, which are currently on sale.
    special_prices = driver.find_elements(By.CLASS_NAME, 'products-list__special-price')
    for iii in special_prices:
        try:
            special_price = iii.text
            print(special_price)
        except:
            pass

    if special_prices is not None:
        special_price_list.append(special_prices.replace('zł', '').replace(' ', '').replace(',', '.').strip())
    else:
        special_price_list.append(None)

    regular_price_list.append(regular_prices.replace('zł', '').replace(' ', '').replace(',', '.').strip())
    old_price_list.append(old_prices.replace('zł', '').replace(' ', '').replace(',', '.').strip())
    first_name_list.append(first_names.strip())
    second_name_list.append(second_names.strip())

#d = pd.DataFrame(list(zip(first_name_list,second_name_list,regular_price_list,special_price_list)),columns=['First_name','Second_name','Regular_price','Special_price'])
print(d)

driver.close()
