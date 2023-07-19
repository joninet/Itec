# Primer for: Almacenar en dos listas paralelas, nombres y sexos de 8 personas.
# Segundo for: Recorrerlas y guardar los nombres de las mujeres en una nueva lista.
# Mostrar los elementos de la lista resultante.
listaNombres = []
listaSexo = []
listaMujeres = []
for x in range(3):
    nombre = input("Nombre: ")
    listaNombres.append(nombre)
    sexo = input("SEXO: ")
    listaSexo.append(sexo)
for rec in range(len(listaSexo)):
    if listaSexo[rec] == "F":
        listaMujeres.append(listaNombres[rec])
print(listaMujeres)
