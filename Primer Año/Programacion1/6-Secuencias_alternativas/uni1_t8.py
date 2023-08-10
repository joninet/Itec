# Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.
seg = float(input("ingrese segundos"))

# min = seg // 60
# hor = seg // 3600
# dias = seg // 86400

# print("en minutos ", min)
# print("en horas ", hor)
# print("en dias ", dias)

totalSegundos = seg
segXdia = 24 * 60 * 60
dias = totalSegundos // segXdia
resto = totalSegundos - (dias * segXdia)
segXhora = 60 * 60
horas = resto // segXhora
resto = resto - (horas * segXhora) 
segXmin = 60
minutos = resto // segXmin
segundos = resto - (minutos * segXmin)
print(totalSegundos, "segundos equivalen a ", dias, "horas")
