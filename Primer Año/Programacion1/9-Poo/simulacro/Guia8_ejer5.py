class Asignatura:
    def __init__(self,nombre,nota) -> None:
        self.nombre=nombre
        self.nota=nota
    def setNota(self,notaNueva):
        self.nota=notaNueva
    def getNota(self):
        return self.nota
    def calificacion(self):
        if self.nota >= 4:
            return f"Aprobado"
        else:
            return f"Reprobado"
    def getAsignatura(self):
        return self.nombre
    
class Alumno:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
        self.listaAsignaturas=[]
    def setNombre(self,nombreNuevo):
        self.nombre=nombreNuevo
    def getNota(self):
        return self.nombre
    def setEdad(self,edadNuevo):
        self.nombre=edadNuevo
    def getedad(self):
        return self.edad
    def Promedio(self):
        promedio=0
        for prom in self.listaAsignaturas:
            promedio+=prom.nota
        return promedio/len(self.listaAsignaturas)
    def agregarAsignatura(self):
        asignaturaNueva=input("Ingresar asignatura Nueva: ")
        for asignatura in self.listaAsignaturas:
            if asignatura.getAsignatura() == asignaturaNueva:
                print("la asignatura ya existe")
                return
        notaNueva=int(input("Ingresar Nota: "))
        alum=Asignatura(asignaturaNueva,notaNueva)
        self.listaAsignaturas.append(alum)
    def mostrarTodo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Asignaturas que curso: ")
        for asignaturas in self.listaAsignaturas:
            print(f"Nombre: {asignaturas.nombre}, Nota {asignaturas.nota}, {asignaturas.calificacion()}")

alumno1=Alumno("Jonathan",35)
alumno1.agregarAsignatura()
alumno1.agregarAsignatura()
alumno1.mostrarTodo()
print(f"Promedio: {alumno1.Promedio()}")

