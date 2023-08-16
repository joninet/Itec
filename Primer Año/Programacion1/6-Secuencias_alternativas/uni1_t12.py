#Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). Pedir la cantidad de días no trabajados y año de ingreso en la empresa.
dias = int(input("ingresar los dias no trabajados: "))
year= int(input("Ingrese el año de ingreso a la empresa: "))

if dias == 0 and year <= 2018:
    print("Tiene unadicional del 30%")
    print("Total a cobrar: $",47000+((47000*30)/100))
else:
    print("Total a cobrar: $47000")
