#Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). Pedir la cantidad de días no trabajados y año de ingreso en la empresa.
#Modificar este programa para que sirva para tres empleados en lugar de uno solo.
for i in range(3):
    dias = float(input("Ingresar los dias no Trabajados: "))
    year = float(input("Ingresar el año de ingreso a la empresa: "))
    sueldoDesc = 47000 + (47000 * 0.30)
    if dias == 0 and  2023 - year > 5:
        print("Tiene un adicional del 3o%, Total: $",sueldoDesc) 
    else:
        print("Sueldo a cobrar $47000")