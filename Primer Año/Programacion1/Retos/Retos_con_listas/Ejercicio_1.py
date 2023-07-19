# Dada una lista de enteros ordenada ascendente y sin repetidos,hacer un programa que genere una nueva lista con todos los que faltan entre el menor y el mayor. Mostrar ambas listas. Comprobar primero que la lista cumpla con la condición inicial.
lista = [2, 3, 6, 8, 20, 22]
listaN = []
min = lista[0]-1
max = lista[len(lista)-1]
for rec in range(max):
    min = min + 1
    listaN.append(min)
print(listaN)
