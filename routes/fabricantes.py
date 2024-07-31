from flask import Blueprint, render_template, redirect, request, url_for
from models import Fabricante
from app import db

fabricantes_bp = Blueprint('fabricantes', __name__)

@fabricantes_bp.route("/fabricantes", methods=['POST', 'GET'])
def agregar_fabricante():   
    fabricantes = Fabricante.query.all()

    if request.method == 'POST':
        nombre_fabricante = request.form['nombre_fabricante']
        pais_origen = request.form['pais_origen']
        nuevo_fabricante = Fabricante(nombre_fabricante=nombre_fabricante, pais_origen=pais_origen)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('fabricantes.agregar_fabricante'))

    return render_template('lista_fabricantes.html', fabricantes=fabricantes)

@fabricantes_bp.route("/fabricante/<id>/editar", methods=['GET', 'POST'])
def fabricante_editar(id):
    fabricante = Fabricante.query.get_or_404(id)

    if request.method == 'POST':
        fabricante.nombre_fabricante = request.form['nombre']
        fabricante.pais_origen = request.form['pais']
        db.session.commit()
        return redirect(url_for('fabricantes.agregar_fabricante'))

    return render_template('fabricante_edit.html', fabricante=fabricante)