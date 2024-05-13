save_producto = {
    'type' : 'object',
    'propierties' : {
        'nombre': {'type' : 'string'},
        'precio': {'type' : 'float'},
        'codigo_lote' : {'type': 'string'}
    },
    'required' : ['nombre','precio','codigo_lote']
}