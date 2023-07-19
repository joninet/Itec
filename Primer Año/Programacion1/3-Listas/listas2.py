nombres = ["juan", "Ana", "luis"]
edades = [32, 87, 12]
print(personas[0][1])
# personas = [[juan, 32], ["Ana", 87], ["Luis", 12]]
for i in range(len(nombres)):
    if edades[i] >= 18: 
        print(nombres[i])


