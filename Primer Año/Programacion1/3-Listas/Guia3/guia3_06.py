# Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está.
listaNombres = []
entrada = "si"
while entrada == "si":
    nombre = input("Ingresar Nombre: ")
    listaNombres.append(nombre)
    entrada = input("ingresar mas SI/NO: ")
buscar = input("Buscar Nombre: ")
for rec in range(len(listaNombres)):
    if listaNombres[rec] == buscar:
        encontrado = listaNombres.index(buscar)
        print(encontrado)
