import ast
import json
import cloudscraper
from bs4 import BeautifulSoup

from app.utils import bulk_convert_percent_string_to_float


class UrlNotFoundException(Exception):
    pass


class PageFormatChangedException(Exception):
    pass


class Scraper:
    url = "https://www.barchart.com/stocks/quotes/{symbol}/overview"
    scraper = cloudscraper.create_scraper(delay=5)


    @classmethod   
    def get_page_html(cls, symbol: str):
        symbol = symbol.strip().upper()
        symbol_url = cls.url.format(symbol=symbol)
        res = cls.scraper.get(symbol_url)

        if res.status_code != 200:
            raise UrlNotFoundException(f"Url not found for {symbol}")
        
        page_html = BeautifulSoup(res._content, 'html5lib')
        
        return page_html
    

    @classmethod
    def scrap_page(cls, html: BeautifulSoup):
        try:
            main_element = html.find('main', class_="off-canvas-wrap")
            data_column = main_element.find("div", class_="inner-wrap")\
                            .find("div", class_="main-content-wrapper")\
                                .find("div", class_="row").find("div", class_="large-12 columns")\
                                    .find("div", class_="two-column-block").find("div", class_="row")\
                                        .find("div", class_="small-12 columns main-column")\
                                            .find("div", class_="column-inner")
        
            stock_info = json.loads(data_column.find("div", class_="page-title")["data-ng-init"].lstrip("init(").rstrip(")"))

            stock_metrics = ast.literal_eval(data_column.find("div", class_="bc-quote-overview")["data-ng-init"].lstrip("init(").rstrip(")"))[3].get("raw")        
            stock_info.update(stock_metrics)

            stock_info = bulk_convert_percent_string_to_float(stock_info, ["percentChange", "percentChangeExt"])
            return stock_info
        except:
            raise PageFormatChangedException(f"Kindly check the HTML format.")


    @classmethod
    def get_stock_info(cls, symbol: str):
        try:
            html = cls.get_page_html(symbol=symbol)
            stock_info = cls.scrap_page(html=html)
            return stock_info
        
        except Exception as e:
            raise e


if __name__ == "__main__":
    res = Scraper.get_stock_info('w')
    print(res)