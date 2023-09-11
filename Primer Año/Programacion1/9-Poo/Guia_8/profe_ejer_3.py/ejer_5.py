"""Implementar la clase Asignatura que represente el nombre de una asignatura y la nota correspondiente obtenida. Las operaciones son:
Constructor que acepte como parámetros el nombre de la asignatura y la nota obtenida.
Métodos para modificar la nota (setNota) y para consultar la nota (getNota).
Método que nos devuelva “Aprobado” si la nota es mayor o igual a 4 o “Reprobado” si la nota es menor que 4.
Método para consultar el nombre de la asignatura.
Implementar la clase Alumno que incluya una colección de Asignaturas a las que el alumno ha asistido. Además de incluir los atributos nombre y edad. Las operaciones disponibles sobre el alumno son:
Constructor que acepte como parámetro el nombre del alumno y edad.
Métodos para modificar el nombre (setNombre) y para consultarlo (getNombre).
Métodos para modificar y consultar la edad.
Método que nos devuelva el promedio del alumno.
Método para agregar una Asignatura a su plan de estudio; verificar que la asignatura no exista previamente en el arreglo de este Alumno.
Implementar la clase Aplicación para hacer uso de las clases Alumno y Asignatura.
Crear 3 alumnos (Tres instancias de la clase Alumno) con sus respectivos nombre y edad.
Para cada alumno establecer sus asignaturas y la nota obtenida.
Imprimir en pantalla:
1.Nombre del alumno.
2.Edad.
3.Asignaturas que cursó:
Nombre de la asignatura.
Nota obtenida.
Si es una asignatura aprobada o no.
4.Promedio del alumno"""
class Asignatura:
    def __init__(self,nombreAsig,nota) -> None:
        self.nombreAsig=nombreAsig
        self.nota=nota
    def setNota(self,notaNueva):
        self.nota=notaNueva
    def getNota(self):
        return self.nota
    def consultarAsignatura(self):
        return self.nombreAsig
    def calificacion(self):
        if self.nota >= 4:
            return f"Aprobado"
        else:
            return f"Desaprobado"
"""Implementar la clase Alumno que incluya una colección de Asignaturas a las que el alumno ha asistido. Además de incluir los atributos nombre y edad. Las operaciones disponibles sobre el alumno son:
Constructor que acepte como parámetro el nombre del alumno y edad.
Métodos para modificar el nombre (setNombre) y para consultarlo (getNombre).
Métodos para modificar y consultar la edad.
Método que nos devuelva el promedio del alumno.
Método para agregar una Asignatura a su plan de estudio; verificar que la asignatura no exista previamente en el arreglo de este Alumno.
Implementar la clase Aplicación para hacer uso de las clases Alumno y Asignatura.
Crear 3 alumnos (Tres instancias de la clase Alumno) con sus respectivos nombre y edad.
Para cada alumno establecer sus asignaturas y la nota obtenida.
Imprimir en pantalla:
1.Nombre del alumno.
2.Edad.
3.Asignaturas que cursó:
Nombre de la asignatura.
Nota obtenida.
Si es una asignatura aprobada o no.
4.Promedio del alumno"""
class Alumno(Asignatura):
    def __init__(self, nombreAsig, nota,nombre,edad) -> None:
        super().__init__(nombreAsig, nota)
        self.nombre=nombre
        self.edad=edad
        self.listaAsignaturas=[]
        cargo=Asignatura(nombreAsig,nota)
        self.listaAsignaturas.append(cargo)

    def setNombre(self,nombreNuevo):
        self.nota=nombreNuevo
    def getNombre(self):
        return self.nombre
    def setNombre(self,edadNuevo):
        self.nota=edadNuevo
    def getNombre(self):
        return self.edad
    def Promedio(self):
        suma=0
        for rec in self.listaAsignaturas:
            suma+=rec.nota
        return suma/len(self.listaAsignaturas)
    def agregarAsignatura(self,agregoAsig,nota):
        for rec in self.listaAsignaturas:
            if agregoAsig == rec.nombreAsig:
                return print("Ya existe la asignatura")
            else:
                cargo=Asignatura(agregoAsig,nota)
                self.listaAsignaturas.append(cargo)
                return print("se agrego la asignatura")
    def listarAsignaturas(self):
        for rec in self.listaAsignaturas:
            cali=rec.calificacion()
            print(f"{rec.nombreAsig} - {rec.nota} - {cali}")
    
Alumno1=Alumno("Ingles",8,"Jonathan",35)
Alumno1.agregarAsignatura("Ingles",8)
Alumno1.agregarAsignatura("Mate",3)
Alumno1.agregarAsignatura("Lengua",8)
print(Alumno1.Promedio())
Alumno1.listarAsignaturas()




