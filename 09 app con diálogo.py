from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QMainWindow


class VP (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App con diálogos")
        boton=QPushButton("Haz click para que aparezca el diálogo")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)
    # Creamos un objeto de la clase diálogo
    def mostrar_dialogo(self):
        ventana_dialogo=QDialog(self)
        ventana_dialogo.setWindowTitle("Ventana Diálogo")
        # Lanzamos su bucle de eventos
        ventana_dialogo.exec()

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VP()
    ventana1.show()
    app.exec()