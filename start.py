# all the imports
import sqlite3
from flask import Flask
import os

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='kevin',
    PASSWORD='kevin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
