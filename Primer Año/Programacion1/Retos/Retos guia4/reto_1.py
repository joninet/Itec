# Transformar esta cadena a dos listas paralelas de nombres y sueldos(sin el signo pesos): “Juan$120000,Ana$250000,Luis$76500,Vilma$98700”. Mostrar las listas resultantes completas.
frase = "Juan$120000,Ana$250000,Luis$76500,Vilma$98700"
listaNombre = []
listaSueldo = []
listaF = frase.split(",")  # transformo la cadena en lista
for rec in listaF:
    buscar = rec.find("$")  # busco el $ y me dice la posicion
    # guardo en la variable lo que dice rec pero desde el principio hasta el valor que me largo find
    nombre = rec[:buscar]
    listaNombre.append(nombre)  # la agrego a la lista
    # guardo en la variable lo que dice rec pero desde lo que me largo find y le sumo 1 mas asi no me toma el $ hasta el final
    sueldo = rec[buscar+1:]
    listaSueldo.append(sueldo)  # agrego a la lista sueldo
print(listaNombre)
print(listaSueldo)
