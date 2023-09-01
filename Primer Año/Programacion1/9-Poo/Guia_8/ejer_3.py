#Crea las siguientes clases (cada una en su archivo): 
 #Motor: con métodos para arrancar el motor y apagarlo. 
 #Rueda: con métodos para inflar la rueda y desinflarla. 
 #Ventana: con métodos para abrirla y cerrarla. 
 #Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
 #Coche: con un motor, cuatro ruedas y dos puertas;  con los métodos que te parezcan 
class Ventana:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.estado = "cerrada"

    def abrirVentana(self):
        self.estado = "abierta"
        return f"Se abrió la ventana {self.ubicacion}"

    def cerrarPuerta(self):
        self.estado = "cerrada"
        return f"Se cerró la ventana {self.ubicacion}"

    def obtenerEstado(self):
        return f"La ventana {self.ubicacion} está {self.estado}"
class Puerta(Ventana):  # Puerta hereda de Ventana
    def __init__(self,):
        super().__init__()

    def abrirPuerta(self):
        self.estado = "abierta"
        return f"Se abrió la puerta {self.ubicacion}"

    def cerrarPuerta(self):
        self.estado = "cerrada"
        return f"Se cerró la puerta {self.ubicacion}"

    def obtenerEstado(self):
        return f"La puerta {self.ubicacion} está {self.estado}"


class Auto():
    def __init__(self):
        self.puertaIzquierda = Puerta("izquierda")
        self.puertaDerecha = Puerta("derecha")

fiesta = Auto()
