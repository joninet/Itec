# Definir una clase Auto con un método que le permita poner la marca y el año. En el programa principal declarar dos instancias (objetos), cargarlas y mostrar las marcas de los dos autos.
class auto:
    def __init__(self, marca, año):
        self.marca=marca
        self.año=año

fiesta=auto("Ford", 1998)
ka=auto("Ford", 2006)
print(fiesta.marca,fiesta.año)
print(ka.marca,ka.año)