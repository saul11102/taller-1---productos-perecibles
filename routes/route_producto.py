from flask import Blueprint, jsonify, make_response, request
from flask_expects_json import expects_json
from control.producto_control import ProductoControl
from routes.schemas.schema_producto import save_producto
from control.utils.errors import Errors
from control.Authenticate import token_required

api_producto = Blueprint('api_producto_producto', __name__)

productoC = ProductoControl()


@api_producto.route('/producto')
@token_required
def home():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in productoC.listar()])}), 
        200
    )

@api_producto.route('/producto/vigentes')
@token_required
def listar_vigentes():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in productoC.listarVigentes()])}), 
        200
    )



@api_producto.route('/producto/guardar'   , methods = ["POST"])
@token_required
@expects_json(save_producto)
def guardar_producto():
    data = request.json 
    id = productoC.guardarProducto(data = data)
    if(id >= 0):
        return make_response(
                jsonify({"msg" : "OK", "code" : 200, "datos" : {"tag" : "datos guardados"}}), 
                200
        )
    else:
        return make_response(
                jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Errors.error[str(id)]}}), 
                400
    )

@api_producto.route('/actualizar/estados/productos'   , methods = ["GET"])
def actualizar_estados():
    mensaje = productoC.actualizarEstados()
    if mensaje:
        return make_response(
                jsonify({"msg" : "OK", "code" : 200, "datos" : {"tag" : mensaje}}), 
                200
        )
    else:
        return make_response(
                jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : "No se puede actualizar"}}), 
                400
    )

