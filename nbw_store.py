# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\nb_store.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QIcon
import requests
import pyrebase
import time

config = {
    "apiKey": "AIzaSyBPkPU-l4BXDXDZs-ZwuWzSckqaGeYG5Ag",
    "authDomain": "nbwallet-nb.firebaseapp.com",
    "databaseURL": "https://nbwallet-nb.firebaseio.com",
    "projectId": "nbwallet-nb",
    "storageBucket": "nbwallet-nb.appspot.com",
    "messagingSenderId": "16565581725"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

db = firebase.database()

class Ui_LOGIN(QtWidgets.QMainWindow):
    def __init__(self, parent, main):
        self.main = main
        super(Ui_LOGIN, self).__init__(parent)
        self.setObjectName("LOGIN")
        self.resize(437, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
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
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, LOGIN):
        _translate = QtCore.QCoreApplication.translate
        LOGIN.setWindowTitle(_translate("LOGIN", "LOGIN"))
        self.label.setText(_translate("LOGIN", "Username"))
        self.label_2.setText(_translate("LOGIN", "Password"))
        self.pushButton.setText(_translate("LOGIN", "LOGIN"))
        self.pushButton.clicked.connect(self.auth)

    def auth(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            if user:
                print(user)
                self.main.user = user['localId']
                self.main.statusbar.showMessage("ID: {}".format(self.main.user))
                self.close()
        except:
            e = sys.exc_info()[0]
            e2 = sys.exc_info()[1]
            print(e, e2)
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("AUTH ERROR")
            msg.setText("LOGIN FAILED")
            # msg.setInformativeText("This is additional information")
            # msg.setDetailedText("The details are as follows:")
            retval = msg.exec_()





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 640)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 811, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(300, 420, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 12, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 651, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 150, 511, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 771, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Type','Amount', 'Time', 'From'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 480, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionView_Transaction = QtWidgets.QAction(MainWindow)
        self.actionView_Transaction.setObjectName("actionView_Transaction")
        self.actionCheck_Balance = QtWidgets.QAction(MainWindow)
        self.actionCheck_Balance.setObjectName("actionCheck_Balance")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.menuMenu.addAction(self.actionCheck_Balance)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionLogin)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.user = ''


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NBWALLET-STORE"))
        MainWindow.setWindowIcon(QtGui.QIcon('nblogo.png'))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label_2.setText(_translate("MainWindow", "AMOUNT"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Purchase"))
        self.pushButton_2.setText(_translate("MainWindow", "UPDATE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View Transaction"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionView_Transaction.setText(_translate("MainWindow", "View Transaction"))
        self.actionCheck_Balance.setText(_translate("MainWindow", "Check Balance.."))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.pushButton.clicked.connect(self.ok_clicked)
        self.pushButton_2.clicked.connect(self.update_clicked)
        self.actionLogin.triggered.connect(self.auth)
        self.actionCheck_Balance.triggered.connect(self.check_clicked)
        # self.setWindowIcon(QtWidgets.QIcon('icon.png'))

    def auth(self):
        # self.loginui = QtWidgets.QMainWindow()
        # MainWindow = QtWidgets.QMainWindow()
        try:
            self.login_ui = Ui_LOGIN(self.tab, self)
            # self.login_ui.setupUi(self.loginui)
            self.login_ui.show()
        except:
            e = sys.exc_info()[0]
            e2 = sys.exc_info()[1]
            print(e, e2)

    def ok_clicked(self):
        if self.user == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Auth Error")
            msg.setText("Please Login")
            # msg.setInformativeText("This is additional information")
            # msg.setDetailedText("The details are as follows:")
            retval = msg.exec_()
        else:
            self.do_purchase()

    def check_clicked(self):
        if self.user == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Auth Error")
            msg.setText("Please Login")
            # msg.setInformativeText("This is additional information")
            # msg.setDetailedText("The details are as follows:")
            retval = msg.exec_()
        else:
            self.check_balance()

    def check_balance(self):
        req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/checkBalance?id={id}&type=store"
                                   .format(id=self.user))
        print(req)
        try:
            req_json = req.json()
            if req_json['Status'] == 'SUCCESS':
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Check Balance")
                msg.setText("Your Balance: {}".format(req_json['Balance']))
                # msg.setInformativeText("This is additional information")
                # msg.setDetailedText("The details are as follows:")
                retval = msg.exec_()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("ERROR")
            msg.setText("FAILED")
            # msg.setInformativeText("This is additional information")
            # msg.setDetailedText("The details are as follows:")
            retval = msg.exec_()

    def timestampsimp(self, times):
        print(times)
        stt = str(times)
        unix_timestamp  = int(stt[:-3])
        utc_time = time.gmtime(unix_timestamp)
        local_time = time.localtime(unix_timestamp)
        print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))

        return time.strftime("%Y-%m-%d %H:%M:%S", local_time)

    def update_clicked(self):
        if self.user == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Auth Error")
            msg.setText("Please Login")
            # msg.setInformativeText("This is additional information")
            # msg.setDetailedText("The details are as follows:")
            retval = msg.exec_()
        else:
            self.update()

    def update(self):
        print("TABLE")
        try:
            # id = self.lineEdit_.text()
            req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/checkTx?id={id}&type=store"
                               .format(id=self.user))
            print(req)
            try:
                req_json = req.json()
                req_len = len(req_json)
                self.tableWidget.setRowCount(req_len)
                # self.tableWidget.setColumnCount(5)
                for row, item in enumerate(req_json):
                    print(item)
                    # for row in range(req_len):
                        # for column in range(4):
                    print("ROW: ",row)
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(req_json[item]["name"]))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(req_json[item]["type"]))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(req_json[item]["amount"]))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(self.timestampsimp(req_json[item]["time"])))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(req_json[item]["from"]))

            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("ERROR")
                msg.setText("FAILED")
                retval = msg.exec_()

        except:
            e = sys.exc_info()[0]
            e2 = sys.exc_info()[1]
            print(e, e2)
        print("Updated")

    def do_purchase(self):
        id = self.lineEdit.text()
        amount = self.lineEdit_2.text()
        # print("https://us-central1-nbwallet-nb.cloudfunctions.net/doPurchase?from={}&userId={}&money={}".format(self.user['localId'], id, amount))
        try:
            reply = QtWidgets.QMessageBox.question(self.tab, 'Message',"Are you sure to Purchase {amount} Baht to {id}?"
                                                   .format(amount=amount, id=id)
                                                   , (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No))
            if reply == QtWidgets.QMessageBox.Yes:
                a = requests.get(
                    "https://us-central1-nbwallet-nb.cloudfunctions.net/doPurchase?from={}&userId={}&money={}".format(self.user, id, amount))
                try:
                    aj = a.json()
                    if aj['Status'] == 'SUCCESS':
                        print(aj)
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        msg.setWindowTitle("SUCCESS")
                        msg.setText("Purchase Complete: {} Baht".format(amount))
                        # msg.setInformativeText("This is additional information")
                        # msg.setDetailedText("The details are as follows:")
                        retval = msg.exec_()
                        # QtWidgets.QMessageBox.about(self, "SUCCESS", "New Balance: {}".format(req_json['Balance']))
                        # print("Add Balance Complete")
                        self.lineEdit.setText('')
                        self.lineEdit_2.setText('')
                    else:
                        pass
                except:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("ERROR")
                    msg.setText("FAILED")
                    # msg.setInformativeText("This is additional information")
                    # msg.setDetailedText("The details are as follows:")
                    retval = msg.exec_()
            else:
                pass
        except:
            e = sys.exc_info()[0]
            e2 = sys.exc_info()[1]
            print(e, e2)

if __name__ == "__main__":
    import sys
    import locale
    app = QtWidgets.QApplication(sys.argv)
    # locale.setlocale(locale.LC_ALL, 'en US')
    # print(QtCore.QLocale())

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.set
    MainWindow.show()
    sys.exit(app.exec_())

