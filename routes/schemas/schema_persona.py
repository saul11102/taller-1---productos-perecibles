save_person = {
    'type' : 'object',
    'propierties' : {
        'nombre': {'type' : 'string'},
        'cedula': {'type' : 'string'},
        'apellido': {'type' : 'string'}
    },
    'required' : ['nombre','cedula','apellido']
}

save_account = {
    'type' : 'object',
    'propierties' : {
        'nombre': {'type' : 'string'},
        'cedula': {'type' : 'string'},
        'apellido': {'type' : 'string'},
        'usuario' : {'type': 'string'},
        'clave' : {'type': 'string'}
    },
    'required' : ['nombre','cedula','apellido', 'clave', 'usuario']
}
