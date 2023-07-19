#Pedir dos nombres y edades respectivas y luego construir una sola cadena con un texto que muestre el nombre del mayor y cuanto le lleva al menor. (Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')
nombre1= input("ingrese nombre: ")
edad1= int(input("Ingrese edad: "))
nombre2= input("ingrese nombre: ")
edad2= int(input("Ingrese edad: "))

if edad1 >= edad2:
    resultado = edad1 - edad2
    print(nombre1,"le lleva", resultado, "años a", nombre2)
else:
    resultado = edad2 - edad1
    print(nombre2,"le lleva", resultado, "años a", nombre1)