from motor import Motor
from rueda import Rueda

class Coche():
    def __init__(self) -> None:
        self.motor = Motor() # Composición
        self.ruedas = [
            Rueda('delantera izquierda'),
            Rueda('delantera derecha'),
            Rueda('trasera izquierda'),
            Rueda('trasera derecha'),
            Rueda('auxilio')
        ]

    def arrancarMotor(self):
        self.motor.arrancar()

    def apagarMotor(self):
        self.motor.apagar()

    def inflarRueda(self):
        for rueda in self.ruedas:
            rueda.inflar()

    def estadoCoche(self):
        print('-------------------')
        print('Estado General del Auto')
        print(f'Motor: {self.motor.estado}')
        for rueda in self.ruedas:
            print(f'Rueda {rueda.posicion}: {rueda.estado}')

        print('-------------------')