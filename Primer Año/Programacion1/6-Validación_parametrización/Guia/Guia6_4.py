# password0 = inputStr('Password (entre 5 y 8 caracteres): ', 5, 8)
# password1 = inputStr('Password (al menos 4): ', 4)
# password2 = inputStr('Password (a lo sumo 5): ', maxi=5)
# password3 = inputStr('Password (sin rango): ')

def inputStr(msg, miniMo=None, maxiMo=None):
    validacion = False
    while not validacion:
        contra = input(msg)
        if miniMo != None and maxiMo != None and len(contra) > miniMo and len(contra) < maxiMo:
            print("contraseña correcta")
            validacion = True
        elif miniMo != None and maxiMo == None and len(contra) >= miniMo:
            print("contraseña correcta")
            validacion = True
        elif miniMo == None and maxiMo != None and len(contra) <= maxiMo:
            print("contraseña correcta")
            validacion = True
        elif miniMo == None and maxiMo == None:
            print("contraseña correcta")
            validacion = True
        else:
            print("ingresar una contraseña correcta")


# Ejemplo de uso de la función:
password0 = inputStr('Contraseña (entre 5 y 8 caracteres): ', 5, 8)
password1 = inputStr('Contraseña (al menos 4): ', 4)
password2 = inputStr('Contraseña (a lo sumo 5): ', maxiMo=5)
password3 = inputStr('Contraseña (sin rango): ')
