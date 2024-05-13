from models.producto import Producto
from models.lote import Lote
from models.estado_producto import Estado_producto
import uuid
from app import db
from datetime import datetime, timedelta
from flask import current_app  

class ProductoControl:
    Producto = Producto()
    def listar(self):
        return Producto.query.all()
    
    def guardarProducto(self, data):
        if data:  
            
            producto = Producto()
            producto.external_id = uuid.uuid4()
            producto.nombre = data['nombre']
            producto.precio = data ['precio']
            producto.stock = True
            #buscar el lote

            lote = Lote.query.filter_by(codigo = data['codigo_lote']).first()

            if lote is None:
                return -3

            producto.lote_id = lote.id

            # Calcular la diferencia de días
            diferencia_dias = (lote.fecha_vencimiento - datetime.now()).days


            # Actualizar el estado según la diferencia de días
            if diferencia_dias <= 0:
                producto.estado = Estado_producto.Caducado
                producto.stock = False
            elif diferencia_dias <= 3:
                producto.estado = Estado_producto.Proximo_caducar
            else:
                producto.estado = Estado_producto.Bueno

            db.session.add(producto)
            db.session.commit()
            
            return producto.id   
        else:
            return -2
        

    def actualizarEstados(self):
        productos = Producto.query.all()

        for producto in productos:
            lote = Lote.query.get(producto.lote_id)

            if lote is not None:
                # Calcular la diferencia de días
                diferencia_dias = (lote.fecha_vencimiento - datetime.now()).days
                
                producto.stock = True

                # Actualizar el estado según la diferencia de días
                if diferencia_dias <= 0:
                    producto.estado = Estado_producto.Caducado
                    producto.stock = False
                elif diferencia_dias <= 3:
                    producto.estado = Estado_producto.Proximo_caducar
                else:
                    producto.estado = Estado_producto.Bueno

            producto.external_id = uuid.uuid4()
            db.session.merge(producto)

        db.session.commit()

        return "Estados actualizados correctamente"