from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.texto = QLabel('hola')
        layout.addWidget(self.texto)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('enviar')
        boton.setDefault(True)
        layout.addWidget(boton)
        boton.clicked.connect(self.joni)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def joni(self):
        self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #c6f5c7; color: #850a30;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
