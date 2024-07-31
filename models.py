from app import db

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_fabricante = db.Column(db.String(255), nullable=False)
    pais_origen = db.Column(db.String(255), nullable=False)

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_marca = db.Column(db.String(255), nullable=False)

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_modelo = db.Column(db.String(255), nullable=False)
    id_fabricante = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    id_marca = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    
    fabricante = db.relationship('Fabricante', backref=db.backref('modelos', lazy=True))
    marca = db.relationship('Marca', backref=db.backref('modelos', lazy=True))

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_accesorio = db.Column(db.String(255), nullable=False)
    compatibilidad_modelo = db.Column(db.String(255), nullable=False)

class Accesorio_Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_accesorio = db.Column(db.Integer, db.ForeignKey('accesorio.id'), nullable=False)
    id_modelo = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    
    accesorio = db.relationship('Accesorio', backref=db.backref('accesorio_modelos', lazy=True))
    modelo = db.relationship('Modelo', backref=db.backref('accesorio_modelos', lazy=True))

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_caracteristica = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)

class Equipo_Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_equipo = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    id_caracteristica = db.Column(db.Integer, db.ForeignKey('caracteristica.id'), nullable=False)
    
    equipo = db.relationship('Equipo', backref=db.backref('equipo_caracteristicas', lazy=True))
    caracteristica = db.relationship('Caracteristica', backref=db.backref('equipo_caracteristicas', lazy=True))

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(255), nullable=False)

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_marca = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    id_modelo = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    costo = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    
    marca = db.relationship('Marca', backref=db.backref('equipos', lazy=True))
    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    categoria = db.relationship('Categoria', backref=db.backref('equipos', lazy=True))

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_proveedor = db.Column(db.String(255), nullable=False)
    contacto = db.Column(db.String(255), nullable=False)

class Proveedor_Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    id_equipo = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    
    proveedor = db.relationship('Proveedor', backref=db.backref('proveedor_equipos', lazy=True))
    equipo = db.relationship('Equipo', backref=db.backref('proveedor_equipos', lazy=True))

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_equipo = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    tipo_movimiento = db.Column(db.Boolean, nullable=False)
    
    equipo = db.relationship('Equipo', backref=db.backref('stocks', lazy=True))