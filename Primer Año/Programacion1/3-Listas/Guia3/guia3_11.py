# 11. Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.
aH=2023
mH=5
dH=3
listaNombre = []
listaA = []
listaM = []
listaD = []
entrada = "si"
while entrada == "si":
    nombre = input("Ingresar Nombre: ")
    listaNombre.append(nombre)
    aA = int(input("Ingresar Año de Nacimiento: "))
    listaA.append(aA)
    aM = int(input("Ingresar Mes de Nacimiento: "))
    listaM.append(aM)
    aD = int(input("Ingresar dia de Nacimiento: "))
    listaD.append(aD)
    entrada = input("hay mas SI/NO: ")
for rec in range(len(listaNombre)):
  edad = aH - listaA[rec]
  if listaM[rec] > mH or listaM[rec] == mH and listaD[rec] > dH:
    edad -= 1
  if edad >= 18:
    print(listaNombre[rec], " es mayor de edad")