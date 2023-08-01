def ordenarLista(lista):
    sexoM = []
    sexoF = []
    listaN = lista.split(",")
    for x in range(0, len(listaN), 3):
        nombre = listaN[x]
        cantidad = listaN[x+1]
        sexo = listaN[x+2]
        completo = nombre+" "+cantidad+" "+sexo
        if sexo == "m":
            sexoM.append(completo)
        else:
            sexoF.append(completo)
    for i in range(len(sexoM)):
        ordeno = i
        for j in range(i+1, len(sexoM)):
            if int(sexoM[j].split()[1]) > int(sexoM[ordeno].split()[1]):
                ordeno = j

        sexoM[i], sexoM[ordeno] = sexoM[ordeno], sexoM[i]
    for i in range(len(sexoF)):
        ordeno = i
        for j in range(i+1, len(sexoF)):
            if int(sexoF[j].split()[1]) > int(sexoF[ordeno].split()[1]):
                ordeno = j

        sexoF[i], sexoF[ordeno] = sexoF[ordeno], sexoF[i]
    return sexoM, sexoF


def inputInt(msg, mini=-10**308, maxi=10**308):
    validado = False
    while not validado:
        try:
            num = int(input(msg))
            if mini <= num <= maxi:
                validado = True
            else:
                print("Error - Numero fuera de rango")
        except:
            print("Error - Ingrese un numero entero")

    return num


def buscarPosicion(lista, orden):
    datos = lista[orden-1]
    nombre, cantidadStr, sexo = datos.split()
    cantidad = int(cantidadStr)
    return nombre, cantidad, sexo


def unificar(inicial, *args):
    resultadoNom = ""
    contador = 0
    inicial = inicial.upper()
    for i in args:
        nombre, cantidad, sexo = i.split()
        ini = nombre[0]
        # nombre=nombre[0]
        if ini == inicial:
            resultadoNom = resultadoNom + " " + nombre
            contador += 1
    if contador == 0:
        resultadoNom = "No hay nombres con esa inicial"

    return resultadoNom


def buscarRepetidos(lista):
    nombres = ""
    listaNom = []
    for i in lista:
        nom, cant, sexo = i.split()
        listaNom.append(nom)
    for x in listaNom:
        busco = listaNom.count(x)
        if busco > 1:
            nombres = nombres + " " + x
            listaNom.remove(x)
    return nombres
