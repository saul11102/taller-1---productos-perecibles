from models.persona import Persona
import uuid
from app import db
from datetime import datetime, timedelta
from flask import current_app   
from models.cuenta import Cuenta

class PersonaControl:
    persona = Persona()
    def listar(self):
        return Persona.query.all()
    
    def guardarPersona(self, data):
        dni = Persona.query.filter_by(cedula = data['cedula']).first()
        if dni:
            return -1
        elif data:  
            persona = Persona()
            persona.uid = uuid.uuid4()
            persona.nombre = data['nombre'] 
            persona.cedula = data['cedula']
            persona.apellido = data['apellido']

            db.session.add(persona)
            db.session.commit()
            
            return persona.id   
        else:
            return -2
        
    def guardarCuenta(self, data):
        
        dni = Persona.query.filter_by(cedula = data['cedula']).first()
        if dni:
            return -1
        elif data:
                persona = Persona()
                persona.external_id = uuid.uuid4()
                persona.nombre = data ['nombre']
                persona.cedula = data ['cedula']
                persona.apellido = data['apellido'] 
                db.session.add(persona)
                db.session.commit()
                cuenta_new = Cuenta()
                cuenta_new.usuario = data['usuario']
                cuenta_new.clave = data['clave']
                cuenta_new.external_id = uuid.uuid4()
                cuenta_new.persona_id = persona.id
                db.session.add(cuenta_new)
                db.session.commit()
                return cuenta_new.id
        else:
            return -2
