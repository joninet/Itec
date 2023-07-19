# Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una.
contador = 0
personas = "si"
while personas == "si":
    nombre = input("Ingresar Nombre: ")
    sexo = input("ingresar sexo Mujer/Varon: ")
    if sexo == "mujer":
        contador += 1
        print("Nombre: ", nombre)
    personas = input("Ingresar mas SI/NO: ")
print("total de Mujeres", contador)
