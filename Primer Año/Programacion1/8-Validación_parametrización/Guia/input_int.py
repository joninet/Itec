def inputInt(msg, mini=-10**308, maxi=10**308):
    validado = False
    while not validado:
        try:
            n = int(input(msg))
            if mini <= n <= maxi:
                validado = True
            else:
                print('fuera de rango')
        except:
            print('ingreso inválido')
    return n