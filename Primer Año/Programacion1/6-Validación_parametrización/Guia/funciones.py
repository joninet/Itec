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
