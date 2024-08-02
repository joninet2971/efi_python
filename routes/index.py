from flask import Blueprint, render_template, redirect, request, url_for
from models import Equipo, Categoria, Marca, Modelo
from app import db

index_bp = Blueprint('index', __name__)

@index_bp.route("/index", methods=['GET', 'POST'])
def index():
    equipos = Equipo.query.all()
    categorias = Categoria.query.all()
    marcas = Marca.query.all()
    modelos = Modelo.query.all()
   
    return render_template(
        'index.html',
        equipos=equipos,
        modelos=modelos,
        categorias=categorias,
        marcas=marcas
    )