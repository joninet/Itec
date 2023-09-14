class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje):
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje
        self.proyecto = None

    def asignarProyecto(self, proyecto):
        self.proyecto = proyecto

    def obtenerProyectoLenguaje(self):
        return f"Sistema: {self.proyecto}. Lenguaje: {self.lenguaje}"

class Empresa:
    def __init__(self, nombre, rubro):
        self.nombre = nombre
        self.rubro = rubro
        self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores = []

    def agEmp(self, nombreEmp, lenguaje, proyecto):
        if lenguaje in self.listaLenguajes:
            if lenguaje == "Python":
                sueldo=1475000
            else:
                sueldo=615000
            programador = Programador(nombreEmp, sueldo, lenguaje)
            programador.asignarProyecto(proyecto)
            self.listaProgramadores.append(programador)
        else:
            print("No se necesita ese lenguaje. Lista de Lenguajes:")
            for rec in self.listaLenguajes:
                print(rec)

    def mostrarTodo(self):
        print(f"Empresa: {self.nombre}. Rubro: {self.rubro}")
        print("Programadores:")
        for programador in self.listaProgramadores:
            print(f"{programador.nombre}. Salario: {programador.sueldo}. {programador.obtenerProyectoLenguaje()}")

empresa1 = Empresa("Google", "Informática")
empresa1.agEmp("Pedro", "C#", "Sistema Gallina SRL")
empresa1.agEmp("Salvador", "Ruby", "Sistema Gallina SRL")
empresa1.agEmp("Pablo", "Python", "Web Pollitos")
empresa1.agEmp("Ana", "JavaScript", "Web Pollitos")
empresa1.mostrarTodo()

