#Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.texto = QLabel('Ingresar Nombre')
        layout.addWidget(self.texto)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('Enviar')
        boton.setDefault(True)
        layout.addWidget(boton)
        boton.clicked.connect(self.nombreInvertido)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        self.nInvertido = QLabel('Nombre Invertido')
        layout.addWidget(self.nInvertido)
        self.resultado = QLabel('')
        layout.addWidget(self.resultado)

    def nombreInvertido(self):
        nombreLista=self.entrada.text().split(" ")
        invertido=f"{nombreLista[1]}, {nombreLista[0]}"
        self.resultado.setText(f'Hola {invertido}')

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #c6f5c7; color: #850a30;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
