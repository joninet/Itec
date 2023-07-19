# Tomar una fecha en formato "DD-MM-AAAA" y convertirla en "D de [Mes] de AAAA".

# Salida: 3 de junio del 1965 (si el día tiene una sola cifra hay que sacar el cero)
meses = "01-enero 02-febrero 03-marzo 04-abril 05-mayo 06-junio 07-julio 08-agosto 09-septiembre 10-octubre 11-noviembre 12-diciembre"
Entrada = "13-06-1965"

meses = meses.split()#convierto en lista la cadena meses
dia, mes, ano = Entrada.split("-")#convierto en lista la cadena Entrada y le armo una variable a cada una
for rec in meses:#recorro en la lista meses
    buscar = rec.find(mes)#busco el numero del mes en el recorrido
    if buscar != -1:#pasan si se encontro
        mes = rec[buscar+3:]#buscamos apartiir de donde encontro y le sumo 3

if dia[0] == "0":
    dia = dia[1]
else:
    dia = dia
print(dia, "de", mes, "del", ano)
