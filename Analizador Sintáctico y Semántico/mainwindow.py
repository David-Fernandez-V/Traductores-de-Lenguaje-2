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
        MainWindow.resize(381, 201)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 311, 69))
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
        self.groupBox_2.setGeometry(QRect(29, 100, 311, 53))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_notacionPostfija = QLineEdit(self.groupBox_2)
        self.lineEdit_notacionPostfija.setObjectName(u"lineEdit_notacionPostfija")
        self.lineEdit_notacionPostfija.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_notacionPostfija, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 381, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Analizador Sint\u00e1ctico", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingresa expresi\u00f3n", None))
        self.pushButton_analizar.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
        self.groupBox_2.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Notaci\u00f3n Postfija", None))
    # retranslateUi

