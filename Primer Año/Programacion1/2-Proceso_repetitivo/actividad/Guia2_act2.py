#Preguntar si hay datos para ingresar, en caso afirmativo solicitar un número entero y decir si es negativo o no. Preguntar si repite
entrada = input("hay datos para ingresar si/no: ")
while entrada == "si":
    num = int(input("Escribir un numero"))
    if num >= 0:
        print("es un numero positivo")
    else:
        print("es un numero Negativo")
    entrada = input("Se repite si/no: ")