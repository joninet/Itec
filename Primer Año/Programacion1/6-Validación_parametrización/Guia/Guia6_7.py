#input con opciones (Ejemplo: ‘Quiere ingresar datos (si/no)”?)
from funciones import inputInt
def inputChoice (opciones,msg,):
    op=opciones.split("/")
    for rec in range(len(op)):
        print(f"{rec+1}) {op[rec]}")
    ing=inputInt(msg, 1,len(op))
    return op[ing-1]
q = inputChoice("si/no/a veces","Ingresar una opcion: ")
print(q)
r = inputChoice("Rojo/Verde/Amarillo/Negro/Azul", "Ingresar una opcion: ")
print(r)
