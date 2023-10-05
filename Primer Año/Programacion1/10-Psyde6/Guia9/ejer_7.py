#Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió.
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Configuracion de la ventana
        layout = QVBoxLayout()
        #creamos las etiquetas y botones
        self.listaDias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        self.texto = QLabel('LLUVIA CAIDA EN MM.')

        layout.addWidget(self.texto)
        for dia in self.listaDias:
            etiqueta = QLabel(dia)
            campo = QLineEdit()
            layout.addWidget(etiqueta)
            layout.addWidget(campo)

        self.boton = QPushButton('Enviar')
        centralWidget = QWidget()
        self.resultado = QLabel('')
        self.boton.setDefault(True)
        layout.addWidget(self.boton)
        self.boton.clicked.connect(self.lluviaTotal)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        layout.addWidget(self.resultado)
    
    def lluviaTotal(self):
        listaMm=[]
        contador=0
        diaMayor=""
        mayorLluvia=0
        for numE in self.findChildren(QLineEdit):
            numero = int(numE.text())
            listaMm.append(numero)
            contador+=numero
        for x in range(len(listaMm)):
            num=listaMm[x]
            llu=self.listaDias[x]
            if num > mayorLluvia:
                mayorLluvia=num
                diaMayor=llu

        self.resultado.setText(f'Lluvia total: {contador}mm\nDia que mas llovio: {diaMayor}')

if __name__ == '__main__':
    app = QApplication()
    #css = '*{font-size: 20px; background-color: #ffffff; color: #850a30;}'
    #app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()