#6) Agregar al ejercicio 2 (clase Auto) un método que obtenga la antigüedad. 
#En el programa principal mostrar cuáles autos tienen más de 5 años.
class auto:
    def __init__(self, marca, año):
        self.marca=marca
        self.año=año
    def antiguedadAuto(self):
        antiguedad=2023 - self.año
        if antiguedad >= 5:
            mayorCinco=f"El auto {self.marca} tiene mas de 5 años"
        else:
            mayorCinco=f"El auto {self.marca} tiene menos 5 años"
        return mayorCinco
a=input("Ingresar marca del auto: ")
validado=False
while not validado:
    try:
        aA=int(input("ingresar el año: "))
        validado=True
    except:
        print("Ingresar solo caracteres numericos")
ingresoAuto=auto(a, aA)
print(ingresoAuto.antiguedadAuto())
