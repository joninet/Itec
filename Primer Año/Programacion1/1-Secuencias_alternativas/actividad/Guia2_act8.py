#Ingresar autos y sus precios y contar cuantos valen entre $3.460.000 y $12.850.000. Terminar la carga cuando el valor ingresado sea 0.
contador = 0
precio = 1
while precio != 0:
    if 3460 < precio < 12850:
        contador = contador + 1
    auto = input("ingrese nombre del auto")
    precio = float(input("Ingrese el precio del auto (0 para terminar): "))
print("Se ingresaron", contador, "autos con un precio entre $3.460.000 y $12.850.000.")
