from dataclasses import dataclass

@dataclass
class Empleado:
    nombre: str
    sueldo: int

@dataclass
class Programador(Empleado):
    lenguaje: str

    def setProyecto(self, proyecto):
        self.proyecto = proyecto

    def __str__(self):
        return f"Nombre: {self.nombre}. Salario: {self.sueldo}. Proyecto: {self.proyecto}. Lenguaje: {self.lenguaje}"
    
@dataclass
class Empresa:
    nombre: str
    rubro: str
    listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
    listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
    listaProgramadores = []

    def __str__(self): # dunder: mẽtodo especial para salida formateada
        return f"Empresa: {self.nombre}. Rubro: {self.rubro}"
    
    def agEmp(self, leng, nombre, proyecto):
        if leng in self.listaLenguajes:
            if leng == 'Python':
                salario = 1_475_000
            else:
                salario = 615_000
            prog = Programador(nombre, salario, leng)
            prog.setProyecto(proyecto)
            self.listaProgramadores.append(prog)    
        else:
            print(f'El lenguaje {leng} no es requerido. Debe ser uno de estos: {self.listaLenguajes}')

    def mostrarTodo(self):
        print()
        print(self)
        print('Programadores:')
        for p in self.listaProgramadores:
            print(p)

empresa = Empresa('iTecLabs', 'Soft Dev')
datos = [
    ['C#', 'Pedro', "Sistema Gallina SRL"],
    ['Python', 'Pablo', "Web Pollitos"],
    ['Ruby', 'Salvador', "Web Pollitos"],
    ['JavaScript', 'Ana', "Web Pollitos"]
]
for d in datos:
    empresa.agEmp(*d)
empresa.mostrarTodo()