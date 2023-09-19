from dataclasses import dataclass
@dataclass
class Deportista:
    nombre: str
    altura: float
    peso: float
    
    def __str__(self):
        return f'{self.nombre}: {self.altura}, {self.peso}'

deportista1 = Deportista('Elena', 1.81, 64)
print(deportista1)  # Elena: 1.81, 64