import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDial
from PySide6.QtCore import Qt

class VentanaSonido(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Configuración de la interfaz
        layout = QVBoxLayout()

        self.etiqueta_valor = QLabel("0 dB", self)
        self.etiqueta_valor.setAlignment(Qt.AlignCenter)

        self.qdial = QDial(self)
        self.qdial.setMinimum(0)
        self.qdial.setMaximum(100)
        self.qdial.setValue(50)
        self.qdial.valueChanged.connect(self.actualizar_valor_etiqueta)

        layout.addWidget(self.etiqueta_valor)
        layout.addWidget(self.qdial)

        self.setLayout(layout)

        self.setWindowTitle('Control de Volumen')
        self.show()

    def actualizar_valor_etiqueta(self, valor):
        texto = f'{valor} dB'
        self.etiqueta_valor.setText(texto)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaSonido()
    sys.exit(app.exec())
