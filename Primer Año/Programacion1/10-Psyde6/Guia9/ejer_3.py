#Pedir una frase y contar las vocales.
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.texto = QLabel('Ingresar frase')
        layout.addWidget(self.texto)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('Enviar')
        boton.setDefault(True)
        layout.addWidget(boton)
        boton.clicked.connect(self.contarVocales)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        self.cantidadVocales = QLabel('Cantidad de vocales')
        layout.addWidget(self.cantidadVocales)
        self.resultado = QLabel('')
        layout.addWidget(self.resultado)

    def contarVocales(self):
        vocales="aeiou"
        contador=0
        for x in range(len(self.entrada.text())):
            letra=self.entrada.text()[x]
            print(letra)
            if letra in vocales:
                contador+=1
        self.resultado.setText(f'{contador}')

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #c6f5c7; color: #850a30;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
