'''
importamos las clases QAplication... del paquete PySide6
'''
from PySide6.QtWidgets import QApplication,QLabel,QWidget
class Ventana(QWidget):
    '''Clase Ventana, hereda de Qwidget, componente base.'''
    #constructor de la clase Window
    def __int__(self):
        #llamada al constructor de la superclase
        super().__init__()
        #Asignamos el título de la ventana
        self.setWindowTitle("Ventana")
        #creamos una etiqueta con la ventana como elemento principal.
        self.etiqueta1 = QLabel("Hola mundo",self)
if __name__=="__main__":
    #Cada aplicación será una sola instancia de QApplication.
    app = QApplication([])
    #Creamos un objeto ventana.
    ventana1 = Ventana()
    #Mostramos la ventana, por defecto los componentes estám ocultos.
    ventana1.show()
    #Iniciamos el bucle de eventos.
    app.exec()