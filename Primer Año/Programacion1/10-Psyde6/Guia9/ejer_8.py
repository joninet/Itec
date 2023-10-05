#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class VentanaPromedio(QMainWindow):
    def __init__(self,cantidad):
        super().__init__()
        self.cantidad=cantidad
        layout = QVBoxLayout()

        #creamos las etiquetas y botones
        self.texto = QLabel('Ingresar edades')
        self.boton = QPushButton('Enviar')
        centralWidget = QWidget()
        self.cantidadVocales = QLabel('Promedio de edades')
        self.resultado = QLabel('')

        #agregamos etiquetas y botonos al layout
        layout.addWidget(self.texto)
        for _ in range(self.cantidad):
            layout.addWidget(QLineEdit())
            layout.addWidget(QLineEdit())
        self.boton.setDefault(True)
        layout.addWidget(self.boton)
        self.boton.clicked.connect(self.promedioEdades)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        layout.addWidget(self.cantidadVocales)
        layout.addWidget(self.resultado)

    def promedioEdades(self):
        listaNum=[]
        contador=0
        for numE in self.findChildren(QLineEdit):
            numero = int(numE.text())
            listaNum.append(numero)
        for x in listaNum:
            contador+=x
        promedio=contador/len(listaNum)
        self.resultado.setText(f'{promedio}')

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Crear los widgets
        self.texto = QLabel('Ingresar cantidad a cargar')
        self.entrada = QLineEdit()
        self.boton = QPushButton('Enviar')

        # Agregar los widgets al layout
        layout.addWidget(self.texto)
        layout.addWidget(self.entrada)
        layout.addWidget(self.boton)

        # Conectar la señal del botón a la función
        self.boton.clicked.connect(self.ventanaDos)

        # Configurar el widget central de la ventana
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def ventanaDos(self):
        cant = int(self.entrada.text())
        self.ventana2 = VentanaPromedio(cant)
        self.ventana2.show()

if __name__ == '__main__':
    app = QApplication([])
    #css = '*{font-size: 20px; background-color: #ffffff; color: #850a30;}'
    #app.setStyleSheet(css)
    window = VentanaPrincipal()
    window.show()
    app.exec()
