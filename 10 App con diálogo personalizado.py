from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtWidgets import QApplication, QDialog, QPushButton, QMainWindow, QDialogButtonBox, QVBoxLayout, QLabel


class DialogoPersonalizado(QDialog):
    def __init__(self):
        super().__init__()
        # Definimos los botones OK y Cancelar en nuestra variable
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        # Pasamos la variable de botones al constructor de QDialogButtonBox
        self.caja_botones = QDialogButtonBox(botones)
        # Conectamos las señales de los botones con las ranuras QDialog
        self.caja_botones.accepted.connect(self.accepted)
        (self.caja_botones.rejected.connect(self.rejected))
        # Añadimos un QLabel y el QDialogButtonBox en el layout vertical
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("¿Estás seguro?"))
        self.layout.addWidget(self.caja_botones)
        self.setLayout(self.layout)


class VP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App con diálogos personalizado")
        boton = QPushButton("Haz click para que aparezca el diálogo")
        boton.clicked.connect(self.mostrar_dialogo)
        self.setCentralWidget(boton)

    def mostrar_dialogo(self):
        ventana_dialogo = DialogoPersonalizado()
        ventana_dialogo.setWindowTitle("Ventana de diálogo Personalizada")

        resultado = ventana_dialogo.exec()

        if resultado:
            print("Aceptado")
        else:
            print("Cancelado")


def cargar_traductor(app):
    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator.load("qt_es", translations)
    app.installTranslator(translator)


if __name__ == "__main__":
    app = QApplication([])
    cargar_traductor(app)
    ventana1 = VP()
    ventana1.show()
    app.exec()
