#Escribe una función que determine si dos listas tienen algún elemento en común.
multiplosDos=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
multiplosTres=[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
def elemCom(listaUno,listaDos):
    listaEcomun=[]
    for rec in listaUno:
        if rec in listaDos:
            listaEcomun.append(rec)
    return listaEcomun
print("los elementos en comun de las dos listas son: ", elemCom(multiplosDos,multiplosTres))
