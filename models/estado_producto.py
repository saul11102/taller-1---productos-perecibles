import enum

class Estado_producto(enum.Enum):
    Bueno = 'Bueno'
    Proximo_caducar = 'Proximo_caducar'
    Caducado = 'Caducado'

    def serialize(self):
        return self.value