#La cantidad de personas nacidas en un país ingresado por el usuario.

personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]
paisUsuario = input("Ingrese Pais: ")
contador = 0
for paises in personas:
    paisL = paises.split(",")
    pais = paisL[1]
    paisBB = pais.find("(")
    paisB = pais[:paisBB]
    if paisUsuario == paisB:
        contador += 1
print("la cantidad de personas de", paisUsuario, "son", contador)
