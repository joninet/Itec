from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QMessageBox, QStatusBar
from PySide6.QtCore import Qt  
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
import sys

class ventanaPrueba(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EFI - Programacion1")
        self.resize(700, 400)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Boton Caja
        layout = QGridLayout()
        self.caja = QPushButton('Caja')
        self.caja.setDefault(True)
        self.caja.setMinimumSize(300, 30)
        self.caja.clicked.connect(self.mostrarVentanaPrueba)
        layout.addWidget(self.caja, 0, 0)  

        # Boton Pagos
        self.pagos = QPushButton('Pagos')
        self.pagos.setDefault(True)
        self.pagos.setMinimumSize(300, 30)
        self.pagos.clicked.connect(self.mostrarVentanaPrueba)
        layout.addWidget(self.pagos, 1, 0)  

        # Boton Gastos
        self.gastos = QPushButton('Gastos')
        self.gastos.setDefault(True)
        self.gastos.setMinimumSize(300, 30)
        self.gastos.clicked.connect(self.mostrarVentanaPrueba)
        layout.addWidget(self.gastos, 2, 0)  

        # Boton Gastos
        self.informes = QPushButton('Informes')
        self.informes.setDefault(True)
        self.informes.setMinimumSize(300, 30)
        self.informes.clicked.connect(self.mostrarVentanaPrueba)
        layout.addWidget(self.informes, 3, 0) 

        layout.setAlignment(Qt.AlignCenter) 
        centralWidget.setLayout(layout)

    def mostrarVentanaPrueba(self):
        self.ventana2 = ventanaPrueba()
        self.ventana2.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

