class Animal: # clase ancestro o madre o superclase (generalización)
    def ponerNombre(self, n):
        self.nombre = n

class Gato(Animal):
    pass

class Perro(Animal):
    pass

michi = Gato()
michi.ponerNombre('Minina')
print(f'El gato se llama {michi.nombre}')

#------------------------------------------------------------------------------------------------

class Animal: # clase ancestro o madre o superclase (generalización)
    def __init__(self, n):
        self.nombre = n

    def habla(self): # método abstracto
        # sirve para indicar que DEBE ser definido en las clases hijas
        pass

class Gato(Animal):
    def __init__(self, n, f):
        super().__init__(n)
        self.familia = f

    def habla(self):
        print('miauuuu')

class Perro(Animal):
    def __init__(self, n):
        super().__init__(n)

    def habla(self):
        print('guauuuu')

michi = Gato('Minina', 'felinos')
print(f'El gato se llama {michi.nombre} y es de la familia {michi.familia}')
bobby = Perro('Bobby')
bobby.habla()

#-----------------------------------------------------------------------------------------

class Operacion(): # clase abstracta: solamente existe para ser heredada NUNCA instanciada
    def pedirNumeros(self):
        self.n1 = int(input('Ingrese el primer número: '))
        self.n2 = int(input('Ingrese el segundo número: '))

    def operar(self):# método abstracto
        # NO sirve para nada mas que sobreescribirlo (polimorfismo)
        self.resultado = None

    def mostrarResultado(self):
        print(self.resultado)

class Suma(Operacion):
    def operar(self):
        self.resultado = self.n1 + self.n2

class Resta(Operacion):
    def operar(self):
        self.resultado = self.n1 - self.n2

s = Suma()         
s.pedirNumeros()
s.operar()
s.mostrarResultado()
r = Resta()
r.pedirNumeros()
r.operar()
r.mostrarResultado()

