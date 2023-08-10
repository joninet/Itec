direcciones = ['Mitre 1234', '9 de Julio 345', 'Alvear 999', '9 de Julio 11']
contMi=0
contJu=0
contAl=0
for calle in direcciones:
    posEspacio= calle.find(" ",5)
    calle=calle[:posEspacio]
    if calle == "Mitre":
        contMi+=1
    elif calle == "9 de Julio":
        contJu+=1
    elif calle == "Alvear":
        contAl+=1
        
print("Mitre", contMi)
print("9 de Julio", contJu)
print("Alvear", contAl)