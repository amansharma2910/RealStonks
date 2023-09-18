from fastapi import FastAPI, Request
from fastapi import Response

from app.models import StockInfo
from app.scraper import PageFormatChangedException, Scraper, UrlNotFoundException

app = FastAPI()


@app.get("/")
def server_check(request: Request):
    return Response(content=f"Hello from RealStonks!\nHead over to {str(request.url).rstrip('/')}/docs for more information.", status_code=200)


@app.get("/stocks/{symbol}", response_model=StockInfo)
def get_stock_info(symbol: str, request: Request):
    try:
        res = Scraper.get_stock_info(symbol)
        return StockInfo(**res)
    except UrlNotFoundException:
        return Response(content=f"Invalid stock symbol. Kindly ensure the ticker symbol is a valid NASDAQ-listed stock.", status_code=404)
    except PageFormatChangedException:
        # todo: implement API break alert using slack or email
        return Response(content=f"Internal server error", status_code=500)
    except Exception as e:
        return Response(content=f"Internal server error", status_code=500)
    
