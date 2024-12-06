# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(684, 508)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 8, 431, 81))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_expresion = QLineEdit(self.groupBox)
        self.lineEdit_expresion.setObjectName(u"lineEdit_expresion")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_expresion)

        self.pushButton_analizar = QPushButton(self.groupBox)
        self.pushButton_analizar.setObjectName(u"pushButton_analizar")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.pushButton_analizar)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 100, 431, 361))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_representacionIntermedia = QTableWidget(self.groupBox_2)
        if (self.tableWidget_representacionIntermedia.columnCount() < 4):
            self.tableWidget_representacionIntermedia.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_representacionIntermedia.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_representacionIntermedia.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_representacionIntermedia.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_representacionIntermedia.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_representacionIntermedia.setObjectName(u"tableWidget_representacionIntermedia")
        self.tableWidget_representacionIntermedia.horizontalHeader().setVisible(True)
        self.tableWidget_representacionIntermedia.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_representacionIntermedia.horizontalHeader().setHighlightSections(True)
        self.tableWidget_representacionIntermedia.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_representacionIntermedia.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableWidget_representacionIntermedia, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(450, 10, 231, 451))
        self.tableWidget_simbolos = QTableWidget(self.groupBox_3)
        if (self.tableWidget_simbolos.columnCount() < 2):
            self.tableWidget_simbolos.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_simbolos.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_simbolos.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.tableWidget_simbolos.setObjectName(u"tableWidget_simbolos")
        self.tableWidget_simbolos.setGeometry(QRect(10, 21, 211, 421))
        self.tableWidget_simbolos.verticalHeader().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 684, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Analizador Sint\u00e1ctico", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Expresi\u00f3n", None))
        self.pushButton_analizar.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Representaci\u00f3n Intermedia (Arreglo)", None))
        ___qtablewidgetitem = self.tableWidget_representacionIntermedia.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Posici\u00f3n", None));
        ___qtablewidgetitem1 = self.tableWidget_representacionIntermedia.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Etiqueta", None));
        ___qtablewidgetitem2 = self.tableWidget_representacionIntermedia.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Argumento 1", None));
        ___qtablewidgetitem3 = self.tableWidget_representacionIntermedia.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Argumento 2", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Tabla de S\u00edmbolos", None))
        ___qtablewidgetitem4 = self.tableWidget_simbolos.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Posici\u00f3n", None));
        ___qtablewidgetitem5 = self.tableWidget_simbolos.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
    # retranslateUi

