# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 355)
        Form.setStyleSheet("background-color: rgb(231, 255, 212);\n"
"")
        self.label_avtorizazia = QtWidgets.QLabel(Form)
        self.label_avtorizazia.setGeometry(QtCore.QRect(180, 20, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_avtorizazia.setFont(font)
        self.label_avtorizazia.setStyleSheet("")
        self.label_avtorizazia.setObjectName("label_avtorizazia")
        self.pushButton_clienti = QtWidgets.QPushButton(Form)
        self.pushButton_clienti.setGeometry(QtCore.QRect(40, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_clienti.setFont(font)
        self.pushButton_clienti.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_clienti.setObjectName("pushButton_clienti")
        self.pushButton_tariffPlan = QtWidgets.QPushButton(Form)
        self.pushButton_tariffPlan.setGeometry(QtCore.QRect(270, 140, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_tariffPlan.setFont(font)
        self.pushButton_tariffPlan.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_tariffPlan.setObjectName("pushButton_tariffPlan")
        self.pushButton_sotrudniki = QtWidgets.QPushButton(Form)
        self.pushButton_sotrudniki.setGeometry(QtCore.QRect(40, 230, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_sotrudniki.setFont(font)
        self.pushButton_sotrudniki.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_sotrudniki.setObjectName("pushButton_sotrudniki")
        self.pushButton_uslugi = QtWidgets.QPushButton(Form)
        self.pushButton_uslugi.setGeometry(QtCore.QRect(270, 230, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_uslugi.setFont(font)
        self.pushButton_uslugi.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_uslugi.setObjectName("pushButton_uslugi")
        self.pushButton_vihod = QtWidgets.QPushButton(Form)
        self.pushButton_vihod.setGeometry(QtCore.QRect(450, 230, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_vihod.setFont(font)
        self.pushButton_vihod.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_vihod.setObjectName("pushButton_vihod")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "menu"))
        self.label_avtorizazia.setText(_translate("Form", "Главное меню"))
        self.pushButton_clienti.setText(_translate("Form", "Абоненты"))
        self.pushButton_tariffPlan.setText(_translate("Form", "Тарифный план"))
        self.pushButton_sotrudniki.setText(_translate("Form", "Сотрудники"))
        self.pushButton_uslugi.setText(_translate("Form", "Услуги"))
        self.pushButton_vihod.setText(_translate("Form", "Выход"))

