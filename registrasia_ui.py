# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrasia_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registrasia_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(451, 392)
        Form.setStyleSheet("background-color: rgb(231, 255, 212);\n"
"")
        self.label_registr = QtWidgets.QLabel(Form)
        self.label_registr.setGeometry(QtCore.QRect(100, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_registr.setFont(font)
        self.label_registr.setStyleSheet("")
        self.label_registr.setObjectName("label_registr")
        self.pushButton_zaregestr = QtWidgets.QPushButton(Form)
        self.pushButton_zaregestr.setGeometry(QtCore.QRect(90, 320, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_zaregestr.setFont(font)
        self.pushButton_zaregestr.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_zaregestr.setObjectName("pushButton_zaregestr")
        self.lineEdit_login = QtWidgets.QLineEdit(Form)
        self.lineEdit_login.setGeometry(QtCore.QRect(230, 140, 181, 34))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_parol = QtWidgets.QLineEdit(Form)
        self.lineEdit_parol.setGeometry(QtCore.QRect(230, 200, 181, 34))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.lineEdit_parol.setFont(font)
        self.lineEdit_parol.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lineEdit_parol.setObjectName("lineEdit_parol")
        self.label_Login = QtWidgets.QLabel(Form)
        self.label_Login.setGeometry(QtCore.QRect(10, 130, 171, 34))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.label_Login.setFont(font)
        self.label_Login.setObjectName("label_Login")
        self.label_Parol = QtWidgets.QLabel(Form)
        self.label_Parol.setGeometry(QtCore.QRect(10, 200, 181, 34))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.label_Parol.setFont(font)
        self.label_Parol.setObjectName("label_Parol")
        self.pushButton_voiti = QtWidgets.QPushButton(Form)
        self.pushButton_voiti.setGeometry(QtCore.QRect(90, 260, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.pushButton_voiti.setFont(font)
        self.pushButton_voiti.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_voiti.setObjectName("pushButton_voiti")
        self.label_pustoi = QtWidgets.QLabel(Form)
        self.label_pustoi.setGeometry(QtCore.QRect(10, 90, 421, 34))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(16)
        self.label_pustoi.setFont(font)
        self.label_pustoi.setText("")
        self.label_pustoi.setObjectName("label_pustoi")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "registrasia"))
        self.label_registr.setText(_translate("Form", "Регистрация"))
        self.pushButton_zaregestr.setText(_translate("Form", "Зарегестрироваться"))
        self.label_Login.setText(_translate("Form", "Введите email:"))
        self.label_Parol.setText(_translate("Form", "Введите пароль:"))
        self.pushButton_voiti.setText(_translate("Form", "Войти"))
