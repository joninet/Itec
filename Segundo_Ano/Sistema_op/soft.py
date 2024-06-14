def admPeticiones(listaSectores, metodo, ultimoSector):
    colaPeticiones = []
    posicionActual = ultimoSector
    totalMov = 0
    listaCopia = listaSectores[:]

    if metodo == 0:  
        colaPeticiones = listaCopia
        totalMov = sum(abs(colaPeticiones[i] - colaPeticiones[i - 1]) for i in range(1, len(colaPeticiones)))

    elif metodo == 1:  
        while listaCopia:
            sectorCercano = min(listaCopia, key=lambda x: abs(x - posicionActual))
            colaPeticiones.append(sectorCercano)
            listaCopia.remove(sectorCercano)
            totalMov += abs(sectorCercano - posicionActual)
            posicionActual = sectorCercano

    elif metodo == 2 or metodo == 3:  
        direccion = 1  
        if metodo == 3:
            listaCopia.sort()  
        while listaCopia:
            if direccion == 1:
                if listaCopia:  
                    sectorCercano = min(listaCopia, key=lambda x: x - posicionActual)
                    while sectorCercano not in listaCopia:
                        sectorCercano = max(listaCopia, key=lambda x: x - posicionActual)
                else:
                    break  

            else:
                if listaCopia: 
                    sectorCercano = max(listaCopia, key=lambda x: x - posicionActual)
                    while sectorCercano not in listaCopia:
                        sectorCercano = min(listaCopia, key=lambda x: x - posicionActual)
                else:
                    break  

            colaPeticiones.append(sectorCercano)
            listaCopia.remove(sectorCercano)
            totalMov += abs(sectorCercano - posicionActual)
            posicionActual = sectorCercano
    
    else:
        return 0

    return colaPeticiones, totalMov


#codigo modificable segun necesidades
listaEjemplo = [10, 50, 80, 100, 120, 200, 250]
ultimoSector = 75
metodo = 0 # 0=FCFS, 1=SSTF, 2=SCAN, 3=C-SCAN
#---fin---

resultado = admPeticiones(listaEjemplo, metodo, ultimoSector)
if resultado == 0:
    print("Opcion de metodo invalido")
else:
    print(f"Cola de peticiones: {resultado[0]} - Total de movimientos: {resultado[1]}")