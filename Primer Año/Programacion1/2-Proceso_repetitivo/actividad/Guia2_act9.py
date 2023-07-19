# Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. Se deberá ir preguntando si hay más números para ingresar. = 0
contador = 0
datos = "si"
while datos == "si":
    num = int(input("Ingrese numero: "))
    if num > contador:
        contador = num
    datos = input("Agregar SI/NO")
print("El numero mas grande es", contador)
