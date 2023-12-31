from funciones_new import *

personas = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-02-1994",
    "Adeline LaPadula,France,18-06-2002",
    "Willy Branscombe,Argentina,21-11-1997",
    "Diane Piffe,France,07-08-1993",
    "Britta Causbey,France,24-04-1991",
    "Elisabeth Cleeve,France,04-03-1991",
    "Rafael Ivanchenkov,France,28-04-2002",
    "Zerk Milsom,Norway,03-12-1994",
    "Adorne Ovington,United States,17-08-1991",
    "Kathryn Backshell,United States,04-03-1992",
    "Blake Colbeck,United States,18-01-1999",
    "Arron Bresnahan,United States,03-07-2001",
    "Deloria Dominguez,France,31-07-1990",
    "Grenville Aldersea,Argentina,11-01-2001",
    "Jemimah Haughian,Argentina,30-11-1998",
    "Con Gethen,United States,06-06-1992",
    "Roxie Igoe,France,31-03-2002",
    "Hollyanne Mottley,United States,05-01-1996",
    "Ambrosio Cadore,Norway,09-12-2002"
]

print(contar_ocurrencias_pais(personas, "Argentina"))
print("Opciones de Paises: Germany - United States - Norway - France")
validado=False
while not validado:
    pais_busqueda = input("Ingresa otro país además de Argentina: ")
    if pais_busqueda.isalpha():
        print(contar_ocurrencias_pais(personas, pais_busqueda))
        validado=True
    else:
        print("ERROR - Ingresar solo letras")
#----------------------
validado=False
while not validado:
    inicial_busqueda = input("Ingresa una inicial para buscar fechas de nacimiento: ")
    if len(inicial_busqueda) == 1 and inicial_busqueda.isalpha():
        print(fechas_nacimiento_con_inicial(personas, inicial_busqueda))
        validado=True
    else:
        print("ERROR - ingresar solo letras y de un caracter")