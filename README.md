# Instruction how to run scrapers in our project

## 1 Beautiful Soup

- Run full code in Python3 interpreter: ```python3 soup.py```

## 2 Scrapy

- Go into: ```DSBA-webscraping/scrapy/eobuwie```
- Run with -O (capital O): ```scrapy crawl shoes -O output.csv```

- To disable verbose output add ```--nolog```

- If the flag ```LIMIT_PAGES``` is set to ```FALSE``` in the scraper code, an additional parameter can be passed to modify the number of pages scraped: ```scrapy crawl shoes -O output.csv -a pages=500```

## 3 Selenium
