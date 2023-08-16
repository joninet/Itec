# Hacer un programa que cuente el número total de bumeranes de una lista de números enteros y muestre cada uno de ellos. Un búmeran es una secuencia formada por 3 números seguidos, en la cual el primero y el último son iguales, y el segundo es diferente. Por ejemplo[5, 2, 5].
# En la lista[7, 2, 1, 2, 3, 3, 3, 4, 2, 4, 1, 8]  hay 2 bumeranes([2, 1, 2] y[4, 2, 4]).

lista = [7, 2, 1, 2, 3, 3, 3, 4, 2, 4, 1, 8]
for rec in range(len(lista)-2):
    bum = lista[rec]
    if bum == lista[rec+2] and bum != lista[rec+1]:
        print(lista[rec], lista[rec+1], lista[rec+2])
