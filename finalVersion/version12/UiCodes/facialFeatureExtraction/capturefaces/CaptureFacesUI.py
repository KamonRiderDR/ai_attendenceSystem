# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaptureFaces.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_CaptureFaces(object):
    def setupUi(self, CaptureFaces):
        CaptureFaces.setObjectName("CaptureFaces")
        CaptureFaces.resize(958, 520)
        self.layout_main=QGridLayout(CaptureFaces)

        self.lbl_video = QtWidgets.QLabel()
        self.lbl_video.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.lbl_video.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_video.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_video.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_video.setObjectName("lbl_video")

        self.layout_main.addWidget(self.lbl_video)


        self.retranslateUi(CaptureFaces)
        QtCore.QMetaObject.connectSlotsByName(CaptureFaces)



    def retranslateUi(self, CaptureFaces):
        _translate = QtCore.QCoreApplication.translate
        CaptureFaces.setWindowTitle(_translate("CaptureFaces", "人脸图像采集系统"))
        self.lbl_video.setText(_translate("CaptureFaces", "<font size=4><b>视频显示区</b></font>"))