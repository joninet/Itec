from input_choice import inputChoice

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje) -> None:
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje    
        
    def setProject(self, proyecto):
        self.proyecto = proyecto

    def getData(self):
        return self.proyecto, self.lenguaje


class Empresa:
    def __init__(self, nombre, rubro) -> None:
        self.nombre = nombre
        self.rubro = rubro
        self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores = []

    def agEmp(self):
        leng = input('Lenguaje: ')
        if leng in self.listaLenguajes:
            nombre = input('Nombre: ')
            if leng == 'Python':
                salario = 1_475_000
            else:
                salario = 615_000
            proyecto = inputChoice(self.listaProyectos, 'Proyecto')
            prog = Programador(nombre, salario, leng)
            prog.setProject(proyecto)
            self.listaProgramadores.append(prog)    
        else:
            print(f'El lenguaje {leng} no es requerido. Debe ser uno de estos: {self.listaLenguajes}')

    def mostrarTodo(self):
        print()
        print(f'Empresa: {self.nombre}. Rubro: {self.rubro} ')
        print('Programadores:')
        for p in self.listaProgramadores:
            print(f'{p.nombre}. Salario: {p.sueldo}. Sistema: {p.getData()[0]}. Lenguaje: {p.getData()[1]}')

empresa = Empresa('iTecLabs', 'Soft Dev')
for i in range(4):
    empresa.agEmp()
empresa.mostrarTodo()