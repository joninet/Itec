# 9. Cargar en dos listas paralelas nombres y sueldos. Luego mostrar los nombres de las personas que ganan más de $185000.
listaNombre = []
listaSueldo = []
entrada = "si"
while entrada == "si":
    nombre = input("ingrese nombre: ")
    listaNombre.append(nombre)
    sueldo = int(input("Ingrese sueldo: "))
    listaSueldo.append(sueldo)
    entrada = input("Ingresar mas si/no: ")
for rec in range(len(listaSueldo)):
    if listaSueldo[rec] >= 185000:
        print(listaNombre[rec], "Gana mas de $185000")
