# Guardar en una lista los números pares mayores que 0 y menores que 31.
entrada = "si"
lista = []
while entrada == "si":
    numero = int(input("Ingresar Numero: "))
    entrada = input("Agregar mas SI/NO: ")
    if numero >= 0 and numero <= 31 and numero % 2 == 0:
        lista.append(numero)
print(lista)
