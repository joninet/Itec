# 1. Pedir el ingreso de 10 números. Contar los mayores de 23 y almacenar los que cumplen la condición.  Mostrar la cantidad y los números guardados.
acumulador = 0
listas = []
for x in range(10):
    num = int(input("ingrese numero"))
    if num >= 23:
        listas.append(num)
        acumulador = acumulador + 1
print("la cantidad de numeros guardados son", acumulador)
print("los numeros guardados son", listas)
