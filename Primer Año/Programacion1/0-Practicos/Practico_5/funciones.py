def contarPais(lista,paisBuscar):
    contador=0
    resultado=""
    for x in lista:
        pais=x.split(",")[1]
        if pais == paisBuscar:
            contador += 1
    if contador > 0:
        resultado = f"El país {paisBuscar} tiene {contador} personas."
    else:
        resultado= f"No se encuentra el pais {paisBuscar}"
    return resultado
def fechaNacimiento(lista):
    validado=False
    while not validado:
        letraIni=input("Ingresar Inicial a buscar: ")
        contador=0
        if len(letraIni) == 1:
            listaFechas=[]
            for x in lista:
                inicialLista=x.split(",")[0][0]
                fecha=x.split(",")[2]
                if letraIni == inicialLista:
                    contador+=1
                    listaFechas.append(fecha)
                validado=True
            if contador == 0:
                resultado=f"No se encontraron nombres con la inicial {letraIni}"
            else:
                resultado= f"Fechas de nacimiento con la inicial {letraIni}\n" + '\n'.join(listaFechas)
        else:
            print("Ingresar solo letras de 1 caracter")
    return resultado