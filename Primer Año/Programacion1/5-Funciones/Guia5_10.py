#Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió.
listaDias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

def totalLluvia(lista):
    listaMm=[]
    contador=0
    dia=""
    for x in range(len(lista)):
        semana=lista[x]
        print(semana)
        dias= int(input("Ingresar lluvia caida en mm: "))
        listaMm.append(dias)
        if dias > contador:
            contador=dias
            dia=semana
    return dia
print("el dia que mas llovio es el: ", totalLluvia(listaDias))