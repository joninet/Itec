# Realizar un algoritmo que permita ingresar un dato numérico y determinar si es un número positivo de dos dígitos.
n1 = int(input("Ingrese un numero: "))
if n1 >= 10 and n1 <= 99: 
    print("es un numero positivo de dos digitos")
else:
    print("No es un numero de dos digitos")
