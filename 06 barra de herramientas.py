import os
from PySide6.QtGui import QAction, QKeySequence, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar


class VP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra de herramientas")
        ruta_icono = os.path.join(os.path.dirname(__file__),
        "corazon.png")
        # Añadimos a la acción, un icono
        accion = QAction(QIcon(ruta_icono), "&Imprimir", self)
        accion.setShortcut(QKeySequence("ctrl+p"))
        accion.triggered.connect(self.imprimir_consola)
        #creamos la barra herramientas
        barra_herramientas = QToolBar("Barra herramientas")
        #añadimos el QAction a la barra herramientas
        barra_herramientas.addAction(accion)
        #añadimos la barra de herramientas a la aplicación
        self.addToolBar(barra_herramientas)

    def imprimir_consola(self):
        print("Love Renate"
              "")

if __name__ == "__main__":

    app = QApplication([])
    ventana1 = VP()
    ventana1.show()
    app.exec()