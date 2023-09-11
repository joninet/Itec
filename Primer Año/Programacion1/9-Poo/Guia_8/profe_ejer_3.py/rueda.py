class Rueda:
    def __init__(self, posicion) -> None:
        self.estado = 'desinflada'
        self.posicion = posicion

    def inflar(self):
        if self.estado == 'desinflada':
            self.estado = 'inflada'
            print(f'Inflando rueda {self.posicion}')