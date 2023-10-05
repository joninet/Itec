#Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad.

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class VentanaPromedio(QMainWindow):
    def __init__(self, cantidad):
        super().__init__()
        self.cantidad = cantidad
        layout = QVBoxLayout()

        # Crear etiquetas, botones y listas
        self.texto = QLabel('Ingresar edades y nombres')
        self.lista_Fecha = []
        self.lista_nombres = []
        for _ in range(self.cantidad):
            self.lista_nombres.append(QLineEdit("Nombre"))
            self.lista_Fecha.append(QLineEdit("xx/xx/xxxx"))

        self.boton = QPushButton('Enviar')
        self.boton.setDefault(True)
        self.boton.clicked.connect(self.Fechas)

        self.resultado = QLabel('')

        # Agregar widgets al layout
        layout.addWidget(self.texto)
        for fecha, nombre in zip(self.lista_Fecha, self.lista_nombres):
            layout.addWidget(nombre)
            layout.addWidget(fecha)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        # Configurar el widget central de la ventana
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def Fechas(self):
        listaMayor = []  # Lista para almacenar los nombres de personas mayores de 18 años
        aH = 2023
        mH = 6
        dH = 3

        for rec in range(len(self.lista_Fecha)):
            reco = self.lista_Fecha[rec].text()  # Obtener el texto del campo de fecha
            aD, aM, aA = reco.split("/")
            edad = aH - int(aA)
            if int(aM) > mH or int(aM) == mH and int(aD) > dH:
                edad -= 1
            if edad >= 18:
                listaMayor.append(nombres[rec])  # Agregar el nombre a la lista de personas mayores

        resultado_texto = ', '.join(listaMayor)  # Unir los nombres en una cadena
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
