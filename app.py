import requests

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/equipos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)


from models import Fabricante, Marca, Modelo, Proveedor, Categoria, Equipo, Stock

@app.route("/")
def index():
    return render_template(
        'index.html'
    )

@app.route("/equipos", methods=['GET', 'POST'])
def equipos():
    equipos = Equipo.query.all()
    categorias = Categoria.query.all()
    marcas = Marca.query.all()
    modelos = Modelo.query.all()

    if request.method == 'POST':
        marca_id = request.form['marca']
        modelo_id = request.form['modelo']
        categoria_id = request.form['categoria']
        costo = request.form['costo']
        descripcion = request.form['descripcion']

        marca = Marca.query.get(marca_id)
        modelo = Modelo.query.get(modelo_id)
        categoria = Categoria.query.get(categoria_id)

        nuevo_equipo = Equipo(
            marca=marca,
            modelo=modelo,
            categoria=categoria,
            costo=costo,
            descripcion=descripcion
        )

        db.session.add(nuevo_equipo)
        db.session.commit()

        return redirect(url_for('equipos'))

    return render_template(
        'equipos.html',
        equipos=equipos,
        modelos=modelos,
        categorias=categorias,
        marcas=marcas
    )


@app.route("/equipo/<id>/editar", methods=['GET', 'POST'])
def equipo_editar(id):
    equipo = Equipo.query.get_or_404(id)

    equipos = Equipo.query.all()
    categorias = Categoria.query.all()
    marcas = Marca.query.all()
    modelos = Modelo.query.all()


    if request.method == 'POST':
        equipo.id_marca = request.form['marca']
        equipo.id_modelo = request.form['modelo']
        equipo.id_categoria = request.form['categoria']
        equipo.costo = request.form['costo']
        equipo.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('equipos'))

    return render_template('equipos_edit.html', 
        equipo=equipo,
        categorias=categorias, 
        marcas=marcas,
        modelos=modelos)
    

@app.route("/stock", methods=['GET', 'POST'])
def stock():   
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    marcas = Marca.query.all()
    equipos = Equipo.query.all()
    stocks = Stock.query.all()

    if request.method == 'POST':
        id_equipo = int(request.form['id_equipo'])
        cantidad = int(request.form['cantidad'])
        tipo_movimiento = request.form['tipo_movimiento'] == "True"
        nuevo_stock = Stock(id_equipo=id_equipo, cantidad=cantidad, tipo_movimiento=tipo_movimiento)
        db.session.add(nuevo_stock)
        db.session.commit()
        return redirect(url_for('stock'))

    stock_actual = {}
    for equipo in equipos:
        entradas = 0
        salidas = 0
        for x in equipo.stocks:
            if x.tipo_movimiento:
                entradas += x.cantidad
            else:
                salidas += x.cantidad
        stock_actual[equipo.id] = entradas - salidas


    return render_template('stock.html',
                            equipos=equipos,
                            modelos=modelos, 
                            fabricantes=fabricantes, 
                            marcas=marcas,
                            stock_actual=stock_actual)


@app.route("/categoria", methods=['POST', 'GET'])
def agregarCategoria():   
    categorias = Categoria.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_categoria = Categoria(nombre_categoria=nombre)
        db.session.add(nueva_categoria)
        db.session.commit()
        return redirect(url_for('agregarCategoria'))
    
    return render_template('lista_categorias.html', categorias=categorias)

@app.route("/proveedores", methods=['POST', 'GET'])
def agregarProveedores():   
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        nueva_proveedor = Proveedor(nombre_proveedor=nombre, contacto=contacto)
        db.session.add(nueva_proveedor)
        db.session.commit()
        return redirect(url_for('agregarProveedores'))
    
    return render_template('lista_proveedores.html', proveedores=proveedores)
    
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

    return render_template('lista_modelos.html',
                            modelos=modelos, 
                            fabricantes=fabricantes, 
                            marcas=marcas)


@app.route("/marca/<id>/editar", methods=['GET', 'POST'])
def marca_editar(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        marca.nombre_marca = request.form['nombre']
        db.session.commit()
        return redirect(url_for('agregarMarcas'))

    return render_template('marca_edit.html', marca=marca )

@app.route("/fabricante/<id>/editar", methods=['GET', 'POST'])
def fabricante_editar(id):
    fabricante = Fabricante.query.get_or_404(id)

    if request.method == 'POST':
        fabricante.nombre_fabricante = request.form['nombre']
        fabricante.pais_origen = request.form['pais']
        db.session.commit()
        return redirect(url_for('agregarFabricante'))

    return render_template('fabricante_edit.html', fabricante=fabricante )

@app.route("/categoria/<id>/editar", methods=['GET', 'POST'])
def categoria_editar(id):
    categorias = Categoria.query.get_or_404(id)

    if request.method == 'POST':
        categorias.nombre_categoria = request.form['nombre']
        db.session.commit()
        return redirect(url_for('agregarCategoria'))

    return render_template('categoria_edit.html', categorias=categorias)

@app.route("/proveedor/<id>/editar", methods=['GET', 'POST'])
def proveedor_editar(id):
    proveedores = Proveedor.query.get_or_404(id)

    if request.method == 'POST':
        proveedores.nombre_proveedor = request.form['nombre']
        proveedores.contacto = request.form['contacto']
        db.session.commit()
        return redirect(url_for('agregarProveedores'))

    return render_template('proveedor_edit.html', proveedores=proveedores)


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

