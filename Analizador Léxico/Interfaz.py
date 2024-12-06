from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QTableWidgetItem
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

    def limpiar_tablas(self):
        for row in range(self.ui.tableWidget_representacionIntermedia.rowCount()):
            for col in range(self.ui.tableWidget_representacionIntermedia.columnCount()):
                item = QTableWidgetItem("")
                self.ui.tableWidget_representacionIntermedia.setItem(row, col, item)
        
        for row in range(self.ui.tableWidget_simbolos.rowCount()):
            for col in range(self.ui.tableWidget_simbolos.columnCount()):
                item = QTableWidgetItem("")
                self.ui.tableWidget_simbolos.setItem(row, col, item)

    def actualizar_tablas(self):
        self.limpiar_tablas()
        self.ui.tableWidget_representacionIntermedia.setRowCount(self.analizador_sintactico.gda.obtener_longitud())
        self.ui.tableWidget_simbolos.setRowCount(self.analizador_sintactico.tabla_simbolos.obtener_longitud())

        for row, nodo in enumerate (self.analizador_sintactico.gda.nodos):
            posicion_item = QTableWidgetItem(str(row+1))
            etiqueta_item = QTableWidgetItem(str(nodo[0]))

            if isinstance(nodo[1], str):
                argumento1 = QTableWidgetItem(str(nodo[1]))
            else:
                argumento1 = QTableWidgetItem(str(nodo[1]+1))

            if isinstance(nodo[2], str):
                argumento2 = QTableWidgetItem(str(nodo[2]))
            else:
                argumento2 = QTableWidgetItem(str(nodo[2]+1))

            self.ui.tableWidget_representacionIntermedia.setItem(row, 0, posicion_item)
            self.ui.tableWidget_representacionIntermedia.setItem(row, 1, etiqueta_item)
            self.ui.tableWidget_representacionIntermedia.setItem(row, 2, argumento1)
            self.ui.tableWidget_representacionIntermedia.setItem(row, 3, argumento2)

        for row, simbolo in enumerate (self.analizador_sintactico.tabla_simbolos.simbolos):
            posicion_item = QTableWidgetItem(str(row+1))
            identificador_item = QTableWidgetItem(str(simbolo))

            self.ui.tableWidget_simbolos.setItem(row, 0, posicion_item)
            self.ui.tableWidget_simbolos.setItem(row, 1, identificador_item) 

    @Slot()
    def analizar(self):
        self.analizador_sintactico.set_expresion(self.ui.lineEdit_expresion.text())
        self.analizador_sintactico.iniciar_analisis()
        if self.analizador_sintactico.es_expresion_valida:
            self.actualizar_tablas()
            QMessageBox.information(self, "Análisis Terminado", "La expresión es válida.")
        else:
            self.limpiar_tablas()
            QMessageBox.information(self, "Análisis Terminado", "La expresión NO es válida.")

        self.analizador_sintactico.reiniciar_analizador()
