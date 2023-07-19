# Comprobar si un año dado es bisiesto (los que tienen 29 de febrero). Pedirle al usuario el ingreso de un año y decirle si es bisiesto o no.
# Un año es bisiesto si es:
# Divisible por 4.
# No divisible por 100.
# Divisible por 400. (2000 y 2400 son bisiestos pues aún siendo divisibles entre 100 lo son también entre 400. Pero los años 1900, 2100, 2200 y 2300 no lo son porque solo son divisibles entre 100).
# Es bisiesto si es divisible por cuatro y (no divisible por 100 o  divisible por 400).
# Un posible camino:
year = int(input("Ingresar el año: "))
if year % 4 == 0 and (year % 100 == 0 or year % 400):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
