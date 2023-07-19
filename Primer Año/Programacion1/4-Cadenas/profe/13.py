# Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez) y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).
nombre = 'Juan Perez'
nombrePila, apellido = nombre.split()
print(nombrePila)
print(apellido)
print(apellido + ', ' + nombrePila)