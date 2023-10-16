import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QLineEdit

#Ejercicio 2: Dado dos variables numéricas a y b, que el usuario debe introducir por consola, se pide realizar un algoritmo
# que intercambie los valores de ambas variables y muestre por pantalla cuanto valen al final las dos variables
#Por comando:
'''
a = int(input("Dame A:"))
b = int(input("Dame B:"))
print("A: ", a); print("B: ", b)

aux = a
a = b
b = aux

print("El valor intercambiado de A es: ", a)
print("El valor intercambiado de B es: " , b)
'''

#Por interfaz gráfica
class Ejercicio2 (QMainWindow):
    def __init__(self):
        super().__init__()
        #Propiedades vantana
        self.setWindowTitle("Intercambio de números")
        self.setGeometry(1000, 250, 400, 200)
        #Layout vertical
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        #Campos de entrada para A y B
        self.input_a = QLineEdit()
        self.input_b = QLineEdit()
        self.input_a.setPlaceholderText('Introduzca el número A')
        self.input_b.setPlaceholderText('Introduzca el número B')
        layout.addWidget(QLabel("Variable A"))
        layout.addWidget(self.input_a)
        layout.addWidget(QLabel("Variable B"))
        layout.addWidget(self.input_b)
        #Boton de intercambio
        self.intercambio_Boton = QPushButton("Hacer la magia")
        layout.addWidget(self.intercambio_Boton)
        self.intercambio_Boton.clicked.connect(self.intercambio_variables)
        #Etiqueta resultado
        self.resultado = QLabel("")
        layout.addWidget(self.resultado)
        central_widget.setLayout(layout)
    #función intercambio_variables
    def intercambio_variables(self):
        #leer QLineEdit
        valor_a = self.input_a.text()
        valor_b = self.input_b.text()
        aux = valor_a
        valor_a = valor_b
        valor_b = aux
        self.resultado.setText(f"Valor \n A: {valor_a} \n B: {valor_b}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ejercicio2()
    window.show()
    sys.exit(app.exec())





