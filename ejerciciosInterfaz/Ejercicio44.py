import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QPushButton

class CalculadoraPorcentaje(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora de Porcentaje')
        self.setGeometry(1000, 250, 400, 200)
        self.init_ui()

    def init_ui(self):
        # Configuración de la interfaz
        layout = QVBoxLayout()

        self.comboBox_ninos = QComboBox(self)
        self.comboBox_ninas = QComboBox(self)

        for i in range(11):
            self.comboBox_ninos.addItem(str(i))
            self.comboBox_ninas.addItem(str(i))

        self.resultado_label = QLabel("")
        resultado_estilo = (
            "background-color: red;"
            "color: white;"
            "font-weight: bold;"
            "font-family: 'Arial';"
            "font-size: 14px;"
        )
        self.resultado_label.setStyleSheet(resultado_estilo)

        calcular_button = QPushButton("Calcular", self)
        calcular_button.clicked.connect(self.actualizar_resultado)

        layout.addWidget(self.comboBox_ninos)
        layout.addWidget(self.comboBox_ninas)
        layout.addWidget(calcular_button)
        layout.addWidget(self.resultado_label)
        self.setLayout(layout)



        self.show()

    def actualizar_resultado(self):
        ninos_seleccionados = int(self.comboBox_ninos.currentText())
        ninas_seleccionadas = int(self.comboBox_ninas.currentText())
        total_estudiantes = ninos_seleccionados + ninas_seleccionadas

        if total_estudiantes > 0:
            porcentaje_ninos = (ninos_seleccionados / total_estudiantes) * 100
            porcentaje_ninas = (ninas_seleccionadas / total_estudiantes) * 100

            resultado_texto = f"Niños: {porcentaje_ninos:.2f}% - Niñas: {porcentaje_ninas:.2f}%"
            self.resultado_label.setText(resultado_texto)
        else:
            self.resultado_label.setText("Selecciona al menos un estudiante.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculadoraPorcentaje()
    sys.exit(app.exec_())
