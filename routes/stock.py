from flask import Blueprint, render_template, redirect, request, url_for
from models import Modelo, Fabricante, Marca, Equipo
from app import db

stock_bp = Blueprint('stock', __name__)

@stock_bp.route("/stock", methods=['GET', 'POST'])
def stock():   
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    marcas = Marca.query.all()
    equipos = Equipo.query.all()
    

    if request.method == 'POST':
        id_equipo = int(request.form['id_equipo'])
        cantidad = request.form['cantidad']
        tipo_movimiento = request.form['tipo_movimiento'] == "True"
        
        
        db.session.commit()
        return redirect(url_for('stock.stock'))

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