import json
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

from scrapy import Scrapy

#TODO: Implement the API methods
app = Flask(__name__)
api = Api(app=app)

class Stock(Resource):
    def get(self, name: str):
        if name:
            try:
                stock = Scrapy(stock=name)
                return json.dumps(stock.getPrice()), 200
            except:
                return "Invalid Stock Ticker", 404
        return "Bad Request: Provide Stock Ticker", 400

api.add_resource(Stock, "/<string:name>")

if __name__ == '__main__':
    app.run(debug=False)
