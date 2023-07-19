# Dada una lista de enteros ordenada ascendente y sin repetidos,
# hacer un programa que genere una nueva lista con todos los que faltan entre
# el menor y el mayor. Mostrar ambas listas.
# Comprobar primero que la lista cumpla con la condición inicial.
entrada = "si"
listaE = []
listaN = []
while entrada == "si":
    nE = int(input("Ingresar un numero entero: "))
    if nE in listaE:
        print("el numero ya se ingreso")
    else:
        listaE.append(nE)
    entrada = input("Ingresar mas: ")
print("Lista Original", listaE)
nMayor = max(listaE)
nMenor = min(listaE)
acumulador = nMenor - 1
for rec in range((nMayor - nMenor)+1):
    acumulador = acumulador + 1
    listaN.append(acumulador)
listaE.sort()
print("Lista ordenada", listaE)
print("Nueva lista", listaN)

