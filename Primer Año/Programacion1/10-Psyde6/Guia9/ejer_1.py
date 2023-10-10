#Pedir dos números enteros, sumarlos y mostrar el resultado
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.primerNumero = QLabel('Ingresar primer Numero')
        layout.addWidget(self.primerNumero)
        self.inputPrimer = QLineEdit()
        layout.addWidget(self.inputPrimer)
        self.segundoNumero = QLabel('Ingresar segundo Numero')
        layout.addWidget(self.segundoNumero)
        self.inputSegundo = QLineEdit()
        layout.addWidget(self.inputSegundo)
        boton = QPushButton('Enviar')
        boton.setDefault(True)
        layout.addWidget(boton)
        boton.clicked.connect(self.sumar)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        self.printResultado = QLabel("Resultado de la suma")
        layout.addWidget(self.printResultado)
        self.resultado = QLabel("")
        layout.addWidget(self.resultado)

    def sumar(self):
        numero1=int(self.inputPrimer.text())
        numero2=int(self.inputSegundo.text())
        self.suma=numero1+numero2
        self.resultado.setText(f"{self.suma}")
        #self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #c6f5c7; color: #850a30;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
