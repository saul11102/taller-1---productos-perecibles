from flask import Blueprint, jsonify, make_response, request
from flask_expects_json import expects_json
from control.factura_control import FacturaControl
from routes.schemas.schema_factura import save_factura
from control.utils.errors import Errors
from control.Authenticate import token_required

api_factura = Blueprint('api_factura_factura', __name__)

facturaC = FacturaControl()


@api_factura.route('/factura')
@token_required
def home():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in facturaC.listar()])}), 
        200
    )

@api_factura.route('/facturar'   , methods = ["POST"])
@token_required
@expects_json(save_factura)
def guardar_lote():
    data = request.json 
    id = facturaC.guardarFactura(data = data)
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