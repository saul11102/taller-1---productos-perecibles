from app import db
import uuid
from datetime import datetime

class Detalle_factura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = str(uuid.uuid4()), nullable = False)

    #foreing
    factura_id = db.Column(db.Integer, db.ForeignKey('factura.id'), nullable = False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable = False)

    #relaciones
    #factura = db.relationship('Factura', backref='detalle_factura', lazy=True)
    producto = db.relationship('Producto', lazy=True)

    def serialize(self):
        return {
            'producto_nombre': self.producto.nombre,
            'producto_precio': self.producto.precio
        }