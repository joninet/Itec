from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar
from PySide6.QtGui import QAction, QIcon, QPainter, QPixmap
from pathlib import Path
from Pagos import InPagos , EditPagos
from Gastos import InGastos , EditGastos
from Informe import InInforme
from Cierre_caja import CierreCaja
import sys

class ventanaPrueba(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasyPay - PRINCIPAL")
        self.resize(700, 400)
        self.menuCompleto()
        self.setStyleSheet("background-image: url(imagenes/easypay.png);")

    def menuCompleto(self):
        menu = self.menuBar()
        
        # Menú Caja
        menuCaja = menu.addMenu("Caja")
        self.crearSubmenu("menuCaja","cierreCaja","Cierre de Caja","CierreCaja()")

        # Menú Pagos
        menuPagos = menu.addMenu("Pago")
        self.crearSubmenu("menuPagos","ingresarPagos","Ingresar","InPagos()")
        self.crearSubmenu("menuPagos","editarPagos","Editar","EditPagos()")

        # Menú Gastos
        menuGastos = menu.addMenu("Gasto")
        self.crearSubmenu("menuGastos","ingresarGastos","Ingresar","InGastos()")
        self.crearSubmenu("menuGastos","editarGastos","Editar","EditGastos()")

        # Menú Informes
        menuInformes = menu.addMenu("Informes")
        self.crearSubmenu("menuInformes","informesAction","Ver Informes","EditGastos()")
        
        self.setStatusBar(QStatusBar(self))

    def crearSubmenu(self,nombreMenu,nombreVariable,texto,conexion):
        nombreVariable = QAction(texto, self)
        nombreVariable.triggered.connect(self.mostrarVentana(conexion))
        nombreMenu.addAction(nombreVariable)

    def mostrarVentana(self,nombreImport):
        self.ventana2 = nombreImport
        self.ventana2.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())