import requests

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/equipos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import *

print("Modelos cargados:")
print(db.Model.metadata.tables.keys())


@app.route("/")
def index():
    return render_template(
        'index.html'
    )

@app.route("/equipos")
def equipos():
    return render_template(
        'equipos.html'
    )

@app.route("/stock")
def stock():
    return render_template(
        'stock.html'
    )