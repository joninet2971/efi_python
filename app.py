from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/equipos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes.equipos import equipos_bp
from routes.stock import stock_bp
from routes.categorias import categorias_bp
from routes.proveedores import proveedores_bp
from routes.marcas import marcas_bp
from routes.fabricantes import fabricantes_bp
from routes.modelos import modelos_bp

app.register_blueprint(equipos_bp)
app.register_blueprint(stock_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(proveedores_bp)
app.register_blueprint(marcas_bp)
app.register_blueprint(fabricantes_bp)
app.register_blueprint(modelos_bp)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)