save_factura = {
    "type": "object",
    "properties": {
        "codigo": {"type": "string"},
        "vendedor": {"type": "string"},
        "forma_pago": {"type": "string"},
        "cedula": {"type": "string"},
        "productos": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "codigo": {"type": "string"},
                },
                "required": ["codigo"]
            }
        }
    },
    "required": ["codigo", "vendedor", "forma_pago", "cedula", "productos"]
}