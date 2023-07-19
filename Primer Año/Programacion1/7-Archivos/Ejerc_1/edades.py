# 4. recorrido con for
from funciones import *
listaMayores = []
with open("7-Archivos/Ejerc_1/personas.txt", encoding="utf-8") as pers:
    pers.readline()
    for linea in pers:
        nombre, nacim = linea.split()
        resultado = calculoEdad(nacim)
        if resultado >= 18:
            nombre = str(nombre) + " " + str(resultado) + "\n"
            listaMayores.append(nombre)
with open('7-Archivos/Ejerc_1/mayores.txt', 'w') as agregoFila:
    agregoFila.write("Nombre, Edad\n")
    ) as agregoMayores:
    agregoMayores.writelines(listaMayores)
