# Dada una lista de enteros ordenada ascendente y sin repetidos,
# hacer un programa que genere una nueva lista con todos los que faltan entre
# el menor y el mayor. Mostrar ambas listas.
# Comprobar primero que la lista cumpla con la condición inicial.
listaE = []
listaN = []
entrada = "si"
while entrada == "si":
    num = int(input("ingresar numero"))
    if num in listaE:
        print("ese numero ya esta")
    else:
        listaE.append(num)
    entrada = input("agrgar mas")
nMax = max(listaE)
nMin = min(listaE)
acumulador = nMin
listaN.append(nMin)
for x in range(nMax-nMin):
    acumulador = acumulador+1
    listaN.append(acumulador)
print(listaN)
