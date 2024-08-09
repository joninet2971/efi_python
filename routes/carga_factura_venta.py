from flask import Blueprint, render_template, redirect, request, url_for, session
from models import Proveedor, Compra, Detalle_Compra
from app import db

carga_factura_venta_bp = Blueprint('carga_factura_venta', __name__)