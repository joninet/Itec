from funciones import *

nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
nacidos2018 = "Liam,19837,m,Noah,18267,m,Michael,14516,m,James,13525,m,Oliver,13389,m,Emma,18688,f,Olivia,17921,f,Ava,14924,f,Isabella,14464,f,Sophia,13928,f"

m2008, f2008 = armoListaNueva(nacidos2008)
m2018, f2018 = armoListaNueva(nacidos2018)
m2008.sort(key=ordenolistaMayor_menor, reverse=True)
f2008.sort(key=ordenolistaMayor_menor, reverse=True)
m2018.sort(key=ordenolistaMayor_menor, reverse=True)
f2018.sort(key=ordenolistaMayor_menor, reverse=True)

listaUnifi = m2008 + f2008 + m2018 + f2018
# ['Liam 19837 m', 'Noah 18267 m', 'Michael 14516 m', 'James 13525 m', 'Oliver 13389 m']
validadar = False
while not validadar:
    sexo = input("Ingresar Sexo m/f: ")
    if sexo == "f":
        obtenerDiferenciaNac("Mujeres", f2008, f2018)
        validadar = True
    elif sexo == "m":
        obtenerDiferenciaNac("Varones", m2008, m2018)
        validadar = True
    else:
        print("ingresar un sexo valido")
        validadar = False
ingresoVal = False
while not ingresoVal:
    ingresoNom = input("Ingresar inicial a Buscar: ")
    if len(ingresoNom) == 1 and ingresoNom.isalpha():
        unaLista = unificar(ingresoNom, *m2008, *m2018, *f2008, *f2018)
        print(f"Nombres con {ingresoNom}: {unaLista}")
        ingresoVal = True
    else:
        print("Ingresar un solo caracter (solo letras)")
print(f"Nombres que se repiten: {buscarRepetido