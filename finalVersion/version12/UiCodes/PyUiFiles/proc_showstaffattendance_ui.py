# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Proc_ShowStaffAttendanceInfo_ui.ui'
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



class Ui_Proc_ShowStaffAttendanceInfo(object):
    def setupUi(self, Proc_ShowStaffAttendanceInfo):
        Proc_ShowStaffAttendanceInfo.setObjectName("Proc_ShowStaffAttendanceInfo")
        Proc_ShowStaffAttendanceInfo.resize(374, 377)
        self.gridLayout_2 = QtWidgets.QGridLayout(Proc_ShowStaffAttendanceInfo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Proc_ShowStaffAttendanceInfo)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_showCheckInNum = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_showCheckInNum.setFont(font)
        self.label_showCheckInNum.setObjectName("label_showCheckInNum")
        self.gridLayout.addWidget(self.label_showCheckInNum, 2, 0, 1, 1)
        self.label_showRank = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_showRank.setFont(font)
        self.label_showRank.setObjectName("label_showRank")
        self.gridLayout.addWidget(self.label_showRank, 5, 0, 1, 1)
        self.label_showStaffName = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_showStaffName.setFont(font)
        self.label_showStaffName.setObjectName("label_showStaffName")
        self.gridLayout.addWidget(self.label_showStaffName, 0, 0, 1, 1)
        self.label_showBreakNum = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_showBreakNum.setFont(font)
        self.label_showBreakNum.setObjectName("label_showBreakNum")
        self.gridLayout.addWidget(self.label_showBreakNum, 4, 0, 1, 1)
        self.label_showStaffId = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_showStaffId.setFont(font)
        self.label_showStaffId.setObjectName("label_showStaffId")
        self.gridLayout.addWidget(self.label_showStaffId, 1, 0, 1, 1)
        self.label_showLateNum = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_showLateNum.setFont(font)
        self.label_showLateNum.setObjectName("label_showLateNum")
        self.gridLayout.addWidget(self.label_showLateNum, 3, 0, 1, 1)
        self.lineEdit_showStaffName = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_showStaffName.setFont(font)
        self.lineEdit_showStaffName.setObjectName("lineEdit_showStaffName")
        self.gridLayout.addWidget(self.lineEdit_showStaffName, 0, 1, 1, 1)
        self.lineEdit_showStaffId = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_showStaffId.setFont(font)
        self.lineEdit_showStaffId.setObjectName("lineEdit_showStaffId")
        self.gridLayout.addWidget(self.lineEdit_showStaffId, 1, 1, 1, 1)
        self.lineEdit_showCheckInNum = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_showCheckInNum.setFont(font)
        self.lineEdit_showCheckInNum.setObjectName("lineEdit_showCheckInNum")
        self.gridLayout.addWidget(self.lineEdit_showCheckInNum, 2, 1, 1, 1)
        self.lineEdit_showLateNum = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_showLateNum.setFont(font)
        self.lineEdit_showLateNum.setObjectName("lineEdit_showLateNum")
        self.gridLayout.addWidget(self.lineEdit_showLateNum, 3, 1, 1, 1)
        self.lineEdit_showBreakNum = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_showBreakNum.setFont(font)
        self.lineEdit_showBreakNum.setObjectName("lineEdit_showBreakNum")
        self.gridLayout.addWidget(self.lineEdit_showBreakNum, 4, 1, 1, 1)
        self.lineEdit_showRank = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_showRank.setFont(font)
        self.lineEdit_showRank.setObjectName("lineEdit_showRank")
        self.gridLayout.addWidget(self.lineEdit_showRank, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        '''set line edit style'''
        with open("Qss/line_edit_style.qss") as LEditStyle:
            self.lineEdit_showBreakNum.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_showCheckInNum.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_showLateNum.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_showRank.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_showStaffId.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_showStaffName.setStyleSheet(LEditStyle.read())
            # LEditStyle.seek(0)

        self.lineEdit_showBreakNum.setReadOnly(True)
        self.lineEdit_showCheckInNum.setReadOnly(True)
        self.lineEdit_showLateNum.setReadOnly(True)
        self.lineEdit_showRank.setReadOnly(True)
        self.lineEdit_showStaffId.setReadOnly(True)
        self.lineEdit_showStaffName.setReadOnly(True)

        self.lineEdit_showBreakNum.setText( str(0) )
        self.lineEdit_showStaffName.setText("许德勤")
        self.lineEdit_showStaffId.setText( '213180001' )
        self.lineEdit_showCheckInNum.setText( str(30) )
        self.lineEdit_showLateNum.setText( str(0) )
        self.lineEdit_showRank.setText( str(1) )

        '''enhance shadow effect'''
        # shadow_effect=QGraphicsDropShadowEffect()
        # shadow_effect.setOffset(0,0)
        # shadow_effect.setColor(QColor("#444444"))
        # shadow_effect.setBlurRadius(5)
        # self.widget.setGraphicsEffect(shadow_effect)

        self.retranslateUi(Proc_ShowStaffAttendanceInfo)
        QtCore.QMetaObject.connectSlotsByName(Proc_ShowStaffAttendanceInfo)

    def retranslateUi(self, Proc_ShowStaffAttendanceInfo):
        _translate = QtCore.QCoreApplication.translate
        Proc_ShowStaffAttendanceInfo.setWindowTitle(_translate("Proc_ShowStaffAttendanceInfo", "Form"))
        self.label_showCheckInNum.setText(_translate("Proc_ShowStaffAttendanceInfo", "本月考勤次数:"))
        self.label_showRank.setText(_translate("Proc_ShowStaffAttendanceInfo", "本月公司内排名:"))
        self.label_showStaffName.setText(_translate("Proc_ShowStaffAttendanceInfo", "员工姓名:"))
        self.label_showBreakNum.setText(_translate("Proc_ShowStaffAttendanceInfo", "本月请假次数:"))
        self.label_showStaffId.setText(_translate("Proc_ShowStaffAttendanceInfo", "员工ID:"))
        self.label_showLateNum.setText(_translate("Proc_ShowStaffAttendanceInfo", "本月迟到次数:"))

if __name__ == "__main__":
    app = QApplication( sys.argv )
    
    TestUi=QWidget()
    #TestUi.setWindowFlags (Qt.FramelessWindowHint)
    TestUi.main_ui=Ui_Proc_ShowStaffAttendanceInfo()
    TestUi.main_ui.setupUi(TestUi)
    TestUi.show()

    sys.exit( app.exec_() )