# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1030)
        MainWindow.setStyleSheet("background-color: rgb(5, 0, 5)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 40, 1371, 951))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 471, 201))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(29, 29, 29);\n"
"color: yellow")
        self.pushButton.setObjectName("pushButton")
        self.RLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.RLabel_2.setGeometry(QtCore.QRect(40, 40, 175, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.RLabel_2.setFont(font)
        self.RLabel_2.setStyleSheet("color: yellow")
        self.RLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.RLabel_2.setObjectName("RLabel_2")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(230, 40, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time.setFont(font)
        self.time.setStyleSheet("color:  rgb(218, 98, 0)")
        self.time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time.setObjectName("time")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.RLabel_2.setText(_translate("MainWindow", "Current angle"))
        self.time.setText(_translate("MainWindow", "0"))