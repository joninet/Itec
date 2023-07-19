nombres = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana",
           "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"]
sexos = ["f", "f", "m", "f", "m", "f", "m"]
fechas = ["02/05/1943", "07/09/1984", "10/02/1971",
          "21/12/1967", "30/01/1982", "30/08/1995", "18/07/1959"]
contador = 0
nombreLargo = ""
for x in range(len(nombres)):
    nombreN = nombres[x].split(" ")
    nombreNN = nombreN[1]
    print(nombreNN)
    nombre2 = int(len(nombreNN))
    if nombre2 > contador:
        contador += nombre2
        nombreLargo = nombres[x].split(" ")
        nombreNN = nombreN[1]
print(contador)
