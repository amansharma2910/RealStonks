# RealStonks
---

API available here: https://rapidapi.com/amansharma2910/api/realstonks

RealStonks is a __REST API__ that scrapes MarketWatch to provide you with __real-time stock prices__ for any NASDAQ-listed stock, along with other parameters like total stock volume, price change and percentage change since last update. 

This API was created and deployed as a part of another Deep Learning project involving time-series analysis, that requires a constant inflow of data in order to detect anomalies and predict future stock performance.

## Technologies Used:
---

* __BeautifulSoup4__: For scraping MarketWatch to fetch the real-time data.
* __Flask-RESTful__: Creating the REST API
* __Heroku__: Deploying the web app
* __RapidAPI__: Analytics and general public availability for the API

## Usage:

The following cURL syntax shows how you can use the API:

```
curl --request GET \
	--url https://realstonks.p.rapidapi.com/{NAME} \
	--header 'x-rapidapi-host: realstonks.p.rapidapi.com' \
	--header 'x-rapidapi-key: {RAPIDAPI-PRIVATE-KEY}'
```

In the above given syntax, replace {NAME} with the ticker/symbol of the stock, and {RAPIDAPI-PRIVATE-KEY} with the private key associated with your RapidAPI account.

The example given below shows the working of the API, where we use the API to get the stock info for Tesla (ticker = TSLA) stocks.

```
curl --request GET \
	--url https://realstonks.p.rapidapi.com/TSLA \
	--header 'x-rapidapi-host: realstonks.p.rapidapi.com' \
	--header 'x-rapidapi-key: d9871d1847mshf384f100123cac5p17318djsn1030616ebfff'
```

Example output:

```
{
  "price":788
  "change_point":-5.53
  "change_percentage":-0.7
  "total_vol":"34.99M"
}
```

Head over to https://rapidapi.com/amansharma2910/api/realstonks to test the API and see examples in other programming languages.
