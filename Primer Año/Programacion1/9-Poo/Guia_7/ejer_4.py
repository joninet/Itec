# Definir una clase que al ser instanciada reciba un valor numérico y cargue una lista de nombres hasta esa cantidad. 
# Hacer también un método que muestre la lista completa
class Nombres:
    def __init__(self,nombre):
        self.nombre=nombre
listaNombres=[]
cantidadNombres=int(input("Cantidad de nombres a ingresar: "))
for x in range(cantidadNombres):
    n=input(f"ingresar el Nombre N°{x+1}: ")
    agregoN=Nombres(n)
    listaNombres.append(agregoN)
print("Lista completa de nombres:")
for i in listaNombres:
    print(i.nombre)

        