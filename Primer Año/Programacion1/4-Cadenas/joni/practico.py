nombres = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana",
    "Santamaría, Carlos",
    "Skarsgard, Azul",
    "Catalejos, Walter"
]
sexos = ["f", "f", "m", "f", "m", "f", "m"]
fechas = [
    "02/05/1943",
    "07/09/1984",
    "10/02/1971",
    "21/12/1967",
    "30/01/1982",
    "30/08/1995",
    "18/07/1959"
]

# El promedio de edad de las mujeres es: 50
aH = 2023
mH = 5
dH = 18
contador = 0
promedio = 0
for i in range(len(sexos)):
    if sexos[i] == "f":
        contador += 1
        edadM = fechas[i]
        dN = int(edadM[:2])
        mN = int(edadM[3:5])
        aN = int(edadM[6:])
        edad = aH - aN
        if (mN > mH) or ((mN == mH) and (dN > dH)):
            edad -= 1
        promedio += edad
print(promedio // contador)
# Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
# A. Torres
# for nombre in nombres:
#     nombreLista = nombre.split(", ")
#     nombreInicial = nombreLista[1][0]
#     apellido = nombreLista[0]
#     print(nombreInicial + ". " + apellido)

# El nombre más largo es: Benicio
# nombreL = ""
# for nombre in nombres:
#     nombreLista = nombre.split(", ")
#     nombreLargo = nombreLista[1]
#     # print(len(nombreLargo))
#     if len(nombreLargo) > len(nombreL):
#         nombreL = nombreLargo
# print("el nombre mas largo es ", nombreL)
