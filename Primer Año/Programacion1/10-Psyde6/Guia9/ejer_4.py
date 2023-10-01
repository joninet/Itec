from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Configuracion de la ventana
        layout = QVBoxLayout()
        #creamos las etiquetas y botones
        self.texto = QLabel('Ingresar Numeros')
        self.entrada = QLineEdit()
        self.boton = QPushButton('Enviar')
        centralWidget = QWidget()
        self.cantidadVocales = QLabel('Cantidad de Numeros mayores a 23')
        self.resultado = QLabel('')

        #agregamos etiquetas y botonos al layout
        layout.addWidget(self.texto)
        for _ in range(10):
            layout.addWidget(QLineEdit())
        self.boton.setDefault(True)
        layout.addWidget(self.boton)
        self.boton.clicked.connect(self.numerosMayores)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        layout.addWidget(self.cantidadVocales)
        layout.addWidget(self.resultado)

        #CSS para editar
        self.entrada.setStyleSheet("QLineEdit {font-family: Arial; color: black; background: transparent; border: none; border-bottom: 1px solid black; font-size: 14px;}")
        self.boton.setStyleSheet(
        """
        QPushButton {font-family: Arial; color: white; background-color: #472B31; border-radius: 15px;}
        QPushButton:hover {border: 2px solid #472B31; background-color: #472B39; color: black;}
        """
)
    
    def numerosMayores(self):
        contador=0
        for numE in self.findChildren(QLineEdit):
            numero = int(numE.text())
            if numero > 23:
                contador += 1
        self.resultado.setText(f'{contador}')
        

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #ffffff; color: #850a30;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()