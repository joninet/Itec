#Los apellidos de las personas nacidas antes de un año solicitado al usuario.
print("1)")
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
añosS = int(input("Ingrese año:"))
print("Los apellidos de las personas nacidas antes del 2000 son:")
# Los apellidos de las personas nacidas antes de un año solicitado al usuario.
for rec in personas:
    fecha = rec.split(",")
    buscar = fecha[2].split("-")
    apellido = fecha[0].split()
    año = int(buscar[2])
    if año < añosS:
        print(apellido[1])



