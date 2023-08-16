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
"""def promedio(*args, sinNegativos=False):
    totalTodos = 0
    totalPositivos = 0
    contadorPositivos = 0
    for n in args:
        if sinNegativos and n >= 0:
            totalPositivos += n
            contadorPositivos += 1
        else:
            totalTodos += n
    if sinNegativos:
        return totalPositivos / contadorPositivos
    else:
        return totalTodos / len(args)"""
print(promedio(121, 65, -88, 34, -9, 27))
print(promedio(121, 65, -88, 34, -9, 27, sinNegativos=True))
