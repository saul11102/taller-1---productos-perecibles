save_lote = {
    'type' : 'object',
    'propierties' : {
        'codigo': {'type' : 'string'},
        'fecha_vencimiento': {'type' : 'string', 'format': 'date'},
        'cantidad' : {'type': 'integer'}
    },
    'required' : ['codigo','fecha_vencimiento','cantidad']
}