# Dadas dos listas con nombres, una de varones y otra de mujeres, solicitar una letra inicial y mostrar los nombres que comiencen con ella en ambas listas en una string concatenada con guiones.
mujeres = ['Lisa', 'Ema', 'Juana', 'Ester']
varones = ['Eduardo', 'Pedro']
inicial = input("Ingresar la inicial a buscar en mayuscula: ")
nombresI = ""

for nombres in mujeres:
    letra = nombres[0]  # me muestra solo la primera letra
    if letra == inicial:  # comparo con la inicial que le pedi anteriormente
        nombresI += nombres + "-"  # la agrego a la variable
for nombres in varones:
    letra = nombres[0]
    if letra == inicial:
        nombresI += nombres + "-"
print(nombresI[:len(nombresI) - 1])
