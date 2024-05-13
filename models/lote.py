from app import db
import uuid
from datetime import datetime

class Lote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = str(uuid.uuid4()), nullable = False)
    codigo = db.Column(db.String(60), nullable = False)
    fecha_vencimiento = db.Column(db.DateTime, nullable = False)
    cantidad = db.Column(db.Integer, nullable = False)

    #default
    fecha_llegada = db.Column(db.DateTime, default = datetime.now)

    #relaciones
    #productos = db.relationship('Producto', backref='lote', lazy=True)

    @property
    def serialize (self):
        return {
            'codigo' : self.codigo,
            'fecha_vencimiento' : self.fecha_vencimiento,
            'cantidad' : self.cantidad,
            'fecha_llegada' : self.fecha_llegada 
        }
    

    def getLote(self, id):
        from models.lote import Lote
        return Lote.query.filter_by(id = id).first() 
