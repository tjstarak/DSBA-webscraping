LIMIT_PAGES = True

from bs4 import BeautifulSoup
import requests
import pandas as pd
from timeit import default_timer as timer

#This part gets number of pages (based on bottom toolbar) or sets it to 100 if parameter above - LIMIT_PAGES is set to True
url = 'https://www.eobuwie.com.pl/damskie.html'
html = requests.get(url).text
bs = BeautifulSoup(html, 'html.parser')

max_page = bs.find_all('a', {'class':'toolbar-bottom__pager-item'})
max = max_page[-2].text

if LIMIT_PAGES:
    last_page = 100
else:
    last_page = int(max)

first_name_list=[]
second_name_list=[]
regular_price_list=[]
special_price_list=[]

#This part iterates through every page to scrap data about shoes
for i in range(1,last_page+1):
    url = 'https://www.eobuwie.com.pl/damskie.html?p=' + str(i)
    html = requests.get(url).text
    bs = BeautifulSoup(html, 'html.parser')

    tags = bs.find_all('ul',{"class":"products-list"})[0].find_all('li')
    
    for tag in tags:
        try:
            first_name = tag.div.a.h2.span.text  
        except:
            first_name = ''
        try:
            second_name = tag.div.a.h2.span.next_sibling.next_sibling.text
        except:
            second_name = ''
        try:
            regular_price = tag.div.a.div.find_next_sibling('div').div.text
        except:
            regular_price = ''
        try:
            special_price = tag.div.a.div.find_next_sibling('div').div.next_sibling.next_sibling.text
        except:
            special_price = ''
        #This part cleans and preprocess the data
        if special_price is not None:
            special_price_list.append(special_price.replace('zł', '').replace(' ', '').replace(',', '.').strip())
        else:
            special_price_list.append(None)
        regular_price_list.append(regular_price.replace('zł', '').replace(' ', '').replace(',', '.').strip())
        first_name_list.append(first_name.strip())
        second_name_list.append(second_name.strip())

d = pd.DataFrame(list(zip(first_name_list,second_name_list,regular_price_list,special_price_list)),columns=['First_name','Second_name','Regular_price','Special_price'])

#This part saves data to csv.
#d.to_csv('shoes.csv')


    
