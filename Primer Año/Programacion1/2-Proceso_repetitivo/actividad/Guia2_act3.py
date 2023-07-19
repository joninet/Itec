#Pedir el ingreso de 5 números. Contar los mayores de 23. Mostrar el resultado.
contador = 0
for i in range(5):
    num = int(input("Ingrese un número: "))
    if num > 23:
        contador = contador + num

print("Hay", contador, "números mayores de 23.")