#3) Definir una clase Persona cuyo constructor reciba nombre y edad. El programa principal pedirá en forma repetitiva (hasta que no haya 
#más) los mismos datos, hará la instanciación de un objeto y lo agregará en una lista. Por lo tanto, los elementos de dicha lista serán 
#objetos y podrá mostrarse con recorrido por elemento o por índices.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
listaPersona=[]
validado="si"

while validado=="si":
    n=input("Ingresar Nombre: ")
    e=input("Ingresar Edad: ")
    agrego=Persona(n,e)
    listaPersona.append(agrego)
    validado=input("Agragar mas SI/NO: ")
for pers in listaPersona:
    print(f"{pers.nombre} tiene {pers.edad} años")