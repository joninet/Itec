#El nombre de pila de la persona más joven de Europe.
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
nombreBusc = ""
contador = 0
for rec in personas:
    Euro = rec.find("Europe")
    # print(Euro)
    if Euro != -1:
        buscado = rec.split(",")
        buscado = buscado[2].split("-")
        fecha = int(buscado[2])
        if fecha > contador:
            contador = fecha
            buscarN = rec.split(",")
            buscarN = buscarN[0].split(" ")
            BuscarN = buscarN[0]
            nombreBusc = buscarN

print("La persona más joven de Europe es", nombreBusc[0])
