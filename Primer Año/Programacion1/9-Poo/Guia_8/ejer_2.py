#2) Desarrolla una clase Cafetera con atributos capacidadMaxima (la cantidad máxima de café que puede contener la cafetera) y 
#cantidadActual (la cantidad actual de café que hay en la cafetera). Implementa, al menos, los siguientes métodos: 
#Constructor: establece la capacidad máxima en 1000 (c.c.)  y la actual en cero (cafetera vacía). 
#llenarCafetera(), servirTaza(int): simula la acción de servir una taza con la capacidad indicada, si la cantidad actual de café
#no alcanza para llenar la taza, se sirve lo que quede. 
#vaciarCafetera(): pone la cantidad de café actual en cero.  
#mostrarCafetera(): nos dice cuánto café hay.
class Cafetera:
    def __init__(self,cantidadMaxima,cantidadActual):
        self.cantidadMaxima=cantidadMaxima
        self.cantidadActual=cantidadActual
    def llenarCafetera(self,cantidad):
        if cantidad < self.cantidadMaxima:
            self.cantidadActual += cantidad
        else:
            print(f"Lo maximo que soporta la cafetera es de {self.cantidadMaxima}")
    def servirTaza(self,cantidad):
        if cantidad < self.cantidadActual:
            self.cantidadActual-=cantidad
            return f"se sirvio la taza correctamente"
        else:
            return f"la cantidad de la cafetera es de {self.cantidadActual}, ingresar menos cantidad a servir"
    def vaciarCafetera(self):
        self.cantidadActual=0
    def mostrarCantidadCafetera(self):
        return f"la cantidad de la cafetera actual es de {self.cantidadActual}"

ingreso=Cafetera(1000,0)
ingreso.llenarCafetera(750)
ingreso.servirTaza(350)
print(ingreso.mostrarCantidadCafetera())
ingreso.vaciarCafetera()
print(ingreso.mostrarCantidadCafetera())
    
    
