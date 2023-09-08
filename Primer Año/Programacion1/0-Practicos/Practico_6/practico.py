class Animal:
    def __init__(self,identificador,peso) -> None:
        self.identificador=identificador
        self.peso=peso

class Puma(Animal):
    def __init__(self,identificador,peso,edad) -> None:
        super().__init__(identificador,peso)
        self.edad=edad
    def estadoSalud(self):
        if self.peso >= 200:
            return f"Sano"
        else:
            return f"enfermo"
    def esAdulto(self):
        if self.edad > 5:
            return f"Adulto"
        else:
            return f"Joven"

class Venado(Animal):
    def __init__(self,identificador,peso) -> None:
        super().__init__(identificador,peso)
    def estadoSalud(self):
        if self.peso >= 200:
            return f"Sano"
        else:
            return f"enfermo"

class Jaula:
    