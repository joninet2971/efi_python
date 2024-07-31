from flask import Blueprint, render_template, redirect, request, url_for
from models import Marca
from app import db

marcas_bp = Blueprint('marcas', __name__)

@marcas_bp.route("/marcas", methods=['POST', 'GET'])
def agregar_marcas():   
    marcas = Marca.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_marca = Marca(nombre_marca=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for('marcas.agregar_marcas'))
    
    return render_template('lista_marcas.html', marcas=marcas)

@marcas_bp.route("/marca/<id>/editar", methods=['GET', 'POST'])
def marca_editar(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        marca.nombre_marca = request.form['nombre']
        db.session.commit()
        return redirect(url_for('marcas.agregar_marcas'))

    return render_template('marca_edit.html', marca=marca)