# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui',
# licensing of 'design.ui' applies.
#
# Created: Sat Oct  5 22:20:43 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.select_files_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_files_button.setObjectName("select_files_button")
        self.verticalLayout.addWidget(self.select_files_button)
        self.check_updates_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_updates_button.setObjectName("check_updates_button")
        self.verticalLayout.addWidget(self.check_updates_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.select_files_button.setText(QtWidgets.QApplication.translate("MainWindow", "Select files", None, -1))
        self.check_updates_button.setText(QtWidgets.QApplication.translate("MainWindow", "Check updates", None, -1))

