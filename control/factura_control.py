from models.factura import Factura
from models.persona import Persona
from models.producto import Producto
from models.lote import Lote
from models.detalle_factura import Detalle_factura
import uuid
from app import db
from datetime import datetime, timedelta
from flask import current_app

class FacturaControl:
    factura = Factura()
    def listar(self):
        return  Factura.query.all()
    
    def guardarFactura(self, data):
        if data:  
            #buscar persona 
            persona = Persona.query.filter_by(cedula = data['cedula']).first()

            if persona is None:
                return -7
            
            total = 0
            factura = Factura()
            factura.external_id = uuid.uuid4()
            factura.codigo = data['codigo']
            factura.vendedor = data['vendedor']
            factura.forma_pago = data['forma_pago']
            factura.total = total

            

            factura.persona_id = persona.id

            db.session.add(factura)
            db.session.flush()
            
            #guardar productos
            for producto_data in data['productos']:
                lote = Lote.query.filter_by(codigo = producto_data['codigo']).first()
                if lote is None:
                    return -3  
                producto = Producto.query.filter_by(lote_id=lote.id).first()
                if producto is None:
                    return -8
                
                detalle_factura = Detalle_factura()
                detalle_factura.factura_id = factura.id
                detalle_factura.producto_id = producto.id
                db.session.add(detalle_factura)
                total += producto.precio

            factura.total = total

            db.session.commit()
            return factura.id   
        else:
            return -2
        