from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Slot
from mainwindow import Ui_MainWindow

from Analizador_Sintactico import AnalizadorSintactico

class Interfaz(QMainWindow):
    def __init__(self):
        super(Interfaz, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.analizador_sintactico = AnalizadorSintactico()

        self.ui.pushButton_analizar.clicked.connect(self.analizar)

    @Slot()
    def analizar(self):
        self.analizador_sintactico.set_expresion(self.ui.lineEdit_expresion.text())
        self.analizador_sintactico.iniciar_analisis()
        if self.analizador_sintactico.es_expresion_valida:
            QMessageBox.information(self, "Análisis Terminado", "La expresión es válida.")
        else:
            QMessageBox.information(self, "Análisis Terminado", "La expresión NO es válida.")

        self.analizador_sintactico.reiniciar_posicion()
        self.analizador_sintactico.validar_expresion()
