import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PySide6.QtCore import Qt

class ConversorEurosPesetas(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 250, 200, 400)
        self.init_ui()

    def init_ui(self):
        # Configuración de la interfaz
        layout = QVBoxLayout()

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(0)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)

        self.label_euros = QLabel("Euros: 0")
        self.resultado_label = QLabel("Pesetas: 0")

        estilo_label = (
            "font-weight: bold;"
            "font-family: 'Arial';"
            "font-size: 14px;"
        )
        self.label_euros.setStyleSheet(estilo_label)
        self.resultado_label.setStyleSheet(estilo_label)

        self.slider.valueChanged.connect(self.actualizar_resultado)

        layout.addWidget(self.label_euros)
        layout.addWidget(self.slider)
        layout.addWidget(self.resultado_label)

        self.setLayout(layout)

        self.setWindowTitle('Conversor de Euros a Pesetas')
        self.show()

    def actualizar_resultado(self):
        euros = self.slider.value()
        pesetas = euros * 166.386
        resultado_texto = f'Pesetas: {pesetas:.2f}'
        self.resultado_label.setText(resultado_texto)

        euros_texto = f'Euros: {euros}'
        self.label_euros.setText(euros_texto)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    conversor = ConversorEurosPesetas()
    sys.exit(app.exec())
