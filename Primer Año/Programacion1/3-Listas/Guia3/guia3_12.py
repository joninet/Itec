# Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el nombre de cada una.
listaNombre = []
listaSexo = []
contadorM = 0
entrada = "si"
while entrada == "si":
    nombre = input("ingrese nombre: ")
    listaNombre.append(nombre)
    sexo = input("Ingrese sexo M o F: ")
    listaSexo.append(sexo)
    entrada = input("Hay mas si / no: ")
for rec in range(len(listaSexo)):
    if listaSexo[rec] == "F":
        contadorM = contadorM+1
        print(listaNombre[rec])
print(contadorM)
