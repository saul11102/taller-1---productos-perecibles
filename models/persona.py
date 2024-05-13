from app import db
import uuid
from datetime import datetime

class Persona(db.Model):
    id        = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = str(uuid.uuid4()), nullable = False)
    nombre      = db.Column(db.String(50), nullable = False)
    cedula       = db.Column(db.String(10), nullable = False, unique = True)
    apellido = db.Column(db.String(50), nullable = False)
    estado    = db.Column(db.Boolean, nullable = False, default = True)
    
    #default
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now, onupdate = datetime.now)
    
    #relación
    facturas = db.relationship('Factura', backref='persona', lazy=True)

    # methods
    @property
    def serialize(self):
        return {
            'external_id'       : self.external_id,
            'nombre'       : self.nombre,
            'cedula'      : self.cedula,
            'apellido' : self.apellido,
            'estado'    : self.estado,
        }
    
    def copy(self):
        copy_person = Persona(
            external_id = self.external_id,
            nombre       = self.nombre,
            cedula = self.cedula,
            apellido = self.apellido,
            estado    = self.estado,
        )
    
        return copy_person