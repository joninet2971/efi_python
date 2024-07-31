from flask import Blueprint, render_template, redirect, request, url_for
from models import Equipo, Categoria, Marca, Modelo
from app import db

equipos_bp = Blueprint('equipos', __name__)

@equipos_bp.route("/equipos", methods=['GET', 'POST'])
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
        return redirect(url_for('equipos.equipos'))

    return render_template('equipos_edit.html', 
        equipo=equipo,
        categorias=categorias, 
        marcas=marcas,
        modelos=modelos)