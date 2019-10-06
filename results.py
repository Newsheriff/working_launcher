# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui',
# licensing of 'results.ui' applies.
#
# Created: Sat Oct  5 22:22:17 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(419, 365)
        self.verticalLayout = QtWidgets.QVBoxLayout(Results)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.results_label = QtWidgets.QLabel(Results)
        self.results_label.setAlignment(QtCore.Qt.AlignCenter)
        self.results_label.setObjectName("results_label")
        self.horizontalLayout.addWidget(self.results_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.confirmation_button = QtWidgets.QPushButton(Results)
        self.confirmation_button.setObjectName("confirmation_button")
        self.horizontalLayout_2.addWidget(self.confirmation_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        Results.setWindowTitle(QtWidgets.QApplication.translate("Results", "Form", None, -1))
        self.results_label.setText(QtWidgets.QApplication.translate("Results", "TextLabel", None, -1))
        self.confirmation_button.setText(QtWidgets.QApplication.translate("Results", "OK", None, -1))

