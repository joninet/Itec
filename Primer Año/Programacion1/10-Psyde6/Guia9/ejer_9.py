#Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el nombre de cada una.
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class VentanaPromedio(QMainWindow):
    def __init__(self, cantidad):
        super().__init__()
        self.cantidad = cantidad
        layout = QVBoxLayout()

        # Crear etiquetas, botones y listas
        self.texto = QLabel('Ingresar nombres y sexos')
        self.listaSexo = []
        self.listaNombres = []
        for _ in range(self.cantidad):
            self.nombreLabel = QLabel('Nombre')
            self.listaNombres.append(QLineEdit(f"Nombre {_+1}"))
            self.SexoLabel = QLabel(f"Sexo")
            self.listaSexo.append(QLineEdit(f"M/F"))

        self.boton = QPushButton('Enviar')
        self.boton.setDefault(True)
        self.boton.clicked.connect(self.Mujeres)
        self.resultadoA = QLabel('Nombre de las Mujeres:')
        self.resultado = QLabel('')
        self.resultadoB = QLabel('Cantidad')
        self.cantidad = QLabel('')

        # Agregar widgets al layout
        layout.addWidget(self.texto)

        for sexo, nombre in zip(self.listaSexo, self.listaNombres):#es lo mismo que hacer un for para cada lista para recorrerla
            layout.addWidget(nombre)
            layout.addWidget(sexo)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultadoA)
        layout.addWidget(self.resultado)
        layout.addWidget(self.resultadoB)
        layout.addWidget(self.cantidad)

        # Configurar el widget central de la ventana
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def Mujeres(self):
        listaMujeres = []  
        for x in range(len(self.listaSexo)):
            sexo=self.listaSexo[x].text()  
            if sexo == "F":
                mujerNombre=self.listaNombres[x].text()
                listaMujeres.append(mujerNombre)
        resultadoMujeres = ', '.join(listaMujeres)  
        self.resultado.setText(resultadoMujeres)
        cantidadLista=str(len(listaMujeres))
        self.cantidad.setText(cantidadLista)


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