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
        self.texto = QLabel('Ingresar 10 numeros')
        for x in range(10):
            self.num = QLineEdit()
        
        boton = QPushButton('Enviar')
        centralWidget = QWidget()
        self.cantidadVocales = QLabel('Cantidad de vocales')
        self.resultado = QLabel('')

        #agregamos etiquetas y botonos al layout
        layout.addWidget(self.texto)
        layout.addWidget(self.num)
        boton.setDefault(True)
        layout.addWidget(boton)
        boton.clicked.connect(self.mayoresVeintitres)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        layout.addWidget(self.mayoresVeintitres)
        layout.addWidget(self.resultado)

        #CSS para editar
        self.num.setStyleSheet("QLineEdit {font-family: Arial; color: black; background: transparent; border: none; border-bottom: 1px solid black; font-size: 14px;}")
        self.boton.setStyleSheet(
        """
        QPushButton {font-family: Arial; color: white; background-color: black; border-radius: 15px;}
        QPushButton:hover {border: 2px solid red; background-color: white; color: black;}
        """
)
    def mayoresVeintitres(self):
        numeros=self.findChildren(QLineEdit)
        numerosLista=[]
        for x in numeros:
            if x < 23:
                numerosLista.append(x)
        return self.resultado.setText(f'{str(numerosLista)}')


if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #c6f5c7; color: #850a30;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()