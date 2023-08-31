#Crea las siguientes clases (cada una en su archivo): 
 #Motor: con métodos para arrancar el motor y apagarlo. 
 #Rueda: con métodos para inflar la rueda y desinflarla. 
 #Ventana: con métodos para abrirla y cerrarla. 
 #Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta. 
 #Coche: con un motor, cuatro ruedas y dos puertas;  con los métodos que te parezcan 
class Motor:
    def __init__(self):
        self.encendido=False
    def arrancarMotor(self):
        if not self.encendido:
            self.encendido=True
            return f"El motor se encendio correctamente"
        else:
            return f"El motor ya esta encendido"
    def apagarMotor(self):
        if self.encendido:
            self.encendido=False
            return f"El motor se apago correctamente"
        else:
            return f"El motor ya esta apagado"
class Rueda:
    def __init__(self):
        self.Inflado=False
    def inflarRueda(self):
        if not self.Inflado:
            self.Inflado=True
            return f"Se inflaron las ruedas correctamente"
        else:
            return f"las ruedas ya estan infladas"
    def desinflarRuedas(self):
        if self.Inflado:
            self.Inflado=False
            return f"Se desinflaron las ruedas correctamente"
        else:
            return f"las ruedas ya estan desinfladas"    
