import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QLineEdit, QComboBox

#Ejercicio 4: La universidad desea una aplicación que le calcule el porcentaje
# de niños y niñas que hay matriculados en una jornada para futuros estudiantes.

class Ejercicio4 (QMainWindow):
    def __int__(self):
        super().__int__()
        #Características
        self.setWindowTitle("Porcentajes")
        #Crear widget central con layout vertical
        central_widget = QWidget()
        layout = QVBoxLayout()
        #QComboBox
        self.combo_ninos = QComboBox()
        lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.combo_ninos.addItems(lista)
        layout.addWidget(QLabel("Numero de niños"))
        layout.addWidget(self.combo_ninos)
        self.combo_ninas.addItems(lista)
        layout.addWidget(QLabel("Numero de niñas"))
        layout.addWidget(self.combo_ninas)
        #Boton
        self.calcular_boton = QPushButton("Calcular")
        layout.addWidget(self.calcular_boton)
        self.calcular_boton.clicked.connect(self.calcular_porcentaje)
    def calcular_porcentaje(self):
        ninos = int(self.combo_ninos.currentText())
        ninas = int(self.combo_ninos.currentText())
        porc_ninos = ninos / (ninos+ninas) * 100
        porc_ninas = ninas / (ninos+ninas) * 100
        self.resultado_label.setText(f"Porcentaje niños{porc_ninos:.2f}% \n Porcentaje niñas{porc_ninas:.2f}% ")

#mostrar resultados
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ejercicio4()
    window.show()
    sys.exit(app.exec())