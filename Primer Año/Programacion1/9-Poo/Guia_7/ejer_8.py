# Redefinir la clase auto con los atributos marca, modelo y año. Hacer una clase heredera TuAuto que 
#agrega dueño y color. Hacer un método que devuelve el color y en el programa principal preguntar por un 
#color y mostrar sólo los autos que cumplan esa condición.
class Auto:
    def __init__(self, marca, modelo, año):
        self.marca=marca
        self.modelo=modelo
        self.año=año

class tuAuto(Auto):
    def __init__(self, marca, modelo, año, dueño, color):
        super().__init__(marca, modelo, año)
        self.dueño=dueño
        self.color=color
    def obtenerColor(self):
        return self.color
    
listaAutos=[]
auto1 = tuAuto("Toyota", "Corola", 2020, "Juan", "Rojo")
auto2 = tuAuto("Ford", "Mustang", 2018, "Maria", "Azul")
auto3 = tuAuto("Chevrolet", "Cruze", 2022, "Pedro", "Rojo")
listaAutos.append(auto1)
listaAutos.append(auto2)
listaAutos.append(auto3)
validado=False
while not validado:
    buscarColor=input("Ingresar el color a buscar: ").capitalize()
    listaColor=[]
    for autos in listaAutos:
        if autos.color == buscarColor:
            listaColor.append(autos.modelo)
    if len(listaColor) == 0:
        print("No se encontraron autos de ese color")
    else:
        print(f"Los autos de color {buscarColor} son:")
        for colorAuto in listaColor:
            print(colorAuto)
            validado=True