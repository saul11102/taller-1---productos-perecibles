from flask import Blueprint, jsonify, make_response, request
from flask_expects_json import expects_json
from control.cuenta_control import CuentaControl
from control.utils.errors import Errors
from routes.schemas.schema_cuenta import session_auth
from control.Authenticate import token_required

api_cuenta = Blueprint('api_cuenta_cuenta', __name__)

cuentaC = CuentaControl()


@api_cuenta.route('/cuenta')
@token_required
def home():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in cuentaC.listar()])}), 
        200
    )



@api_cuenta.route('/session'   , methods = ["POST"])
@expects_json(session_auth)
def session():
    data = request.json     
    id = cuentaC.inicio_sesion(data = data)
    if type (id) == int:
        return make_response(
                jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Errors.error[str(id)]}}), 
                400
        )
        
    else:
        return make_response(
                jsonify({"msg" : "OK", "code" : 200, "datos" : id}), 
                200
        )