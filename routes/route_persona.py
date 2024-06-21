from flask import Blueprint, jsonify, make_response, request, send_from_directory, current_app
from flask_expects_json import expects_json
from control.persona_control import PersonaControl
from routes.schemas.schema_persona import save_person
from control.utils.errors import Errors
from control.Authenticate import token_required
import os

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

@api_persona.route('/persona/perfil', methods = ["POST"])
def guardar_perfil():

    files = request.files

    #persona = str(request.form['uid'])

    id = personaC.subir_img_perfil(files=files)#, uid_persona=persona)

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

@api_persona.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config['MEDIA_PERFIL'], filename)

@api_persona.route('/media', methods=['GET'])
def all_media():
    fotos = os.listdir(current_app.config['MEDIA_PERFIL'])
    images = [foto for foto in fotos if foto.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return jsonify({'files': images})