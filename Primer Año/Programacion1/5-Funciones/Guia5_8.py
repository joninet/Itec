#Ingresar nombres, luego buscar un nombre y de encontrarlo decir en qué posición está.

def ingresoNombre ():
    nombresLista=[]
    entrada="si"
    while entrada == "si":
        nombre=nombresLista.append(input("ingresar nombre: "))
        entrada=input("agregar mas si/no: ")
    return nombresLista
nn=ingresoNombre()
print(nn)
def buscarNombre (lista):
    nombreBuscar=input("Ingresar nombre a buscar: ")
    for rec in range(len(lista)):
        nom=lista[rec]
        if nom == nombreBuscar:
            nom=rec
    return nom
print(ingresoNombre())
print("la posicion de la palabra buscada es:", buscarNombre(nn))
