# Pedir dos nombres y edades respectivas y luego construir una sola cadena con un texto que muestre el nombre del mayor y cuanto le lleva al menor. (Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')
# salida -> 'Juan le lleva 7 años a Pedro'

nombre1 = 'Juan'
edad1 = 12
nombre2 = 'Pedro'
edad2 = 15

if edad1 > edad2:
    salida = nombre1 + " le lleva " + str(edad1-edad2) + " años a " + nombre2
else:
    salida = nombre2 + " le lleva " + str(edad2-edad1) + " años a " + nombre1

print(salida)
