from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton,QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator, QDoubleValidator, QFont
from datetime import datetime
import sqlite3


class InGastos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("EasyPay - GASTOS")
        self.resize(300, 300)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        centralWidget.setLayout(layout)

        
        """def funQlabel(self, nombreVariable,texto,fila,columna):
            self.nombreVariable=QLabel(texto)
            layout.addWidget(self.nombreVariable,fila,columna)

        funQlabel("titulo", "Ingresar Gastos", 0,0)"""

        # TITULO
        self.titulo = QLabel("INGRESAR GASTOS")
        layout.addWidget(self.titulo, 0, 0)

        """def funEspacio(self,fila,columna):
            espacio = QLabel()
            espacio.setFixedSize(10,10)
            layout.addWidget(espacio,fila,columna)

        funEspacio(1,0)"""

        # ESPACIO
        espacio1 = QLabel()
        espacio1.setFixedSize(10, 10)
        layout.addWidget(espacio1, 1, 0)


        # Ingreso de Monto
        self.tituloMonto = QLabel("Monto")
        layout.addWidget(self.tituloMonto, 2, 0)
        self.ingresoMonto = QLineEdit()
        self.ingresoMonto.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ingresoMonto.setFixedSize(200, 30)
        layout.addWidget(self.ingresoMonto, 3, 0)

        # ESPACIO
        espacio2 = QLabel()
        espacio2.setFixedSize(10, 10)
        layout.addWidget(espacio2, 4, 0)

        # Título del Tipo de Pago
        self.tituloD = QLabel("Tipo de Pago")
        layout.addWidget(self.tituloD, 5, 0)

        # Combobox con las opciones
        self.tipoGastoCombo = QComboBox()
        self.tipoGastoCombo.addItems(["Proveedores", "Devolucion", "Descuento", "Promoción"])
        self.tipoGastoCombo.setFixedSize(200, 30)
        layout.addWidget(self.tipoGastoCombo, 6, 0)

        # ESPACIO
        espacio3 = QLabel()
        espacio3.setFixedSize(10, 10)
        layout.addWidget(espacio3, 7, 0)

        # Botón Enviar
        self.botonEnviar = QPushButton("Enviar")
        self.botonEnviar.setDefault(True)
        self.botonEnviar.setFixedSize(200, 30)
        self.botonEnviar.clicked.connect(self.enviar)
        layout.addWidget(self.botonEnviar, 8, 0)

    def enviar(self):
        monto = float(self.ingresoMonto.text())
        fecha = datetime.now()
        PagoGasto = 'Gasto'
        tipo = self.tipoGastoCombo.currentText()
        eliminado = False
        conn = sqlite3.connect("EasyPay.db")
        conn.execute(f"INSERT INTO caja (PagoGasto,tipo,monto,fecha,eliminado) VALUES ('{PagoGasto}','{tipo}','{monto}','{fecha}','{eliminado}');")
        conn.commit()
        print("Records created successfully")
        conn.close()



class EditGastos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("EasyPay - GASTOS")
        self.resize(300, 300)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        centralWidget.setLayout(layout)

        # TITULO EDITAR
        self.titulo = QLabel("EDITAR GASTOS")
        layout.addWidget(self.titulo, 10, 0)

        # ESPACIO
        espacio5 = QLabel()
        espacio5.setFixedSize(10, 10)
        layout.addWidget(espacio5, 11, 0)

        # Ingreso de ID (editar)
        self.tituloEditar = QLabel("ID")
        layout.addWidget(self.tituloEditar, 12, 0)
        self.ingresoIdEditar = QLineEdit()
        self.ingresoIdEditar.setFixedSize(200, 30)
        layout.addWidget(self.ingresoIdEditar, 13, 0)

        # Ingreso de monto (editar)
        self.tituloMontoEditar = QLabel("Monto")
        layout.addWidget(self.tituloMontoEditar, 14, 0)
        self.ingresoMontoEditar = QLineEdit()
        self.ingresoMontoEditar.setFixedSize(200, 30)
        layout.addWidget(self.ingresoMontoEditar, 15, 0)

        # Tipo de Pago (editar)
        self.tituloDeditar = QLabel("Tipo de Pago")
        layout.addWidget(self.tituloDeditar, 16, 0)
        self.tipoGastoEditar = QComboBox()
        self.tipoGastoEditar.addItems(["Efectivo", "Credito", "Debito", "Transferencia", "Cheque"])
        self.tipoGastoEditar.setFixedSize(200, 30)
        layout.addWidget(self.tipoGastoEditar, 17, 0)

        # Botón Enviar (editar)
        self.botonEnviarEditar = QPushButton("Enviar")
        self.botonEnviarEditar.setDefault(True)
        self.botonEnviarEditar.setFixedSize(200, 30)
        self.botonEnviarEditar.clicked.connect(self.enviar)
        layout.addWidget(self.botonEnviarEditar, 18, 0)


        
    def enviar(self):
        idEditar=int(self.ingresoIdEditar.text())
        monto = float(self.ingresoMontoEditar.text())
        tipo = self.tipoGastoCombo.currentText()
        eliminado = False
        conn = sqlite3.connect("EasyPay.db")
        conn.execute(f"INSERT INTO caja (PagoGasto,tipo,monto,fecha,eliminado) VALUES ('{PagoGasto}','{tipo}','{monto}','{fecha}','{eliminado}');")
        conn.commit()
        print("Records created successfully")
        conn.close()