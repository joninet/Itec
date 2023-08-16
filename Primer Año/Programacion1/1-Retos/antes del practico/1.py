# Dados estos datos desordenados, encontrar los sueldos y obtener el total.
sueldos = "Pedro$120.000, Ana(frontend)$512.700, el portero$175.120, el pibe del backend(capaz hay que actualizarle!)$371.459, revisar bien el total de erogaciones!"
lista = sueldos.split(",")
sueldoTotal = 0
for rec in lista:
    sueldo = rec.find("$")
    if sueldo != -1:
        listaSueldo = rec.split("$")[1]
        punto = listaSueldo.find(".")
        suma = listaSueldo[:punto]+listaSueldo[punto+1:]
        sueldoTotal += int(suma)
  print(sueldoTotal)
