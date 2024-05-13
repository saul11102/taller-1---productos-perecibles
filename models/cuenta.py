from app import db
import uuid 
from datetime import datetime

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    external_id = db.Column(db.String(60), default = str(uuid.uuid4()), nullable = False)
    usuario = db.Column(db.String(150), unique = True)
    clave = db.Column(db.String(150))
    estado = db.Column(db.Boolean, default = True)

    #default
    created_at = db.Column(db.DateTime, default = datetime.now)
    updated_at = db.Column(db.DateTime, default = datetime.now, onupdate = datetime.now)

    #foreing
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable = False)

    #relación
    #persona = db.relationship('Persona', backref='cuenta', lazy=True)

    @property
    def serialize(self):
        return{
            'external_id' :self.external_id,
            'usuario' : self.usuario,
            'clave' : self.clave,
            'estado' : self.estado
        }
    
    def copy(self):
        new_cuenta = Cuenta(
            id=self.id,
            external_id=self.external_id,
            usuario=self.usuario,
            clave=self.clave,
            estado=self.estado,
            created_at=self.created_at,
            updated_at = self.updated_at,
            persona_id = self.persona_id
        )

    def getPersona(self, id):
        from models.persona import Persona
        return Persona.query.filter_by(id = id).first() 
