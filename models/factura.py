from app import db
import uuid
from datetime import datetime

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = uuid.uuid4(), nullable = False)
    codigo = db.Column(db.String(60), nullable = False)
    vendedor = db.Column(db.String(60), nullable = False)
    forma_pago = db.Column(db.String(60), nullable = False)
    total = db.Column(db.Float, nullable = False)

    #default
    fecha = db.Column(db.DateTime, default = datetime.now)

    #foreing
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable = False)
    
    #relaciones
    #persona = db.relationship('Persona', backref='factura', lazy=True)
    productos = db.relationship('Detalle_factura', backref='factura', lazy=True)

    @property
    def serialize(self):
        productos_se = [producto.serialize() for producto in self.productos] if self.productos else None
        return {
            'external_id': self.external_id,
            'codigo' : self.codigo,
            'vendedor': self.vendedor,
            'fecha': self.fecha,
            'forma_pago': self.forma_pago,
            'productos' : productos_se,
            'total' : self.total
        }