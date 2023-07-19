#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad. Funciones de carga y cálculo de edad.
def carga():
    listaNom=[]
    listaNac=[]
    entrada="si"
    while entrada == "si":
        nombre=input("ingresar nombre: ")
        listaNom.append(nombre)
        fecha=input("Ingresar fecha dd/mm/aaaa: ")
        listaNac.append(fecha)
        entrada=input("Agregar mas si/no: ")
    return listaNom,listaNac
nombres,nacimiento=carga()
def mayores(nom,nac):
    listaMayor=[]
    aH=2023
    mH=6
    dH=3
    for rec in range(len(nac)):
        reco=nac[rec]
        aD,aM,aA=reco.split("/")
        edad = aH - int(aA)
        if int(aM) > mH or int(aM) == mH and int(aD) > dH:
            edad -= 1
        if edad >= 18:
            mayor=nom[rec]
            listaMayor.append(mayor)
    return listaMayor
print(mayores(nombres,nacimiento))
