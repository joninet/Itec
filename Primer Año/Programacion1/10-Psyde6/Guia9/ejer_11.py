from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

def crear_y_agregar_widget(layout, widget, texto):
    new_widget = widget(texto)  
    layout.addWidget(new_widget) 

# Ejemplo de uso
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_widget = QWidget()
    main_layout = QVBoxLayout(main_widget)

    # Crear y agregar un widget
    crear_y_agregar_widget(main_layout, QLabel, "Hola mundo")

    main_widget.show()
    sys.exit(app.exec_())
