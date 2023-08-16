# password0 = inputStr('Password (entre 5 y 8 caracteres): ', 5, 8)
# password1 = inputStr('Password (al menos 4): ', 4)
# password2 = inputStr('Password (a lo sumo 5): ', maxi=5)
# password3 = inputStr('Password (sin rango): ')

"""def inputStr(msg, miniMo=0, maxiMo=None):
    validacion = False
    while not validacion:
        contra = input(msg)
        if miniMo != 0 and maxiMo != None and len(contra) > miniMo and len(contra) < maxiMo:
            print("contraseña correcta")
            validacion = True
        elif miniMo != 0 and maxiMo == None and len(contra) >= miniMo:
            print("contraseña correcta")
            validacion = True
        elif miniMo == 0 and maxiMo != None and len(contra) <= maxiMo:
            print("contraseña correcta")
            validacion = True
        elif miniMo == 0 and maxiMo == None:
            print("contraseña correcta")
            validacion = True
        else:
            print("ingresar una contraseña correcta")"""

def inputStr(msg, mini=0, maxi=10**308):
    validado = False
    while not validado:
        s = input(msg)
        if mini <= len(s) <= maxi:
            validado = True
        else:
            print(f'Debe tener una longitud entre {mini} y {maxi}') 
    return s 

# Ejemplo de uso de la función:
password0 = inputStr('Contraseña (entre 5 y 8 caracteres): ', 5, 8)
password1 = inputStr('Contraseña (al menos 4): ', 4)
password2 = inputStr('Contraseña (a lo sumo 5): ', maxiMo=5)
password3 = inputStr('Contraseña (sin rango): ')
