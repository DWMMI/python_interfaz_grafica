from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QAction, QKeySequence


# ventana principal
class VentanaPrincipal(QMainWindow):
    """
    Ventana principal de la aplicación.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")

        # barra de menú
        barra_menu = self.menuBar()
        # añadirla la menú principal
        menu = barra_menu.addMenu("&Menu")
        # crear acción
        accion = QAction("Imprimir por consola", self)
        # Atajo de teclado
        accion.setShortcut(QKeySequence("ctrl+i"))
        # descripción
        accion.setToolTip("Imprime un mensaje en la consola")
        # conectar acción con ranura
        accion.triggered.connect(self.imprimir_consola)
        # añadir acción al menú
        menu.addAction(accion)


    def imprimir_consola(self):
        print("Acción lanzada a traves del menu")


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()

