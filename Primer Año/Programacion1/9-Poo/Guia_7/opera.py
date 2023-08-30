class Operacion: # clase abstracta
    def pedirDosNumeros(self):
        self.n1 = int(input('Número 1: '))
        self.n2 = int(input('Número 2: '))

    def operar(self): # método abstracto
        self.resultado = None

    def mostrarResultado(self):
        print(self.resultado)
    
class Suma(Operacion):
    def operar(self):
        self.resultado = self.n1 + self.n2

class Resta(Operacion):
    def operar(self):
        self.resultado = self.n1 - self.n2

if __name__ == "__main__":
    # solamente se ejecuta cuando este programa es el módulo principal, es decir, donde comienza la ejecución
    s = Suma()
    s.pedirDosNumeros()
    s.operar()
    s.mostrarResultado()

    r = Resta()
    r.pedirDosNumeros()
    r.operar()
    r.mostrarResultado()

    o = Operacion()
    o.pedirDosNumeros()
    o.operar()
    o.mostrarResultado()