from dataclasses import dataclass
@dataclass
class Asignatura:
    nombre: str
    nota: int
    def setNota(self,notaNueva):
        self.nota=notaNueva
        return f"Se modifico la nota"
    def getNota(self):
        return self.nota
    def Calificacion (self):
        if self.nota >= 4:
            return f"Aprobado"
        else:
            return f"desaprobado"
    def getNombre(self):
        return self.nombre
    
@dataclass
class Alumno:
    nombre: str
    edad: int
    listaAsignaturas=[]
    def setNombre(self,nombreNuevo):
        self.nombre=nombreNuevo
        return f"Se modifico el nombre"
    def getNombre(self):
        return self.nombre
    def setEdad(self,edadNuevo):
        self.edad=edadNuevo
        return f"Se modifico la edad"
    def getNombre(self):
        return self.edad
    def Promedio(self):
        promedio=0
        for recnota in self.listaAsignaturas:
            promedio+=recnota.nota
            return promedio / len(self.listaAsignaturas)
    def agregarAsignatura(self):
        validado=False
        while not validado:
            asigNueva=input("Ingresar asignatura nueva: ").lower()
            if asigNueva.isalpha():
                for asignatura in self.listaAsignaturas:
                    if asigNueva == asignatura.nombre:
                        return print(f"la asignatura ya existe")
                validado=False
                while not validado:
                    try:
                        notaNueva=int(input("Ingresar Nota: "))
                        agregoAsig=Asignatura(asigNueva,notaNueva)
                        self.listaAsignaturas.append(agregoAsig)
                        return print(f"Agregada correctamente")
                        validado=True
                    except:
                        print("Ingresar solo numeros")
            else:
                print("Ingresar solo letras")
    def mostrarTodo(self):
        print(f"Nombre Alumno: {self.nombre}")
        print(f"Edad: {self.edad}")
        print("Asignaturas que curso:")
        for asignatura in self.listaAsignaturas:
            print(f"Nombre: {asignatura.nombre}")
            print(f"Nota: {asignatura.nota}")
            print(f"{asignatura.Calificacion()}")
    
alumno1=Alumno("jonathan",35)
alumno1.agregarAsignatura()
alumno1.agregarAsignatura()
alumno1.agregarAsignatura()
alumno1.mostrarTodo()
alumno1.Promedio()
    