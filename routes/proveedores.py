from flask import Blueprint, render_template, redirect, request, url_for
from models import Proveedor
from app import db

proveedores_bp = Blueprint('proveedores', __name__)

@proveedores_bp.route("/proveedores", methods=['POST', 'GET'])
def agregar_proveedores():   
    proveedores = Proveedor.query.all()

    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        nuevo_proveedor = Proveedor(nombre_proveedor=nombre, contacto=contacto)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('proveedores.agregar_proveedores'))
    
    return render_template('lista_proveedores.html', proveedores=proveedores)

@proveedores_bp.route("/proveedor/<id>/editar", methods=['GET', 'POST'])
def proveedor_editar(id):
    proveedor = Proveedor.query.get_or_404(id)

    if request.method == 'POST':
        proveedor.nombre_proveedor = request.form['nombre']
        proveedor.contacto = request.form['contacto']
        db.session.commit()
        return redirect(url_for('proveedores.agregar_proveedores'))

    return render_template('proveedor_edit.html', proveedores=proveedor)