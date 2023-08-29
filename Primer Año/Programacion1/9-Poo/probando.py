# Definir una clase Auto con un método que le permita poner la marca y el año. En el programa principal 
#declarar dos instancias (objetos), cargarlas y mostrar las marcas de los dos autos.
#6) Agregar al ejercicio 2 (clase Auto) un método que obtenga la antigüedad. 
#En el programa principal mostrar cuáles autos tienen más de 5 años.
# Heredar de la clase Auto una clase Marca, que agregue el atributo Modelo. Instanciar en  el programa principal 
#(una sola línea en total). La salida debe ser por ejemplo: Auto: VW Modelo: Gol
# Redefinir la clase auto con los atributos marca, modelo y año. Hacer una clase heredera TuAuto que 
#agrega dueño y color. Hacer un método que devuelve el color y en el programa principal preguntar por un 
#color y mostrar sólo los autos que cumplan esa condición.
class Cars:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
class yourCar(Cars):
    def __init__(self, brand, model,year,color,owner):
        super().__init__(brand, model,year)
        self.color=color
        self.owner=owner
cars1=yourCar("Toyota","Corolla",2005,"Black","Pedro")
cars2=yourCar("Ford","Fiesta",2020,"Red","Juan")
cars3=yourCar("Renault","Clio",2012,"Black","Jonathan")
cars4=yourCar("Chevrolet","Corsa",1999,"Black","Jorge")
listCars=[]
listCars.append(cars1)
listCars.append(cars2)
listCars.append(cars3)
listCars.append(cars4)
colorSearch=input("Enter the color to search for: ").capitalize()
listColor=[]
for car in listCars:
    if car.color == colorSearch:
        listColor.append(car)
if not listColor:
    print("you will not find cars of that color")
else:
    print(f"the list of cars with the {colorSearch} color are: ")
for car in listColor:
    print(car.model)