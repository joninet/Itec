# 3)La persona más joven de Europe es Willy.
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
contador = 0
joven = "Europe"
for rec in personas:
    buscar = rec.find(joven)
    if buscar != -1:
        edad = rec.split(",")[2]
        edad = int(edad.split("-")[2])
        if edad > contador:
            nombre = rec.split(",")[0]
            nombre = nombre.split()[0]
            contador = edad

print("La persona más joven de", joven, "es", nombre)
