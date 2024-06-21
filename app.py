from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import config.config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.config.Config')

    CORS(app)
    
    db.init_app(app)
    with app.app_context():
        
        from models.cuenta import Cuenta
        from models.detalle_factura import Detalle_factura
        from models.factura import Factura
        from models.lote import Lote
        from models.producto import Producto
        from models.persona import Persona

        from routes.route_persona import api_persona
        from routes.route_lote import api_lote
        from routes.route_producto import api_producto
        from routes.route_cuenta import api_cuenta
        from routes.route_factura import api_factura

        app.register_blueprint(api_persona)
        app.register_blueprint(api_lote)
        app.register_blueprint(api_producto)
        app.register_blueprint(api_cuenta)
        app.register_blueprint(api_factura)

        #crear tablas de bd
        db.create_all()
        
    return app
