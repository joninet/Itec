# Definir una clase que al ser instanciada reciba un valor numérico y cargue una lista de nombres hasta esa cantidad. 
# Hacer también un método que muestre la lista completa
class ListaNombres:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.nombres = []

    def cargar_nombres(self):
        for i in range(self.cantidad):
            nombre = input(f"Ingrese el nombre {i+1}: ")
            self.nombres.append(nombre)
for nombre in self.nombres:
    print("")

class ListaNombres:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.nombres = []

    def cargar_nombres(self):
        for i in range(self.cantidad):
            nombre = input(f"Ingrese el nombre {i+1}: ")
            self.nombres.append(nombre)

    def mostrar_lista(self):
        print("Lista de nombres:")
        for nombre in self.nombres:
            print(nombre)

# Instanciar la clase y usar los métodos
cantidad_nombres = int(input("Ingrese la cantidad de nombres a cargar: "))
lista_nombres = ListaNombres(cantidad_nombres)
lista_nombres.cargar_nombres()
lista_nombres.mostrar_lista()

        