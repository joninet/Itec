# Convierte una lista en cadena, solicitando al usuario el separador a utilizar.
lista = ["quico", 123, "mesa"]
separador = "<->"
cadena = ""
for rec in lista:
    cadena += str(rec) + separador
print(cadena)
