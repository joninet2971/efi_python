from flask import Blueprint, render_template, redirect, request, url_for, jsonify
from models import Equipo, Categoria, Marca, Modelo

from app import db

equipos_bp = Blueprint('equipos', __name__)

@equipos_bp.route("/equipos", methods=['GET', 'POST'])
def equipos():
    equipos = Equipo.query.filter_by(activo=True).all()
    
    categorias = Categoria.query.all()
    marcas = Marca.query.all()
    modelos = Modelo.query.all()

    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        costo = float(request.form['costo'])
        descripcion = request.form['descripcion']

        nuevo_equipo = Equipo(
            id_marca=marca,
            id_modelo=modelo,
            costo=costo,
            descripcion=descripcion
        )

        db.session.add(nuevo_equipo)
        db.session.commit()

        return redirect(url_for('equipos.equipos'))
   
    return render_template(
        'equipos.html',
        equipos=equipos,
        modelos=modelos,
        categorias=categorias,
        marcas=marcas
    )

@equipos_bp.route("/equipo/<id>/editar", methods=['GET', 'POST'])
def equipo_editar(id):
    equipo = Equipo.query.get_or_404(id)

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
        return redirect(url_for('equipos.equipos'))

    return render_template('equipos_edit.html', 
        equipo=equipo,
        categorias=categorias, 
        marcas=marcas,
        modelos=modelos)

@equipos_bp.route("/equipo/<id>/borrar", methods=['GET', 'POST'])
def equipo_borrar(id):
    equipo = Equipo.query.get_or_404(id)

    db.session.delete(equipo)
    db.session.commit()

    return redirect(url_for('equipos.equipos'))

@equipos_bp.route("/modelos/<marca_id>")
def get_modelos(marca_id):
    modelos = Modelo.query.filter_by(id_marca=marca_id).all()
    modelos_data = [{'id': modelo.id, 'nombre_modelo': modelo.nombre_modelo} for modelo in modelos]
    return jsonify(modelos_data)