from flask import Blueprint, jsonify, make_response, request
from flask_expects_json import expects_json
from control.persona_control import PersonaControl
from routes.schemas.schema_persona import save_person
from control.utils.errors import Errors
from control.Authenticate import token_required

api_persona = Blueprint('api_persona_persona', __name__)

personaC = PersonaControl()


@api_persona.route('/persona')
@token_required
def home():
    return make_response(
        jsonify({"msg" : "OK", "code" : 200, "datos" : ([i.serialize for i in personaC.listar()])}), 
        200
    )


@api_persona.route('/persona/guardar'   , methods = ["POST"])
@token_required
@expects_json(save_person)
def guardar_persona():
    data = request.json 
    id = personaC.guardarPersona(data = data)
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

@api_persona.route('/cuenta/guardar'   , methods = ["POST"])
#@token_required
@expects_json(save_person)
def guardar_cuenta():
    data = request.json 
    id = personaC.guardarCuenta(data = data)
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
