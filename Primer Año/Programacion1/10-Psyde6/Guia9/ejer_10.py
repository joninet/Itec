#Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo  y mostrar el nombre de la persona que menos gana.
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class VentanaPromedio(QMainWindow):
    def __init__(self, cantidad):
        super().__init__()
        self.perSalMin = cantidad
        layout = QVBoxLayout()

        # Crear etiquetas, botones y listas
        self.texto = QLabel('Ingresar nombre y salario')
        self.listaSalario = []
        self.listaNombres = []
        for _ in range(self.perSalMin):
            self.nombreLabel = QLabel('Nombre')
            self.listaNombres.append(QLineEdit(f"Nombre {_+1}"))
            self.SexoLabel = QLabel(f"Salario")
            self.listaSalario.append(QLineEdit())

        self.boton = QPushButton('Enviar')
        self.boton.setDefault(True)
        self.boton.clicked.connect(self.Mujeres)
        self.resultadoA = QLabel('Persona de la que menos gana:')
        self.resultado = QLabel('')
        self.resultadoB = QLabel('Salario minimo')
        self.perSalMin = QLabel('')

        # Agregar widgets al layout
        layout.addWidget(self.texto)

        for salario, nombre in zip(self.listaSalario, self.listaNombres):#es lo mismo que hacer un for para cada lista para recorrerla
            layout.addWidget(nombre)
            layout.addWidget(salario)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultadoA)
        layout.addWidget(self.resultado)
        layout.addWidget(self.resultadoB)
        layout.addWidget(self.perSalMin)

        # Configurar el widget central de la ventana
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def Mujeres(self):
        salarioMinimo = 100000000000000000000000000000
        personaNombre=""
        for x in range(len(self.listaSalario)):
            salarioMin=int(self.listaSalario[x].text())
            if salarioMin < salarioMinimo:
                salarioMinimo=salarioMin
                personaNombre=self.listaNombres[x].text()
        self.perSalMin.setText(str(salarioMinimo))
        self.resultado.setText(personaNombre)



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.texto = QLabel('Ingresar cantidad a cargar')
        self.entrada = QLineEdit()
        self.boton = QPushButton('Enviar')
        layout.addWidget(self.texto)
        layout.addWidget(self.entrada)
        layout.addWidget(self.boton)

        self.boton.clicked.connect(self.ventanaDos)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def ventanaDos(self):
        cant = int(self.entrada.text())
        self.ventana2 = VentanaPromedio(cant)
        self.ventana2.show()

if __name__ == '__main__':
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec()