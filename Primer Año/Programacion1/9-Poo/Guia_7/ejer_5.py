# Hacer una clase Persona con dos métodos: uno para saber si es mayor de edad y el otro para determinar si es varón o 
# mujer. En el programa principal instanciarlo, tomar nombre, edad y sexo, y finalmente mostrar un cartel que diga por 
# ejemplo ‘Juan es mayor de edad y es varón’.
class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    def mayorEdad(self):
        if self.edad >= 18:
            resultado=f"{self.nombre} es mayor de edad"
        else:
            resultado=f"{self.nombre} es menor de edad"
        return resultado
    def verificarSexo(self):
        if self.sexo == "M":
            resultado="Varon"
        else:
            resultado="Mujer"
        return resultado

n=input("ingresar nombre: ")
validado=False
while not validado:
    try:
        e=int(input("ingresar edad: "))
        validado=True
    except:
        print("Ingresar solo caracteres numericos")

validado=False
while not validado:
    s=input("Ingresar Sexo M/F: ").upper()
    if s=="M" or s=="F":
        validado=True
    else:
        print("Ingresar solo M o F")

personaIngreso=Persona(n,e,s)
print(f"{personaIngreso.mayorEdad()} y es {personaIngreso.verificarSexo()}")
