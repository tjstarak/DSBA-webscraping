# Instruction how to run scrapers in our project

## 1 Beautiful Soup

- Run full code in Python3 interpreter: ```python3 soup.py```

## 2 Scrapy

- Go into: ```DSBA-webscraping/scrapy/eobuwie```
- Run with -O (capital O): ```scrapy crawl shoes -O output.csv```

- To disable verbose output add ```--nolog```

- If the flag ```LIMIT_PAGES``` is set to ```FALSE``` in the scraper code, an additional parameter can be passed to modify the number of pages scraped: ```scrapy crawl shoes -O output.csv -a pages=500```

## 3 Selenium
For the purpose of the project we use geckodriver for Firefox browser and a neccessary set of packages accordingly, therefore Mozilla Firefox browser is required. Otherwise driver and all packages need to be adjusted to a specific browser.

- Go into:  ```DSBA-webscraping/selenium/selenium.py```
- Locate and replace geckodriver path according to your device  ```gecko_path = '/Users/karolina.szczesna/.Trash/geckodriver'```
- Install Driver  ```driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())```
- Run full code in Python3 interpreter:  ```python3 selenium.py```
