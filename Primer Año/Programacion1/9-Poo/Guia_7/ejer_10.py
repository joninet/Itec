#Usando las clases Operacion y Suma, definir otra que se llame Promedio y utilizarla.
class Operacion(): # clase abstracta: solamente existe para ser heredada NUNCA instanciada
    def pedirNumeros(self):
        validado=False
        while not validado:
            try:
                self.n1 = int(input('Ingrese el primer número: '))
                self.n2 = int(input('Ingrese el segundo número: '))
                validado=True
            except:
                print("Ingresar solo numeros")

    def operar(self):# método abstracto
        # NO sirve para nada mas que sobreescribirlo (polimorfismo)
        self.resultado = None

    def mostrarResultado(self):
        print(f"El resultado es: {self.resultado}")

class Suma(Operacion):
    def operar(self):
        self.resultado = self.n1 + self.n2

class Resta(Operacion):
    def operar(self):
        self.resultado = self.n1 - self.n2
class Promedio(Operacion):
    def operar(self):
        self.resultado = (self.n1 + self.n2) / 2
print("Suma")
s = Suma()         
s.pedirNumeros()
s.operar()
s.mostrarResultado()
print("Resta")
s = Resta()         
s.pedirNumeros()
s.operar()
s.mostrarResultado()
print("Promedio")
r = Promedio()
r.pedirNumeros()
r.operar()
r.mostrarResultado()