from metodos_cadenas import *
nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
nacidos2018 = "Liam,19837,m,Noah,18267,m,Michael,14516,m,James,13525,m,Oliver,13389,m,Emma,18688,f,Olivia,17921,f,Ava,14924,f,Isabella,14464,f,Sophia,13928,f"

m2008, f2008 = ordenarLista(nacidos2008)
m2018, f2018 = ordenarLista(nacidos2018)
listaUnifi = m2008 + f2008 + m2018 + f2018
# ['Liam 19837 m', 'Noah 18267 m', 'Michael 14516 m', 'James 13525 m', 'Oliver 13389 m']
validadar = False
while not validadar:
    sexo = input("Ingresar Sexo m/f: ")
    if sexo == "f":
        posi = inputInt("Ingrese posicion hasta 5: ", 0, 5)
        n1, c1, s1 = buscarPosicion(f2008, posi)
        n2, c2, s2 = buscarPosicion(f2018, posi)
        diferencia = c1-c2
        if diferencia > 0:
            print(
                f"{diferencia} nacimientos de Mujeres más del primero del ranking de 2008 {n1} sobre {n2}")
        elif diferencia < 0:
            print(
                f"{diferencia} nacimientos de Mujeres más del primero del ranking de 2018 {n2} sobre {n1}")
        else:
            print(f"{diferencia} nacimientos de Mujeres son iguales {n1} {n2}")
        validadar = True
    elif sexo == "m":
        posi = inputInt("Ingrese posicion hasta 5: ", 0, 5)
        n1, c1, s1 = buscarPosicion(m2008, posi)
        n2, c2, s2 = buscarPosicion(m2018, posi)
        diferencia = c1-c2
        if diferencia > 0:
            print(
                f"{diferencia} nacimientos de Varone más del primero del ranking de 2008 {n1} sobre {n2}")
        elif diferencia < 0:
            print(
                f"{diferencia} nacimientos de Varones más del primero del ranking de 2018 {n2} sobre {n1}")
        else:
            print(f"{diferencia} nacimientos de Varones son iguales {n1} {n2}")
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
print(f"Nombres que se repiten: {buscarRepetidos(listaUnifi)}")
