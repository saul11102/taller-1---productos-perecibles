from flask import Blueprint, jsonify, make_response, request
from flask_expects_json import expects_json
from control.lote_control import LoteControl
from routes.schemas.schema_lote import save_lote
from control.utils.errors import Errors
from control.Authenticate import token_required

api_lote = Blueprint('api_lote_lote', __name__)

loteC = LoteControl()


@api_lote.route('/lote')
@token_required
def home():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in loteC.listar()])}), 
        200
    )



@api_lote.route('/lote/guardar'   , methods = ["POST"])
@token_required
@expects_json(save_lote)
def guardar_lote():
    data = request.json 
    id = loteC.guardarLote(data = data)
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