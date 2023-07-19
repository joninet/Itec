# Dada una lista con números, crear otra con los cuadrados de esos valores.
listaNumeros = []
listaCuadrados = []
entrada = "si"
while entrada == "si":
    numero = int(input("Ingresar Numero: "))
    listaNumeros.append(numero)
    entrada = input("Ingresar mas SI/NO: ")
    cuadrado = numero**2
    listaCuadrados.append(cuadrado)
print(listaNumeros)
print(listaCuadrados)
