# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\nb.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWinExtras
import requests
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 151, 591))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 100, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 140, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 180, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(170, 0, 651, 591))
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(220, 110, 81, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 131, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_Add = QtWidgets.QPushButton(self.tab)
        self.pushButton_Add.setGeometry(QtCore.QRect(500, 510, 131, 41))
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(380, 40, 91, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(220, 110, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 40, 351, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 131, 21))
        self.label_7.setObjectName("label_7")
        self.pushButton_Sub = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Sub.setGeometry(QtCore.QRect(500, 510, 131, 41))
        self.pushButton_Sub.setObjectName("pushButton_Sub")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 110, 191, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 40, 91, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_view = QtWidgets.QLabel(self.tab_3)
        self.label_view.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label_view.setObjectName("label_view")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 40, 351, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_view = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_view.setGeometry(QtCore.QRect(500, 510, 131, 41))
        self.pushButton_view.setObjectName("pushButton_view")
        self.label_balance = QtWidgets.QLabel(self.tab_3)
        self.label_balance.setGeometry(QtCore.QRect(10, 80, 601, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_balance.setFont(font)
        self.label_balance.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_balance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_balance.setObjectName("label_balance")
        self.label_baht = QtWidgets.QLabel(self.tab_3)
        self.label_baht.setGeometry(QtCore.QRect(480, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_baht.setFont(font)
        self.label_baht.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_baht.setObjectName("label_baht")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(390, 41, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Student")
        self.comboBox.addItem("Store")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 621, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Type','Amount', 'Time', 'To'])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 40, 351, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label_19.setObjectName("label_19")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_14.setGeometry(QtCore.QRect(500, 510, 131, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 41, 101, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Student")
        self.comboBox_2.addItem("Store")
        self.tabWidget.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_20 = QtWidgets.QLabel(self.tab_5)
        self.label_20.setGeometry(QtCore.QRect(10, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_12.setGeometry(QtCore.QRect(10, 110, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_21 = QtWidgets.QLabel(self.tab_5)
        self.label_21.setGeometry(QtCore.QRect(10, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_13.setGeometry(QtCore.QRect(10, 200, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        self.label_22.setGeometry(QtCore.QRect(10, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_14.setGeometry(QtCore.QRect(10, 300, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_23 = QtWidgets.QLabel(self.tab_5)
        self.label_23.setGeometry(QtCore.QRect(10, 360, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(10, 400, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_15.setGeometry(QtCore.QRect(500, 510, 131, 41))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_24 = QtWidgets.QLabel(self.tab_5)
        self.label_24.setGeometry(QtCore.QRect(30, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(90, 20, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_25 = QtWidgets.QLabel(self.tab_5)
        self.label_25.setGeometry(QtCore.QRect(10, 460, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(10, 510, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        app.setWindowIcon(QtGui.QIcon('nblogo.png'))
        MainWindow.setStatusBar(self.statusbar)

        # print(self.tbutton.overlayIcon())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NBWALLET-ADMIN"))
        MainWindow.setWindowIcon(QtGui.QIcon("nblogo.png"))
        self.tbutton = QtWinExtras.QWinTaskbarButton(MainWindow)
        self.tbutton.setWindow(MainWindow.windowHandle())
        self.tbutton.setOverlayIcon(QtGui.QIcon('nblogo.png'))
        self.groupBox.setTitle(_translate("MainWindow", "Mode"))
        self.pushButton.setText(_translate("MainWindow", "Add Balance"))
        self.pushButton_2.setText(_translate("MainWindow", "Sub Balance"))
        self.pushButton_3.setText(_translate("MainWindow", "View Balance"))
        self.pushButton_4.setText(_translate("MainWindow", "View Transaction"))
        self.pushButton_5.setText(_translate("MainWindow", "New User"))
        self.label_2.setText(_translate("MainWindow", "USER ID :"))
        self.label_4.setText(_translate("MainWindow", "Baht"))
        self.label_3.setText(_translate("MainWindow", "Amount : "))
        self.pushButton_Add.setText(_translate("MainWindow", "OK"))
        self.pushButton_9.setText(_translate("MainWindow", "Check"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add Balance"))
        self.label_5.setText(_translate("MainWindow", "Baht"))
        self.label_6.setText(_translate("MainWindow", "USER ID :"))
        self.label_7.setText(_translate("MainWindow", "Amount : "))
        self.label_19.setText(_translate("MainWindow", "USER ID :"))
        self.label_view.setText(_translate("MainWindow", "USER ID :"))
        self.pushButton_14.setText(_translate("MainWindow", "OK"))
        self.pushButton_Sub.setText(_translate("MainWindow", "OK"))
        self.pushButton_view.setText(_translate("MainWindow", "OK"))
        self.pushButton_8.setText(_translate("MainWindow", "Check"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Sub Balance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "View Balance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "View Tx"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "New User"))
        self.label_20.setText(_translate("MainWindow", "Name"))
        self.label_21.setText(_translate("MainWindow", "Department"))
        self.label_22.setText(_translate("MainWindow", "Faculty"))
        self.label_23.setText(_translate("MainWindow", "Balance"))
        self.pushButton_15.setText(_translate("MainWindow", "OK"))
        self.label_24.setText(_translate("MainWindow", "ID"))
        self.label_25.setText(_translate("MainWindow", "TEL."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "New User"))
        # Tab Setting
        self.pushButton.clicked.connect(lambda checked: self.change_tab(0))
        self.pushButton_2.clicked.connect(lambda checked: self.change_tab(1))
        self.pushButton_3.clicked.connect(lambda checked: self.change_tab(2))
        self.pushButton_4.clicked.connect(lambda checked: self.change_tab(3))
        self.pushButton_5.clicked.connect(lambda checked: self.change_tab(4))
        self.pushButton_9.clicked.connect(lambda checked: self.show_balance(from_add=True))
        self.pushButton_Add.clicked.connect(self.add_balance)
        self.pushButton_Sub.clicked.connect(self.sub_balance)
        self.pushButton_view.clicked.connect(self.show_balance)
        self.pushButton_14.clicked.connect(self.table_update)
        self.pushButton_15.clicked.connect(self.add_user)
        self.label_baht.setText(_translate("MainWindow", "Baht"))

    def change_tab(self, i):
        self.tabWidget.setCurrentIndex(i)

    def add_user(self):
        id = self.lineEdit_16.text()
        name = self.lineEdit_12.text()
        department = self.lineEdit_13.text()
        faculty = self.lineEdit_14.text()
        balance = self.lineEdit_15.text()
        tel = self.lineEdit_17.text()

        try:
            if id == None or name == None or department == None or faculty == None or balance == None:
                pass
            else:
                print("Add user!", id, name, balance)
                try:
                    a = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/addUser?userId={}&balance={}&department={}&faculty={}&name={}&tel={}".format(
                        id, balance, department, faculty, name, tel))
                    aj = a.json()
                    if aj['Status'] == 'SUCCESS':
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        msg.setWindowTitle("SUCCESS")
                        msg.setText(aj['Info'])
                        retval = msg.exec_()
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

    def timestampsimp(self, times):
        print(times)
        stt = str(times)
        unix_timestamp  = int(stt[:-3])
        utc_time = time.gmtime(unix_timestamp)
        local_time = time.localtime(unix_timestamp)
        print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))

        return time.strftime("%Y-%m-%d %H:%M:%S", local_time)

    def table_update(self):
        print("TABLE")
        try:
            id = self.lineEdit_11.text()
            type = self.comboBox_2.currentText()
            if type == 'Student':
                req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/checkTx?id={id}&type=users"
                                   .format(id=id))
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
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(req_json[item]["Name"]))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(req_json[item]["type"]))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(req_json[item]["amount"]))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(self.timestampsimp(req_json[item]["time"])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(req_json[item]["to"]))

                except:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("ERROR")
                    msg.setText("FAILED")
                    retval = msg.exec_()
            else:
                req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/checkTx?id={id}&type=store"
                                   .format(id=id))
                print(req)
                try:
                    req_json = req.json()
                    req_len = len(req_json)
                    self.tableWidget.setRowCount(req_len)
                    # self.tableWidget.setColumnCount(5)
                    self.tableWidget.setHorizontalHeaderLabels(['Name', 'Type', 'Amount', 'Time', 'From'])
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
                    e = sys.exc_info()[0]
                    e2 = sys.exc_info()[1]
                    # print(e, e2)
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("ERROR")
                    msg.setText("{} {}".format(e, e2))

                    retval = msg.exec_()

        except:
            e = sys.exc_info()[0]
            e2 = sys.exc_info()[1]
            print(e, e2)

    def show_balance(self, from_add=False):
        try:
            if from_add:
                id = self.lineEdit.text()
                req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/checkBalance?id={id}&type=users"
                                   .format(id=id))
                print(req)
                try:
                    req_json = req.json()
                    if req_json['Status'] == 'SUCCESS':
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        msg.setWindowTitle("SUCCESS")
                        msg.setText("Balance: {}".format(req_json['Balance']))
                    # msg.setInformativeText("This is additional information")
                    # msg.setDetailedText("The details are as follows:")
                        retval = msg.exec_()
                except:
                     msg = QtWidgets.QMessageBox()
                     msg.setIcon(QtWidgets.QMessageBox.Warning)
                     msg.setWindowTitle("ERROR")
                     msg.setText("FAILED")
                     retval = msg.exec_()
            else:
                id = self.lineEdit_5.text()
                type = self.comboBox.currentText()
                if type == "Student":
                    req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/checkBalance?id={id}&type=users"
                                   .format(id=id))
                    print(req)
                    try:

                        req_json = req.json()
                        if req_json['Status'] == 'SUCCESS':
                            self.label_balance.setText(str(req_json['Balance']))
                    except:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setWindowTitle("ERROR")
                        msg.setText("FAILED")
                        # msg.setInformativeText("This is additional information")
                        # msg.setDetailedText("The details are as follows:")
                        retval = msg.exec_()
                else:
                    req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/checkBalance?id={id}&type=store"
                                   .format(id=id))
                    print(req)
                    try:
                        req_json = req.json()
                        if req_json['Status'] == 'SUCCESS':
                            self.label_balance.setText(str(req_json['Balance']))
                    except:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setWindowTitle("ERROR")
                        msg.setText("FAILED")
                        # msg.setInformativeText("This is additional information")
                        # msg.setDetailedText("The details are as follows:")
                        retval = msg.exec_()
        except:
            e = sys.exc_info()[0]
            e2 = sys.exc_info()[1]
            print(e, e2)


    def add_balance(self):

        try:
            id = self.lineEdit.text()
            amount = self.lineEdit_2.text()
            print(id)
            print(amount)
            reply = QtWidgets.QMessageBox.question(self.tab, 'Message',"Are you sure to Add {amount} Baht to {id}?"
                                                   .format(amount=amount, id=id)
                                                   , (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No))
            if reply == QtWidgets.QMessageBox.Yes:
                print("YEs")
                req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/addBalance?id={id}&amount={amount}"
                               .format(id=id, amount=amount))
                print(req)
                req_json = req.json()
                print(req_json)
                if req_json['Status'] == 'SUCCESS':
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setWindowTitle("SUCCESS")
                    msg.setText("New Balance: {}".format(req_json['Balance']))
                    # msg.setInformativeText("This is additional information")
                    # msg.setDetailedText("The details are as follows:")
                    retval = msg.exec_()
                    # QtWidgets.QMessageBox.about(self, "SUCCESS", "New Balance: {}".format(req_json['Balance']))
                    print("Add Balance Complete")
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("ERROR")
                    msg.setText("FAILED")
                    # msg.setInformativeText("This is additional information")
                    # msg.setDetailedText("The details are as follows:")
                    retval = msg.exec_()
            else:
                print("NO")
                pass
        except:
            e = sys.exc_info()[0]
            e2 = sys.exc_info()[1]
            print(e, e2)

    def sub_balance(self):
        try:
            id = self.lineEdit.text()
            amount = self.lineEdit_2.text()
            print(id)
            print(amount)
            reply = QtWidgets.QMessageBox.question(self.tab, 'Message',"Are you sure to SUB {amount} Baht to {id}?"
                                                   .format(amount=amount, id=id)
                                                   , (QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No))
            if reply == QtWidgets.QMessageBox.Yes:
                print("YEs")
                req = requests.get("https://us-central1-nbwallet-nb.cloudfunctions.net/subBalance?id={id}&amount={amount}"
                               .format(id=id, amount=amount))
                print(req)
                req_json = req.json()
                if req_json['Status'] == 'SUCCESS':
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setWindowTitle("SUCCESS")
                    msg.setText("New Balance: {}".format(req_json['Balance']))
                    # msg.setInformativeText("This is additional information")
                    # msg.setDetailedText("The details are as follows:")
                    retval = msg.exec_()
                    # QtWidgets.QMessageBox.about(self, "SUCCESS", "New Balance: {}".format(req_json['Balance']))
                    print("Add Balance Complete")
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setWindowTitle("ERROR")
                    msg.setText("FAILED")
                    # msg.setInformativeText("This is additional information")
                    # msg.setDetailedText("The details are as follows:")
                    retval = msg.exec_()
            else:
                print("NO")
                pass
        except:
            e = sys.exc_info()[0]
            e2 = sys.exc_info()[1]
            print(e, e2)




if __name__ == "__main__":
    import sys
    import locale
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('nblogo.png'))
    # locale.setlocale(locale.LC_ALL, 'en US')
    # print(QtCore.QLocale())

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


