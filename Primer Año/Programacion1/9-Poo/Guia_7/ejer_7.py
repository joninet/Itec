# Heredar de la clase Auto una clase Marca, que agregue el atributo Modelo. Instanciar en  el programa principal 
#(una sola línea en total). La salida debe ser por ejemplo: Auto: VW Modelo: Gol
class auto:
    def __init__(self, marca, año):
        self.marca=marca
        self.año=año

class Modelo(auto):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo=modelo
        
ingresoAuto=Modelo("Ford", 1998,"Fiesta")
print(f"Auto: {ingresoAuto.marca} \nModelo: {ingresoAuto.modelo} \nAño: {ingresoAuto.año}")