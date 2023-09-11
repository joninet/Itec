class Motor():
    def __init__(self) -> None:
        self.estado = 'apagado'

    def arrancar(self):
        if self.estado == 'apagado':
            self.estado = 'encendido'
            print('Encendiendo Motor ... ')
        else:
            print('Oiga anciano, el motor ya está encendido')


    def apagar(self):
        if self.estado == 'encendido':
            self.estado = 'apagado'
            print('Apagando Motor...')
        else:
            print('Oiga anciano, el motor ya está apagado')
