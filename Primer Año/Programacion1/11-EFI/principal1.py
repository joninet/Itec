from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar)
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)
class ventanaPrueba(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EFI - Programacion1")
        self.resize(700, 400)
        self.menuCompleto()

    def menuCompleto(self):
        menu = self.menuBar()
        #menu caja
        menuCaja = menu.addMenu("Caja")
        arqueoCaja = QAction("Arqueo caja", self)
        arqueoCaja.triggered.connect(self.mostrarVentanaPrueba)
        menuCaja.addAction(arqueoCaja)
        cierreCaja = QAction("Cierre de Caja", self)
        cierreCaja.triggered.connect(self.mostrarVentanaPrueba)
        menuCaja.addAction(cierreCaja)

        #menu pagos
        menuPagos = menu.addMenu("Pagos")
        ingresarPagos = QAction("Ingresar", self)
        ingresarPagos.triggered.connect(self.mostrarVentanaPrueba)
        menuPagos.addAction(ingresarPagos)

        editarPagos = QAction("Editar", self)
        editarPagos.triggered.connect(self.mostrarVentanaPrueba)
        menuPagos.addAction(editarPagos)

        #menu gastos
        menuGastos = menu.addMenu("Pagos")
        ingresarGastos = QAction("Ingresar", self)
        ingresarGastos.triggered.connect(self.mostrarVentanaPrueba)
        menuGastos.addAction(ingresarGastos)

        editarGastos = QAction("Ingresar", self)
        editarGastos.triggered.connect(self.mostrarVentanaPrueba)
        menuGastos.addAction(editarGastos)

        #menu informes
        menuInformes = menu.addMenu("Informes")
        informesAction = QAction("Ver Informes", self)
        informesAction.triggered.connect(self.mostrarVentanaPrueba)
        menuInformes.addAction(informesAction)


        self.setStatusBar(QStatusBar(self))

    def mostrarVentanaPrueba(self):
        self.ventana2 = ventanaPrueba()
        self.ventana2.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())