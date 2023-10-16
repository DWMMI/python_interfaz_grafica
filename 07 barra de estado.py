from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel
from PySide6.QtGui import QAction, QKeySequence, QIcon

#ventana principal
class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("barra de estado")
        #barra de estado
        barra_estado=self.statusBar()
        #agregamos un componente permanente
        barra_estado.addPermanentWidget(QLabel("Desarrollo Interfaz"))
        #mostrar un mensaje durante 10 seg.
        barra_estado.showMessage("Listo. Esperando acción...", 10000)

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()