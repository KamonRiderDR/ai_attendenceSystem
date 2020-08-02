# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dateinfo_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")

        '''label to show picture'''
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        pix=QPixmap()
        img=QImage("months_imgs\Apr.PNG")
        self.label.setPixmap(pix.fromImage(img))
        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label.setScaledContents(True)

        '''widget to show date info'''
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ""))


if __name__ == "__main__":
    app = QApplication( sys.argv )
    
    TestUi=QWidget()
    TestUi.setStyleSheet("background-color: white;")
    TestUi.setAttribute(Qt.WA_TranslucentBackground, True)
    TestUi.main_ui=Ui_Form()
    TestUi.main_ui.setupUi(TestUi)
    TestUi.show()

    sys.exit( app.exec_() )