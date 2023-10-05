#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class VentanaPromedio(QMainWindow):
    def __init__(self, cantidad):
        super().__init__()
        self.cantidad = cantidad
        layout = QVBoxLayout()

        # Crear etiquetas, botones y listas
        self.texto = QLabel('Ingresar edades y nombres')
        self.lista_edades = []
        self.lista_nombres = []
        for _ in range(self.cantidad):
            self.lista_edades.append(QLineEdit())
            self.lista_nombres.append(QLineEdit())

        self.boton = QPushButton('Enviar')
        self.boton.setDefault(True)
        self.boton.clicked.connect(self.promedioEdades)

        self.resultado = QLabel('')

        # Agregar widgets al layout
        layout.addWidget(self.texto)
        for edad, nombre in zip(self.lista_edades, self.lista_nombres):
            layout.addWidget(edad)
            layout.addWidget(nombre)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        # Configurar el widget central de la ventana
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def promedioEdades(self):
        lista_edades = []
        lista_nombres = []
        contador = 0

        for edad, nombre in zip(self.lista_edades, self.lista_nombres):
            edad_valor = int(edad.text())
            lista_edades.append(edad_valor)
            lista_nombres.append(nombre.text())

        for x in lista_edades:
            contador += x

        promedio = contador / len(lista_edades)
        nombres_completos = ', '.join(lista_nombres)
        resultado_texto = f'Promedio de edades: {promedio}\nNombres ingresados: {nombres_completos}'
        self.resultado.setText(resultado_texto)

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
