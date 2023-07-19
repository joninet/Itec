# Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo y mostrar el nombre de la persona que menos gana.
salarioMinimo = 100000000
nombreMin = ""
datos = "si"
while datos == "si":
    nombre = input("nombre")
    salario = int(input("salario: "))
    if salario < salarioMinimo:
        salarioMinimo = salario
        nombreMin = nombre
    datos = input("hay más Si/NO: ")
print(nombreMin, "es el del menor salario ", salarioMinimo)
