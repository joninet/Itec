# Usando inputStr(la función realizada en el ejercicio anterior), escribir una función que valide un nombre de usuario, agregando restricciones específicas, como por ejemplo que tenga al menos 8 caracteres en total, al menos una letra, al menos 1 dígito numérico y al menos 1 caracter especial entre estos: #, $, %,&.
def inputUser(msg):
    validado = False
    abece = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    carac = "#$%&"
    contadorAbc = -1
    contadorNum = -1
    contadorCara = -1
    while not validado:
        user = input(msg)
        if len(user) >= 8: 
            for rec in user:
                buscarAbc = abece.find(rec)
                buscarNum = num.find(rec)
                buscarCara = carac.find(rec)
                if buscarAbc >= 0:
                    contadorAbc += 1
                elif buscarNum >= 0:
                    contadorNum += 1
                elif buscarCara >= 0:
                    contadorCara += 1
            if contadorCara == -1:
               print("Le falta un caracter especial ")
            if contadorNum == -1:
                print("Le falta un caracter Numerico ")
            if contadorAbc == -1:
                print("Le falta por lo menos una letra")
            if contadorCara != -1 and contadorNum != -1 and contadorAbc != -1:
                print("usuario valido")
                validado = True
        else:
            print("el usuario tiene que tener al menos 8 caracteres")


usuario = inputUser(
    "Ingrese un nombre de usuario válido (debe contener como mínimo una letra, un dígito y al menos uno de estos caracteres especiales:  #, $, %,&):")
