#Modificar este programa para que se pregunte previamente cuántos estudiantes se van a inscribir.
# Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto. Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento en la cuota que es de $7000. Mostrar nombre, ciudad, carrera y monto final de la cuota.
ins = int (input("cuantos inscriptos"))
for i in range(ins):
    nombre = input("Nombre ")
    carrera = input("Carrera ")
    ciudad = input("Ciudad ")
    descuento = 7000 * 0.85
    if carrera == "electromecanica" and ciudad != "rio cuarto":
        print(nombre)
        print(carrera)
        print(ciudad)
        print("Monto a pagar con descuento del 15% $", descuento)
    else:
        print(nombre)
        print(carrera)
        print(ciudad)
        print("Monto a pagar $7000 no tenes descuento")