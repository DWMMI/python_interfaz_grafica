import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QDockWidget, QTextEdit


class vp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ventana flotante")
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        ruta = os.path.join(os.path.dirname(__file__), "images/consola.png")
        accion = QAction(QIcon(ruta), "Imprimir...", self)
        accion.setShortcut(QKeySequence("ctrl+p"))
        accion.triggered.connect(self.imprimir_consola)
        menu.addAction(accion)

        barra_herramientas = QToolBar("Barra herramientas")
        barra_herramientas.addAction(accion)
        self.addToolBar(barra_herramientas)

        barra_estado = self.statusBar()
        barra_estado.addPermanentWidget(QLabel("Desarrolla de interfaces"))
        barra_estado.showMessage("Listo...", 5000)

        # Creación de un componente flotante
        dock1 = QDockWidget()
        # Agregamos título al componente
        dock1.setWindowTitle("Componente base 1")
        # Asignaremos el componente que contendrá
        dock1.setWidget(QTextEdit(""))
        # Le asignamos anchura mínima
        dock1.setMinimumWidth(50)
        # Le posicionamos a la derecha
        self.addDockWidget(Qt.RightDockWidgetArea, dock1)
        self.setCentralWidget(QLabel("Componente principal"))

    def imprimir_consola(self):
        print("Impreso...")

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = vp()
    ventana1.show()
    app.exec()
