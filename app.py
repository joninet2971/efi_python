import requests

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/equipos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)


from models import Fabricante, Marca, Modelo

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
    
@app.route("/cargar", methods=['POST', 'GET'])
def agregarMarcas():   
    marcas = Marca.query.all()
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        if 'nombre' in request.form:
            nombre = request.form['nombre']
            nueva_marca = Marca(nombre_marca=nombre)
            db.session.add(nueva_marca)
            db.session.commit()
            return redirect(url_for('agregarMarcas'))
        elif 'nombre_fabricante' in request.form and 'pais_origen' in request.form:
            nombre_fabricante = request.form['nombre_fabricante']
            pais_origen = request.form['pais_origen']
            nuevo_fabricante = Fabricante(nombre_fabricante=nombre_fabricante, pais_origen=pais_origen)
            db.session.add(nuevo_fabricante)
            db.session.commit()
            return redirect(url_for('agregarMarcas'))
        elif 'modelo' in request.form and 'id_fabricante' in request.form and 'id_marca' in request.form:
            nombre_modelo = request.form['modelo']
            id_fabricante = int(request.form['id_fabricante'])
            id_marca = int(request.form['id_marca'])
            nuevo_modelo = Modelo(nombre_modelo=nombre_modelo, id_fabricante=id_fabricante, id_marca=id_marca)
            db.session.add(nuevo_modelo)
            db.session.commit()
            return redirect(url_for('agregarMarcas'))

    return render_template('cargar.html', marcas=marcas, modelos=modelos, fabricantes=fabricantes)
