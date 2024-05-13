from app import db
import uuid
from datetime import datetime
from .estado_producto import Estado_producto

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = str(uuid.uuid4()), nullable = False)
    nombre = db.Column(db.String(60), nullable = False)
    precio = db.Column(db.Float, nullable = False)
    stock = db.Column(db.Boolean, default = True)

    #foránea
    lote_id = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable = False)

    #enum
    estado = db.Column(db.Enum(Estado_producto), nullable = False)

    #default
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now, onupdate = datetime.now)

    #relaciones
    lote = db.relationship('Lote', backref='producto', lazy=True)
    #factura = db.relationship('Detalle_factura', backref='producto', lazy=True)

    @property
    def serialize(self):
        lote_serialized = self.lote.serialize if self.lote else None
        return {
            'nombre' : self.nombre,
            'precio' : self.precio,
            'stock' : [1 if self.stock else 0],
            'estado' : self.estado.serialize(),
            'lote': lote_serialized
        }


    def copy(self):
        new_producto = Producto(
            id=self.id,
            nombre=self.nombre,
            precio=self.precio,
            estado=self.estado,
            lote_id = self.lote_id,
            created_at = self.created_at,
            updated_at = self.updated_at
        )
        return new_producto