#Preguntar cuántas personas se van a cargar y luego solicitar sus edades, mostrando al final la edad promedi
personas=int(input("Cuantas personas cargas: "))
contador = 0
for i in range(personas):
    edad = int(input("Edad: "))
    contador = contador + edad
prom = contador / personas
print("El promedio de las edad es ", prom)