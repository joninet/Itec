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
            for x in lista:
                inicialLista=x.split(",")[0][0]
                fecha=x.split(",")[2]
                if letraIni == inicialLista:
                    contador+=1
                    print(fecha)
            if contador == 0:
                print(f"No se encontraron nombres con la inicial {letraIni}")
        else:
            print("se debe ingresar solo un caracter")
    return 