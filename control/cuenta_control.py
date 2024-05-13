from models.cuenta import Cuenta
import uuid
from app import db
from datetime import datetime, timedelta
from flask import current_app  
import jwt

class CuentaControl:
    cuenta = Cuenta()
    def listar(self):
        return Cuenta.query.all()
    
    def inicio_sesion(self, data):
        cuentaA = Cuenta.query.filter_by(usuario = data["usuario"]).first()
        if (cuentaA):
            if (cuentaA.clave == data["clave"]):   
                token = jwt.encode(
                    {
                        "external": cuentaA.external_id,
                        "exp": datetime.utcnow() + timedelta(minutes=30) #solo por ahora
                    },
                    key = current_app.config["SECRET_KEY"],
                    algorithm = "HS512"
                )
                cuenta = Cuenta()
                cuenta.copy()
                persona = cuenta.getPersona(cuentaA.persona_id)
                info = {
                    "token": token,
                    "user": persona.apellido+" "+persona.nombre
                }   
                return info 
            else:
                return -4
        else:
            return -4
        