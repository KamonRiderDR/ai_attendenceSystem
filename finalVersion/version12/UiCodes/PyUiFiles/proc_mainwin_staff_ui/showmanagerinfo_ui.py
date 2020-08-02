# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowManagerInfo_ui.ui'
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

class Ui_ShowManagerInfo(object):
    def setupUi(self, ShowManagerInfo):
        ShowManagerInfo.setObjectName("ShowManagerInfo")
        ShowManagerInfo.resize(544, 315)
        self.gridLayout = QtWidgets.QGridLayout(ShowManagerInfo)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_showManagerInfo_container = QtWidgets.QWidget(ShowManagerInfo)
        self.widget_showManagerInfo_container.setObjectName("widget_showManagerInfo_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_showManagerInfo_container)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_showNamagerInfo = QtWidgets.QGridLayout()
        self.layout_showNamagerInfo.setObjectName("layout_showNamagerInfo")
        self.label_showManagerName = QtWidgets.QLabel(self.widget_showManagerInfo_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_showManagerName.setFont(font)
        self.label_showManagerName.setObjectName("label_showManagerName")
        self.layout_showNamagerInfo.addWidget(self.label_showManagerName, 0, 0, 1, 1)
        self.label_showManagerId = QtWidgets.QLabel(self.widget_showManagerInfo_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_showManagerId.setFont(font)
        self.label_showManagerId.setObjectName("label_showManagerId")
        self.layout_showNamagerInfo.addWidget(self.label_showManagerId, 1, 0, 1, 1)
        self.lineEdit_showManagerName = QtWidgets.QLineEdit(self.widget_showManagerInfo_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_showManagerName.setFont(font)
        self.lineEdit_showManagerName.setObjectName("lineEdit_showManagerName")
        self.layout_showNamagerInfo.addWidget(self.lineEdit_showManagerName, 0, 1, 1, 1)
        self.lineEdit_showManagerId = QtWidgets.QLineEdit(self.widget_showManagerInfo_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_showManagerId.setFont(font)
        self.lineEdit_showManagerId.setObjectName("lineEdit_showManagerId")
        self.layout_showNamagerInfo.addWidget(self.lineEdit_showManagerId, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.layout_showNamagerInfo)
        self.layout_showManagerBtn = QtWidgets.QHBoxLayout()
        self.layout_showManagerBtn.setObjectName("layout_showManagerBtn")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_showManagerBtn.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget_showManagerInfo_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.layout_showManagerBtn.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.layout_showManagerBtn)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addWidget(self.widget_showManagerInfo_container, 0, 0, 1, 1)
        self.layout_showStaffDataSerach = QtWidgets.QHBoxLayout()
        self.layout_showStaffDataSerach.setObjectName("layout_showStaffDataSerach")
        self.lineEdit_getStaffId = QtWidgets.QLineEdit(ShowManagerInfo)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getStaffId.setFont(font)
        self.lineEdit_getStaffId.setObjectName("lineEdit_getStaffId")
        self.layout_showStaffDataSerach.addWidget(self.lineEdit_getStaffId)
        self.btn_searchStaffData = QtWidgets.QPushButton(ShowManagerInfo)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_searchStaffData.setFont(font)
        self.btn_searchStaffData.setObjectName("btn_searchStaffData")
        self.layout_showStaffDataSerach.addWidget(self.btn_searchStaffData)
        self.layout_showStaffDataSerach.setSpacing(10)
        self.gridLayout.addLayout(self.layout_showStaffDataSerach, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setContentsMargins(3,3,3,3)

        '''set lineedit style'''
        with open("Qss/line_edit_style.qss") as LEditStyle:
            self.lineEdit_getStaffId.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_showManagerId.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_showManagerName.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)

        self.lineEdit_showManagerId.setReadOnly(True)
        self.lineEdit_showManagerName.setReadOnly(True)
        regx=QtCore.QRegExp("[0-9]+$")
        validator=QtGui.QRegExpValidator(regx, self.lineEdit_getStaffId)
        self.lineEdit_getStaffId.setValidator(validator)
        self.lineEdit_getStaffId.setPlaceholderText("请输入您的员工ID以搜索")


        '''set btn style'''
        with open("Qss/push_button_style.qss") as BtnStyle:
            self.btn_searchStaffData.setStyleSheet(BtnStyle.read())
        with open("Qss/push_button_style_lightred.qss") as BtnStyle:
            self.pushButton.setStyleSheet(BtnStyle.read())

        '''enhance shadow effect'''
        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_showManagerInfo_container.setGraphicsEffect(shadow_effect)
        self.widget_showManagerInfo_container.setStyleSheet("""QWidget#widget_showManagerInfo_container{
                                                    background-color: rgba(255,255,255,90);
                                                    border-radius: 8px}""")

        '''init connection'''
        self.btn_searchStaffData.clicked.connect(ShowManagerInfo.slot_showSearchedStaffData)

        self.retranslateUi(ShowManagerInfo)
        QtCore.QMetaObject.connectSlotsByName(ShowManagerInfo)

    def retranslateUi(self, ShowManagerInfo):
        _translate = QtCore.QCoreApplication.translate
        ShowManagerInfo.setWindowTitle(_translate("ShowManagerInfo", "Form"))
        self.label_showManagerName.setText(_translate("ShowManagerInfo", "管理员姓名:"))
        self.label_showManagerId.setText(_translate("ShowManagerInfo", "管理员ID:"))
        self.pushButton.setText(_translate("ShowManagerInfo", "退出管理员账号"))
        self.btn_searchStaffData.setText(_translate("ShowManagerInfo", "搜索考勤数据"))

    def getID( self,id ):
        return


if __name__ == "__main__":
    app = QApplication( sys.argv )
    
    TestUi=QWidget()
    #TestUi.setWindowFlags (Qt.FramelessWindowHint)
    TestUi.main_ui=Ui_ShowManagerInfo()
    TestUi.main_ui.setupUi(TestUi)
    TestUi.show()

    sys.exit( app.exec_() )
