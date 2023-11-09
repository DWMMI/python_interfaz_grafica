
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Ejercicio11(QMainWindow):
    def __init__(self):
        super().__init__()
        # Propiedades vantana
        self.setWindowTitle("Hola Mundo")
        self.setGeometry(1000, 250, 400, 200)

        QLabel("Hola mundo!", self)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ejercicio11()
    ventana.show()
    app.exec()
