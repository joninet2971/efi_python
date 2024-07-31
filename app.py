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
    
@app.route("/marcas", methods=['POST', 'GET'])
def agregarMarcas():   
    marcas = Marca.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_marca = Marca(nombre_marca=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for('agregarMarcas'))
    
    return render_template('lista_marcas.html', marcas=marcas)

@app.route("/fabricantes", methods=['POST', 'GET'])
def agregarFabricante():   
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        nombre_fabricante = request.form['nombre_fabricante']
        pais_origen = request.form['pais_origen']
        nuevo_fabricante = Fabricante(nombre_fabricante=nombre_fabricante, pais_origen=pais_origen)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('agregarFabricante'))

    return render_template('lista_fabricantes.html', fabricantes=fabricantes)

@app.route("/modelos", methods=['POST', 'GET'])
def agregarModelo():   
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    marcas = Marca.query.all()

    if request.method == 'POST':
        nombre_modelo = request.form['modelo']
        id_fabricante = int(request.form['id_fabricante'])
        id_marca = int(request.form['id_marca'])
        nuevo_modelo = Modelo(nombre_modelo=nombre_modelo, id_fabricante=id_fabricante, id_marca=id_marca)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('agregarModelo'))

    return render_template('lista_modelos.html', modelos=modelos, fabricantes=fabricantes, marcas=marcas)


@app.route("/marca/<id>/editar", methods=['GET', 'POST'])
def marca_editar(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        marca.nombre_marca = request.form['nombre']
        db.session.commit()
        return redirect(url_for('agregarMarcas'))

    return render_template('marca_edit.html', marca=marca )


@app.route("/modelo/<id>/borrar", methods=['GET', 'POST'])
def marca_borrar(id):
    modelo = Modelo.query.get_or_404(id)

    db.session.delete(modelo)
    db.session.commit()

    return redirect(url_for('agregarModelo'))

@app.route("/modelo/<id>/editar", methods=['GET', 'POST'])
def modelo_editar(id):
    fabricantes = Fabricante.query.all()
    marcas = Marca.query.all()
    modelo = Modelo.query.get_or_404(id)

    if request.method == 'POST':
        modelo.nombre_modelo = request.form['modelo']
        modelo.id_fabricante = int(request.form['id_fabricante'])
        modelo.id_marca = int(request.form['id_marca'])
        db.session.commit()
        return redirect(url_for('agregarModelo'))

    return render_template('modelo_edit.html', fabricantes=fabricantes, marcas=marcas)

