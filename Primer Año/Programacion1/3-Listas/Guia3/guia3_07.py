# Eliminar todos los valores iguales de una lista. Previamente, solicitar el valor y si no está, mostrar un cartel diciendo que no lo ha encontrado.
listaNombres = []
entrada = "si"
while entrada == "si":
    nombre = input("Ingresar nombre: ")
    listaNombres.append(nombre)
    entrada = input("ingresar mas si/no: ")
buscar = input("buscar nombrea borrar: ")
elementoEliminar = buscar
cO = len(listaNombres)
while elementoEliminar in listaNombres:
    listaNombres.remove(elementoEliminar)
    print("se elimino el nombre", buscar)
cA = len(listaNombres)
if cO == cA:
    print(buscar, "no se encuentra")
print(listaNombres)
