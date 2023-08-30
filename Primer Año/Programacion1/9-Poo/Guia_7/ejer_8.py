# Redefinir la clase auto con los atributos marca, modelo y año. Hacer una clase heredera TuAuto que 
#agrega dueño y color. Hacer un método que devuelve el color y en el programa principal preguntar por un 
#color y mostrar sólo los autos que cumplan esa condición.

#version mia
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
auto1 = listaAutos.append(tuAuto("Toyota", "Corola", 2020, "Juan", "Rojo"))
auto2 = listaAutos.append(tuAuto("Ford", "Mustang", 2018, "Maria", "Azul"))
auto3 = listaAutos.append(tuAuto("Chevrolet", "Cruze", 2022, "Pedro", "Rojo"))
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
#-----------------------------------
#Profesor version 1
class Auto():
    def __init__(self, ma, mo, an):
        self.marca = ma
        self.modelo = mo
        self.anio = an

class TuAuto(Auto):
    def __init__(self, ma, mo, an, du, co):
        super().__init__(ma, mo, an)
        self.duenio = du
        self.color = co

    def getColor(self):
        return self.color
    
listaStringsAutos = [
    'Ford,EcoSport,2016,kan,rojo',
    'Fiat,Cronos,2021,pipo,blanco',
    'Honda,HR-V,2018,pelado,rojo',
    'VW,Amarok,2022,Gustavo,gris'
]

listaObjetosAutos = []
for auto in listaStringsAutos:
    mar, mod, ani, due, col = auto.split(',')
    a = TuAuto(mar, mod, ani, due, col)
    listaObjetosAutos.append(a)

whichColor = 'blanco'
for autito in listaObjetosAutos:
    if autito.getColor() == whichColor:
        print(f'El {autito.modelo} de {autito.duenio} es {autito.color}')
#-----------------------------------
#Profesor version 2
class Auto():
    def __init__(self, ma, mo, an):
        self.marca = ma
        self.modelo = mo
        self.anio = an

class TuAuto(Auto):
    def __init__(self, ma, mo, an, du, co):
        super().__init__(ma, mo, an)
        self.duenio = du
        self.color = co

    def getColor(self):
        return self.color
    
listaAutos = [
    TuAuto('Ford','EcoSport',2016,'kan','rojo'),
    TuAuto('Fiat','Cronos',2021,'pipo','blanco'),
    TuAuto('Honda','HR-V',2018,'pelado','rojo'),
    TuAuto('VW','Amarok',2022,'Gustavo','gris')
]


whichColor = 'rojo'
for autito in listaAutos:
    if autito.getColor() == whichColor:
        print(f'El {autito.modelo} de {autito.duenio} es {autito.color}')