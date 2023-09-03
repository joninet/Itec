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
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def setNota(self,notaNueva):
        self.nota=notaNueva
        return f"La nota se cambio correctamente"

    def getNota(self):
        return self.nota
    
    def aprobadoReprobado(self):
        if 4 <= self.nota <= 10:
            return f"Aprobado"
        elif 1 <= self.nota < 4:
            return f"Reprobado"
        else:
            return f"la nota tiene que estar entre 1 y 10"
        
    def consultaAsignatura(self):
        return self.nombre
"""Implementar la clase Alumno que incluya una colección de Asignaturas a las que el alumno ha asistido. Además de incluir los atributos nombre y edad. Las operaciones disponibles sobre el alumno son:
Constructor que acepte como parámetro el nombre del alumno y edad.
Métodos para modificar el nombre (setNombre) y para consultarlo (getNombre).
Métodos para modificar y consultar la edad.
Método que nos devuelva el promedio del alumno."""
class Alumno(Asignatura):
    def __init__(self, nombre,nota,nombreAlumno,edadAlumno):
        super().__init__(nombre,nota)
        self.nombreAlumno=nombreAlumno
        self.edadAlumno=edadAlumno
        self.listaMaterias=[]

    def setNombre(self,nuevoNombreAlumno):
        self.nombreAlumno=nuevoNombreAlumno

    def getNombre(self):
        return self.nombreAlumno
    
    def setEdad(self,edadNueva):
        self.edadAlumno=edadNueva
        return f"La edad se cambio correctamente"

    def getEdad(self):
        return self.edadAlumno
    
    def agregarAsignaturasLista(self,nombre,nota):
        agregar=Asignatura(nombre,nota)
        self.listaMaterias.append(agregar)
        return f"Asignatura agregada a la lista"
    
    def Promedio(self):
        sumaNotas=0
        for notas in self.listaMaterias:
            sumaNotas += notas.getNota()
        return sumaNotas / len(self.listaMaterias)

joni=Alumno("Ingles",7,"Jonathan",35)
joni.agregarAsignaturasLista("matematica",3)
joni.agregarAsignaturasLista("lengua",6)
print(joni.Promedio())
print(joni.getNota(),joni.aprobadoReprobado(),joni.consultaAsignatura(),joni.setEdad(34),joni.getEdad())
        
    

