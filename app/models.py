from pydantic import BaseModel


class StockInfo(BaseModel):
    symbol: str
    symbolName: str
    lastPrice: float
    priceChange: float
    percentChange: float
    lowPrice: float
    openPrice: float
    highPrice: float
    volume: int


class DetailedStockInfo(BaseModel):
    symbol: str
    symbolName: str
    lastPrice: float
    priceChange: float
    percentChange: float
    bidPrice: float
    askPrice: float
    bidSize: int
    askSize: int
    tradeTime: str
    lastPriceExt: float
    priceChangeExt: float
    percentChangeExt: float
    tradeTimeExt: str
    contractName: str
    daysToContractExpiration: str
    symbolCode: str
    exchange: str
    sicIndustry: str
    symbolRoot: str
    sessionDateDisplayLong: str
    shouldUpdate: bool
    lowPrice: float
    openPrice: float
    highPrice: float
    previousPrice: float
    volume: int
    averageVolume: int
    stochasticK14d: float
    weightedAlpha: float
    priceChange5d: float
    percentChange5d: float
    lowPrice1y: float
    highPrice1y: float


"""
{'symbol': 'TSLA', 'symbolName': 'Tesla Inc', 'symbolType': 1, 'lastPrice': 266.63, 'priceChange': '-7.84', 
'percentChange': -0.0286, 'bidPrice': '267.36', 'askPrice': '267.38', 'bidSize': '100', 'askSize': '400', 
'tradeTime': '12:13 ET', 'lastPriceExt': '271.15', 'priceChangeExt': '-3.24', 'percentChangeExt': -0.0118, 
'tradeTimeExt': '09:30 ET', 'contractName': 'N/A', 'daysToContractExpiration': 'N/A', 'symbolCode': 'STK', 
'exchange': 'NASDAQ', 'sicIndustry': 'Auto - Domestic', 'symbolRoot': 'N/A', 'sessionDateDisplayLong': 'Mon, Sep 18th, 2023', 
'shouldUpdate': True, 'lowPrice': 263.7601, 'openPrice': 271.16, 'highPrice': 271.44, 'previousPrice': 274.39, 
'volume': 58439942, 'averageVolume': 118860445, 'stochasticK14d': 85.95, 'weightedAlpha': 8.7, 'priceChange5d': -5.62, 
'percentChange5d': -0.0205, 'lowPrice1y': 101.81, 'highPrice1y': 313.8}
"""