#Dada una lista cargada con números enteros, obtener el promedio de ellos. Mostrar por pantalla dicho promedio y los números ingresados que sean mayores que él. Dos funciones: promedio y mayorQue.
listaNum=[34,56,89,23,67]
def promedio(lista):
    acum=0
    for x in lista:
        acum+=x
    prom=acum/len(lista)
    return prom
p=promedio(listaNum)
def mayorQue(lista):
    numMayor=""
    for x in lista:
        if x > p:
            numMayor+=str(x) + " "
    return numMayor
print("los numeros ingresados que son mayor al promedio:", mayorQue(listaNum))



