#Crea las siguientes clases (cada una en su archivo): 
 #Motor: con métodos para arrancar el motor y apagarlo. 
 #Rueda: con métodos para inflar la rueda y desinflarla. 
 #Ventana: con métodos para abrirla y cerrarla. 
 #Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
 #Coche: con un motor, cuatro ruedas y dos puertas;  con los métodos que te parezcan 
class Puerta:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.ventana = Ventana(ubicacion)

    def abrirPuerta(self):
        print(f"puerta {self.ubicacion} Abierta")

    def cerrarPuerta(self):
        print(f"puerta {self.ubicacion} Cerrada y ventana {self.ubicacion} cerrada")

class Ventana:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion

    def abrirVentana(self):
        print(f"Ventana {self.ubicacion} Abierta")

    def cerrarVentana(self):
        print(f"Ventana {self.ubicacion} Cerrada")

class inflarRuedas:
    def __init__(self,ubicacion):
        self.ubicacion=ubicacion

    def inflarRueda(self):
        print(f"Rueda {self.ubicacion} inflada")

    def desinflarRueda(self):
        print(f"Rueda {self.ubicacion} desinflada")

class Motor:
    def __init__(self,arrancar):
        self.arrancar=arrancar

    def arrancarMotor(self):
        print(f"Se arranco Motor")

    def apagarMotor(self):    
        print(f"Se apago el Motor")

class Auto:
    def __init__(self):
        self.puertaIzquierda = Puerta("izquierda")
        self.puertaDerecha = Puerta("derecha")
        self.ruedaDelDer = inflarRuedas("Delantera Derecha")
        self.ruedaDelIzq = inflarRuedas("Delantera Izquierda")
        self.ruedaTraDer = inflarRuedas("Trasera Derecha")
        self.ruedaTraIzq = inflarRuedas("Trasera Izquierda")
        self.MotorEstado = Motor("")

fiesta = Auto()
fiesta.puertaIzquierda.abrirPuerta()
fiesta.puertaDerecha.cerrarPuerta()
fiesta.puertaDerecha.ventana.abrirVentana()
fiesta.ruedaTraIzq.inflarRueda()
fiesta.MotorEstado.apagarMotor()


