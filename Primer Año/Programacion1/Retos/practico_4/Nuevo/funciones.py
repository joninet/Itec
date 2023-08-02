def armoListaNueva(lista):
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
    return sexoM, sexoF


def ordenolistaMayor_menor (lista):
    separo_cantidad=lista.split()
    cantidad=int(separo_cantidad[1])
    return cantidad


def obtenerDiferenciaNac(genero, año2008, año2018):
    posi = inputInt("Ingrese posicion hasta 5: ", 0, 5)
    n1, c1, s1 = buscarPosicion(año2008, posi)
    n2, c2, s2 = buscarPosicion(año2018, posi)
    diferencia = c1-c2
    if diferencia > 0:
        print(
            f"{diferencia} nacimientos de {genero} más del primero del ranking de 2008 {n1} sobre {n2}")
    elif diferencia < 0:
        print(
            f"{diferencia} nacimientos de {genero} más del primero del ranking de 2018 {n2} sobre {n1}")
    else:
        print(f"{diferencia} nacimientos de {genero} son iguales {n1} {n2}")


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


def buscarRepetidos(*args):
    nombres = ""
    listaNom = []
    for i in args:
        nom, cant, sexo = i.split()
        listaNom.append(nom)
    for x in listaNom:
        busco = listaNom.count(x)
        if busco > 1:
            nombres = nombres + " " + x
            listaNom.remove(x)
    return nombres
print("prueba2")