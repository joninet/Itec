def mostrarTodo(self):
    print(f"Empresa: {self.nombre} Rubro: {self.rubro}")
    print("Programadores")
    for programador in self.listaProgramadores:
        print(f"{programador.nombre}. Salario: {programador.sueldo} ")
