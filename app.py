import requests

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/equipos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import *

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
    
@app.route("/crear_marcas", methods=['POST', 'GET'])
def agregarMarcas():   
    marcas = Marca.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_marca = Marca(nombre_marca=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for('agregarMarcas'))

    return render_template('crear_marcas.html', marcas=marcas)