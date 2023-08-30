#Usando las clases Operacion y Suma, definir otra que se llame Promedio y utilizarla.
from opera import Suma

class Promedio(Suma):
    def promediar(self):
        return self.resultado // 2
    
p = Promedio()
p.pedirDosNumeros()
p.operar()
print(p.promediar())