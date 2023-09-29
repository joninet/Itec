from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        for _ in range(3):
            #self.entrada = QLineEdit()
            #layout.addWidget(self.entrada)
            layout.addWidget(QLineEdit())

        boton = QPushButton('Recolectar')
        boton.setDefault(True)
        layout.addWidget(boton)

        self.salida = QLabel()
        layout.addWidget(self.salida)

        boton.clicked.connect(self.reco)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def reco(self):
        s = ''
        for cajaTexto in self.findChildren(QLineEdit):
            s += cajaTexto.text()
        self.salida.setText(s)

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 50px; background-color: #c6f5c7; color: #850a30;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()