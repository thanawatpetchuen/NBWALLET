# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LOGIN(object):
    def setupUi(self, LOGIN):
        LOGIN.setObjectName("LOGIN")
        LOGIN.resize(437, 294)
        self.centralwidget = QtWidgets.QWidget(LOGIN)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 70, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        LOGIN.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LOGIN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 21))
        self.menubar.setObjectName("menubar")
        LOGIN.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LOGIN)
        self.statusbar.setObjectName("statusbar")
        LOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(LOGIN)
        QtCore.QMetaObject.connectSlotsByName(LOGIN)

    def retranslateUi(self, LOGIN):
        _translate = QtCore.QCoreApplication.translate
        LOGIN.setWindowTitle(_translate("LOGIN", "LOGIN"))
        self.label.setText(_translate("LOGIN", "Username"))
        self.label_2.setText(_translate("LOGIN", "Password"))
        self.pushButton.setText(_translate("LOGIN", "LOGIN"))

