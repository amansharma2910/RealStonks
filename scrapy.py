import requests
from bs4 import BeautifulSoup

class Scrapy:
    def __init__(self, stock: str):
        self.stock = stock.strip().lower()
        self.url = 'https://www.nasdaq.com/market-activity/stocks/'+self.stock
        
    def getPage(self):
        self.page = requests.get(self.url)
        return self.page
     
    #TODO: Implement method to get the current price
    def getPrice(self, stock: str):
        pass

