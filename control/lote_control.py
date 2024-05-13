from models.lote import Lote
import uuid
from app import db
from datetime import datetime, timedelta
from flask import current_app   
from models.lote import Lote
from models.producto import Producto

class LoteControl:
    lote = Lote()
    def listar(self):
        return  Lote.query.all()
    
    def guardarLote(self, data):
        if data:  
            lote = Lote()
            lote.external_id = uuid.uuid4()
            lote.codigo = data ['codigo']
            lote.fecha_vencimiento = data ['fecha_vencimiento']
            lote.cantidad = data ['cantidad']
            db.session.add(lote)
            db.session.commit()
            return lote.id   
        else:
            return -2
        