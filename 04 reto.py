from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meses del año")
        self.setGeometry(300, 300, 250, 200)

        # Creamos una etiqueta
        self.etiqueta1 = QLabel("Pulsa un botón de meses", self)

        # Creamos una lista para almacenar los nombres de los meses
        self.meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

        # Creamos un layout vertical
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.etiqueta1)

        # Creamos botones para cada mes y los conectamos a la función boton_pulsado
        for mes in self.meses:
            boton = QPushButton(mes, self)
            boton.clicked.connect(self.boton_pulsado)
            layout_vertical.addWidget(boton)

        # Establecemos el layout como el layout principal de la ventana
        self.setLayout(layout_vertical)

    def boton_pulsado(self):
        # Obtenemos el botón que ha sido pulsado usando la función sender
        boton = self.sender()

        # Obtenemos el texto del botón
        texto_boton = boton.text()

        # Actualizamos el texto de la etiqueta con el mes seleccionado
        self.etiqueta1.setText(f"Has pulsado en {texto_boton}")

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
