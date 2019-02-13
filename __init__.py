import sqlite3
import markdown
import os

import click
from flask import current_app, g
from flask.cli import with_appcontext

#import framework
from flask import flask, g

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


