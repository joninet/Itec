# Definir una clase que al ser instanciada reciba un valor numérico y cargue una lista de nombres hasta esa cantidad. 
# Hacer también un método que muestre la lista completa
class Nombres:
    def __init__(self,cantidad):
        self.cantidad=cantidad
        self.lista=[]
    def ingresoNombre(self):
        for i in range(self.cantidad):
            nombre = input(f"Ingrese el nombre N°{i+1}: ")
            self.lista.append(nombre)
    def listaMostrar(self):
        print("Lista completa:")
        for rec in self.lista:
            print(rec)
validado=False
while not validado:
    try:
        cantidadIngresar = int(input("Ingrese la cantidad de nombres a cargar: "))
        validado=True
    except:
        print("Ingresar solo numeros")
listaN = Nombres(cantidadIngresar)
listaN.ingresoNombre()
listaN.listaMostrar()