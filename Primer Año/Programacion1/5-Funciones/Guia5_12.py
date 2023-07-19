#Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).
def nombreInvertido(ingreso):
    nom=ingreso.split(" ")
    nom=nom[1]+", "+nom[0]
    return nom
ingresoNom=input("ingresar nombre y apellido: ")
print(nombreInvertido(ingresoNom))
