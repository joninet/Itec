from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Ventana1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana 1')
        button = QPushButton('Botón en Ventana 1', self)
        button.move(50, 50)

class Ventana2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana 2')
        button = QPushButton('Botón en Ventana 2', self)
        button.move(50, 50)

if __name__ == '__main__':
    app = QApplication([])
    
    ventana1 = Ventana1()
    ventana1.show()

    ventana2 = Ventana2()
    ventana2.show()
    
    app.exec()
