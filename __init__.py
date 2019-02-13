import sqlite3
import markdown
import os

import click
from flask import current_app, g
from flask.cli import with_appcontext

#import framework
from flask import Flask, g

#create instance
app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    #Open the README file
    with open(os.path.dirname(app.root_path) + 'README.md', 'r') as markdown_file:
       #Read content of file
        content = markdown_file.read()
        #Convert to HTML
        return markdown.markdown(content)


class StockList(Resource):
       def get(self):
              shelf = get_db()
              keys = list(shelf.keys())

              stocks = []

              for key in stocks:
                     stock.append(shelf[key])

              return {'message': 'Success', 'data': devices}, 200
       def post(self):
              parser = reqparse.RequestParser()

              parser.add_argument('ticker', required=True)
              parser.add_argument('stock', required=True)
              parser.add_argument('index', required=True)
              parser.add_argument('last-price', required=True)


              args = parser.parse_args()

              shelf = get_db()
              shelf[args['ticker']] = args
              
              return {'message': 'Stock Registered', 'data': args}, 201

class Stock(resource):
       def get(self, ticker):
              shelf = get_db()

              if not (ticker in shelf):
                     return {'message': 'Stock not found', 'data':{}}, 404
              return {'message': 'Stock found', 'data': shelf[ticker]}, 200

       def delete(self, ticker):
              shelf = get_db()

              if not (ticker in shelf):
                     return {'message': 'Stock not found', 'data':{}}, 404

              del shelf[ticker]
              return '', 204

api.add_resource(StockList, '/stocks')
api.add_resource(Stock, '/stocks/<string:ticker>')