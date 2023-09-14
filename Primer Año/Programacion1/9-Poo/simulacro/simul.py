class Empleado:
    def __init__(self,nombre,sueldo) -> None:
        self.nombre=nombre
        self.sueldo=sueldo
class Programador(Empleado):
    def __init__(self, nombre, sueldo,lenguaje) -> None:
        super().__init__(nombre, sueldo,)
        self.lenguaje=lenguaje
    def asignarProyecto(self,proyecto):
        self.proyecto=proyecto
    def obtenerProyectoLenguaje(self):
        return f"{self.proyecto} {self.lenguaje}"

    
class Empresa:
    def __init__(self,nombre,rubro) -> None:
        self.nombre=nombre
        self.rubro=rubro
        self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores = []
    def agEmp(self,nombreEmp,agregoLenguaje,agregoProyecto):
        self.agregoLenguaje=agregoLenguaje
        self.agregoProyecto=agregoProyecto
        self.nombreEmp=nombreEmp
        self.sueldo=None

        if self.agregoLenguaje in self.listaLenguajes:
            if agregoLenguaje == "Python":
                self.sueldo=1475000
            else:
                self.sueldo=615000
            agregoProgramador=Programador(self.nombreEmp,self.sueldo,self.agregoLenguaje)
            self.listaProgramadores.append(agregoProgramador)
        else:
            print("no se necesita ")
            print("Lista de Lenguajes:")
            for rec in self.listaLenguajes:
                print(rec)
    def mostrarTodo(self):
        print(f"Empresa: {self.nombre} Rubro: {self.rubro}")
        print("Programadores")
        for programador in self.listaProgramadores:
            print(f"{programador.nombre}. Salario: {programador.sueldo} sistema: {self.agregoProyecto} lenguaje: {programador.lenguaje}")

    def imprNombre(self):
        return self.nombre
    def imprRubro(self):
        return self.rubro
empresa1=Empresa("Google","Informatica")
empresa1.agEmp("Pedro","C#","Sistema: Gallina SRL.")
empresa1.agEmp("Salvador","Ruby","Sistema: Gallina SRL.")
empresa1.agEmp("Pablo","Python","Web Pollitos.")
empresa1.agEmp("Ana","JavaScript","Web Pollitos.")
empresa1.mostrarTodo()
