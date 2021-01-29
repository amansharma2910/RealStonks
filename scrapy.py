import requests
from bs4 import BeautifulSoup

class Scrapy:
    def __init__(self, stock: str):
        self.stock = stock.strip().lower()
        self.url = 'https://www.marketwatch.com/investing/stock/' + self.stock + '?mod=over_search'
        
    def getPage(self):
        self.page = requests.get(self.url)
        return self.page
     
    #TODO: Implement method to get the current price
    def getPrice(self):
        page = self.getPage()
        soup = BeautifulSoup(page._content, 'html.parser')
        result = {}
        result['price'] = soup.find("bg-quote", class_="value").text
        result['change'] = soup.find("bg-quote", field_="change").text
        # result['price'] = soup.find("bg-quote", class_="value").text
        # result['price'] = soup.find("bg-quote", class_="value").text

        return result['change']


if __name__ == "__main__":
    aapl = Scrapy('AAPL')
    print(aapl.getPrice())