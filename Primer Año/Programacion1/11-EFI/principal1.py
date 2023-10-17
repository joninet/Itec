from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar
from PySide6.QtGui import QAction, QIcon, QPainter, QPixmap
from pathlib import Path
from Pagos import InPagos, EditPagos
from Gastos import InGastos, EditGastos
from Informe import InInforme
from Cierre_caja import CierreCaja
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasyPay - PRINCIPAL")
        self.resize(700, 400)
        self.setStyleSheet("background-image: url(imagenes/easypay.png);")

        self.menuCompleto()

    def menuCompleto(self):
        menu = self.menuBar()

        # Menú Caja
        menuCaja = menu.addMenu("Caja")
        cierreCaja = QAction("Cierre de Caja", self)
        cierreCaja.triggered.connect(self.mostrarVentana("InGastos()"))
        menuCaja.addAction(cierreCaja)

        # Menú Pagos
        menuPagos = menu.addMenu("Pago")
        ingresarPagos = QAction("Ingresar", self)
        ingresarPagos.triggered.connect(self.mostrarVentana("InPagos()"))
        menuPagos.addAction(ingresarPagos)

        editarPagos = QAction("Editar", self)
        editarPagos.triggered.connect(self.mostrarVentana("EditPagos()"))
        menuPagos.addAction(editarPagos)

        # Menú Gastos
        menuGastos = menu.addMenu("Gasto")
        ingresarGastos = QAction("Ingresar", self)
        ingresarGastos.triggered.connect(self.mostrarVentana("InGastos()"))
        menuGastos.addAction(ingresarGastos)

        editarGastos = QAction("Editar", self)
        editarGastos.triggered.connect(self.mostrarVentana("EditGastos()"))
        menuGastos.addAction(editarGastos)

        # Menú Informes
        menuInformes = menu.addMenu("Informes")
        informesAction = QAction("Ver Informes", self)
        informesAction.triggered.connect(self.mostrarVentana("CierreCaja()"))
        menuInformes.addAction(informesAction)

        self.setStatusBar(QStatusBar(self))

    def mostrarVentana(self,nombreImport):
        self.ventana2 = nombreImport
        self.ventana2.show()

    def mostrarVentanaInPagos(self):
        self.ventana2 = InPagos()
        self.ventana2.show()

    def mostrarVentanaEditPagos(self):
        self.ventana2 = EditPagos()
        self.ventana2.show()

    def mostrarVentanaInGastos(self):
        self.ventana2 = InGastos()
        self.ventana2.show()

    def mostrarVentanaEditGastos(self):
        self.ventana2 = EditGastos()
        self.ventana2.show()

    def mostrarVentanaInInformes(self):
        self.ventana2 = InInforme()
        self.ventana2.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())