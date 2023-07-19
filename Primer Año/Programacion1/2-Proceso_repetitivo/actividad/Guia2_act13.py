# Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.
contador = 0
dias = 0
for x in range(7):
    lluvia = int(input("Ingrese mm: "))
    if lluvia > 0:
        contador = contador + lluvia
    elif lluvia == 0:
        dias = dias + 1
print("Cantidad Total de LLuvia ",contador,"mm.","Los dias que no llovio son", dias )
