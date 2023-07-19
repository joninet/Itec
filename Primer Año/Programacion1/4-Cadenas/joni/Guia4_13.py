#Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez) y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).
frase = input("ingrese nombre: ")
frase= frase.split()
print(frase)
frase = frase[1].capitalize() + ", " + frase[0].capitalize()
print(frase)