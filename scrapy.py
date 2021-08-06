import re
import requests
from bs4 import BeautifulSoup

class Scrapy:
    def __init__(self, stock: str):
        self.stock = stock.strip().lower()
        self.url = 'https://www.marketwatch.com/investing/stock/' + self.stock + '?mod=quote_search'
        
    def getPage(self):
        self.page = requests.get(self.url)
        return self.page
     
    def getPrice(self):
        page = self.getPage()
        soup = BeautifulSoup(page._content, 'html.parser')
        result = {}
        result['price'] = float("".join(soup.find("h2", {"class": "intraday__price"}).find(class_="value").text.split(",")))
        result['change_point'] = float("".join(soup.find("span", {"class": "change--point--q"}).text.split(",")))
        result['change_percentage'] = float(soup.find("span", {"class": "change--percent--q"}).text[:-1])
        result['total_vol'] = re.search(r"\d+[.]*\d*[a-zA-Z]*", soup.find("div", {"class": "range__header"}).find("span", {"class": "primary"}).text).group()

        return result
        


if __name__ == "__main__":
    tsla = Scrapy('TSLA')
    print(tsla.getPrice())