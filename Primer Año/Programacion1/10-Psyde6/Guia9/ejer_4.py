#https://es.stackoverflow.com/questions/409293/por-que-cambia-el-estilo-del-boton
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Configuracion de la ventana
        layout = QVBoxLayout()
        #creamos las etiquetas y botones
        self.texto = QLabel('Ingresar frase')
        self.entrada = QLineEdit()
        boton = QPushButton('Enviar')
        centralWidget = QWidget()
        self.cantidadVocales = QLabel('Cantidad de vocales')
        self.resultado = QLabel('')

        #agregamos etiquetas y botonos al layout
        layout.addWidget(self.texto)
        layout.addWidget(self.entrada)
        boton.setDefault(True)
        layout.addWidget(boton)
        boton.clicked.connect(self.contarVocales)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        layout.addWidget(self.cantidadVocales)
        layout.addWidget(self.resultado)

        #CSS para editar
        self.entrada.setStyleSheet("QLineEdit {font-family: Arial; color: black; background: transparent; border: none; border-bottom: 1px solid black; font-size: 14px;}")
        self.boton.setStyleSheet("QPushButton {font-family: Arial; color: white; background-color: black; border-radius: 15px;}")
        self.boton.setStyleSheet("QPushButton:hover {border: 2px solid red; background-color: white; color: black;}")
    
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