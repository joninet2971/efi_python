from flask import Blueprint, render_template, redirect, request, url_for, session
from models import Proveedor, Compra, Equipo, Marca, Detalle_Compra
from app import db

detalle_venta_bp = Blueprint('detalle_venta', __name__)

