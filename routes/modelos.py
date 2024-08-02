from flask import Blueprint, render_template, redirect, request, url_for
from app import db
from models import Fabricante, Marca, Modelo, Categoria

modelos_bp = Blueprint('modelos', __name__)

@modelos_bp.route("/modelos", methods=['POST', 'GET'])
def agregar_modelo():   
    modelos = Modelo.query.all() 
    fabricantes = Fabricante.query.all()  
    marcas = Marca.query.all() 
    categorias = Categoria.query.all() 

    if request.method == 'POST':
        nombre_modelo = request.form['modelo']
        id_fabricante = int(request.form['id_fabricante'])
        id_marca = int(request.form['id_marca'])
        id_categoria = int(request.form['id_categoria'])
        nuevo_modelo = Modelo(nombre_modelo=nombre_modelo, id_fabricante=id_fabricante, id_marca=id_marca, id_categoria = id_categoria )
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('modelos.agregar_modelo'))

    return render_template('lista_modelos.html', modelos=modelos, fabricantes=fabricantes, marcas=marcas, categorias=categorias)

@modelos_bp.route("/modelo/<id>/borrar", methods=['GET', 'POST'])
def modelo_borrar(id):
    modelo = Modelo.query.get_or_404(id)

    db.session.delete(modelo)
    db.session.commit()

    return redirect(url_for('modelos.agregar_modelo'))

@modelos_bp.route("/modelo/<int:id>/editar", methods=['GET', 'POST'])
def modelo_editar(id):
    fabricantes = Fabricante.query.all()
    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    modelo = Modelo.query.get_or_404(id)

    if request.method == 'POST':
        modelo.nombre_modelo = request.form['modelo']
        modelo.id_fabricante = int(request.form['id_fabricante'])
        modelo.id_marca = int(request.form['id_marca'])
        modelo.id_categoria = int(request.form['categoria'])
        db.session.commit()
        return redirect(url_for('modelos.agregar_modelo'))

    return render_template('modelo_edit.html', modelo=modelo, categorias=categorias, fabricantes=fabricantes, marcas=marcas)