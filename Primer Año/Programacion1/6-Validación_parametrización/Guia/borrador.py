abece = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
carac = "#$%&"

user = "hola"
contadorAbc = 0
for rec in user:
    buscarAbc = abece.find(rec)
    if buscarAbc >= 0:
        contadorAbc += 1
print(contadorAbc)
