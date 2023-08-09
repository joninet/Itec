# Implemente una función que calcule el promedio de una cantidad variable de números. Se tiene que poder pasar un argumento que descarte los valores negativos para sacar dicho promedio.
def promedio(*num, sinNegativos=False):
    contador = 0
    cantidad = 0
    if sinNegativos != True:
        for x in num:
            contador += x
        prom = contador/len(num)
    elif sinNegativos:
        for x in num:
            if x >= 0:
                contador += x
                cantidad += 1
        prom = contador/cantidad
    return prom
#------------------------------------------
print(promedio(121, 65, -88, 34, -9, 27))
print(promedio(121, 65, -88, 34, -9, 27, sinNegativos=True))
