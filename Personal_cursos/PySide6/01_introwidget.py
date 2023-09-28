from PySide6.QtWidgets import *# se importan todos los widgets
class myFirstWindow(QMainWindow): #hereda de QMainwidows para que se comporte como una ventana
    def setupUi(self):
        self.setFixedSize (500, 330)#cambia el tamaño de la ventana
        self.setStyleSheet("background: #242526;")

        #contenedor del titulo
        self.frameTitulo = QFrame(self)#se define una caja nueva y el sefl quiere decir que va a estar dentro de Myfirst windows
        self.frameTitulo.setGeometry(10,10,480,100)
        self.frameTitulo.setStyleSheet("background: #0CABAC;")

        #Texto del titulo
        self.titulo=QLabel(self.frameTitulo)#indica donde va a ir el texto
        self.titulo.text="Hola"


        self.frameInputs = QFrame(self)
        self.frameInputs.setGeometry(10,120,480,200)
        self.frameInputs.setStyleSheet("background: #0CABAC;")

#ejecutar aplicacion
import sys
app=QApplication(sys.argv)

#creamos la instancia de la clase para que se ejecute
window=myFirstWindow()
window.setupUi()
window.show() #hace que la ventana se muestre

##para que no se cierre la ventana automaticamente
sys.exit(app.exec_())