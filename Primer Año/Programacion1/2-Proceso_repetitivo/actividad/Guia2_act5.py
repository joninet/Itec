#Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.
contador = 0
datos = "si"
while datos == "si":
    sueldo = int(input("Ingrese sueldo: "))
    contador = contador + sueldo
    datos = input("Agregar más si/no: ")
print("El total es: ", contador)
