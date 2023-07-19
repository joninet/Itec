# Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió.
lluviaDias = ["Lunes", "Martes", "Miercoles",
              "Jueves", "Viernes", "Sabado", "Domingo"]
lluviaMm = []
lluviamax = []
contador = 0
for x in range(7):
    print(lluviaDias[x])
    mm = int(input("Ingresar mm: "))
    lluviaMm.append(mm)
    if mm > contador:
        contador = mm
        lluviamax.append(x)
        lM = lluviaDias[x]
print(contador)
totalLluvia = sum(lluviaMm)
print("el total de la lluvia es ", totalLluvia, "mm")
print("el dia que mas llovio fu el ", lM, " ", contador, "mm")
