# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lineChart.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView, QLineSeries, QChart
from PyQt5.QtGui import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chartView = QChartView(Form)
        self.chartView.setObjectName("chartView")
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.verticalLayout.addWidget(self.chartView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
