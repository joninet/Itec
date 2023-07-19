# Mostrar por pantalla una lista de 10 números enteros consecutivos, comenzando con un número ingresado por teclado.
num = int(input("ingrese numero: "))
num2 = num + 10
for i in range(num, num2):
    print(i)
