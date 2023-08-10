# Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad
nom = input("ingrese nombre: ")
sig = input("Ingrese signo ><: ")

if sig == ">":
    print(nom, "es mayor de edad")
elif sig == "<":
    print(nom, "es menor de edad")
else:
    print("Ingrese un signo correcto")
