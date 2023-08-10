#input de fechas (validar formato y devolver año, mes y día como enteros), debe forzar un formato estricto, por ejemplo dd/mm/aaaa.
def validarFecha(msg):
    validado=False
    while not validado:
        fecha=input(msg)
        buscarB=fecha.find("/")
        if buscarB != -1:
            try:
                dia,mes,año=fecha.split("/")
                if len(dia) == 2 and int(dia) <= 31 and int(mes) <= 12 and len(mes) == 2 and len(año) == 4:
                    print(int(dia),int(mes),int(año))
                else:
                    print("ingresar formato de fecha valido dd/mm/aaaa")
            except:
                print("ingresar formato de fecha valido dd/mm/aaaa")
ingreso=validarFecha("ingresar fecha con este formato dd/mm/aaaa: ")

#len(dia)==2 and len(mes)==2


