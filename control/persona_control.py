from models.persona import Persona
import uuid
from app import db
from datetime import datetime, timedelta
from flask import current_app   
from models.cuenta import Cuenta
import os
from flask import current_app

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

    def subir_img_perfil(self, files):#, uid_persona):
        
        file = files['file']

        name = file.filename

        file.save(os.path.join(current_app.config['MEDIA_PERFIL'], name))

        return 1