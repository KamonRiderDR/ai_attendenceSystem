# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attendanceinfo_ui.ui'
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
from PyQt5.QtChart import *

from DataViewWidgets.piechart_widget.pieChartMain import PieChartFrame
from DataViewWidgets.linechart_widget.lineChartMain import LineChartFrame

class Ui_AttendanceInfo_ui(object):
    def setupUi(self, AttendanceInfo_ui):
        AttendanceInfo_ui.setObjectName("AttendanceInfo_ui")
        AttendanceInfo_ui.resize(1009, 361)

        '''main layout -- gridLayout_4'''
        self.gridLayout_4 = QtWidgets.QGridLayout(AttendanceInfo_ui)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)


        '''widget as background to show attendance progress''' 
        self.widget_showProgress = QtWidgets.QWidget(AttendanceInfo_ui)
        self.widget_showProgress.setObjectName("widget_showProgress")
        self.widget_showProgress.setAttribute(Qt.WA_TranslucentBackground, True)

        '''layout for widget_showProgress'''
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_showProgress)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layout_showPieChart = QtWidgets.QVBoxLayout()
        self.layout_showPieChart.setObjectName("layout_showPieChart")
        self.label_showPieChartTitle = QtWidgets.QLabel(self.widget_showProgress)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_showPieChartTitle.setFont(font)
        self.label_showPieChartTitle.setObjectName("label_showPieChartTitle")
        self.label_showPieChartTitle.setAttribute(Qt.WA_TranslucentBackground, True)
        self.layout_showPieChart.addWidget(self.label_showPieChartTitle)

        ''' @widget_showPieChart: widget to show chart'''
        self.widget_showPieChart = PieChartFrame([],[])
        self.widget_showPieChart.setAttribute(Qt.WA_TranslucentBackground, True)
        self.widget_showPieChart.setStyleSheet("background-color:rgba(255,255,255,0);")
        self.widget_showPieChart.setObjectName("widget_showPieChart")
        self.layout_showPieChart.addWidget(self.widget_showPieChart)
        self.layout_showPieChart.setStretch(0, 1)
        self.layout_showPieChart.setStretch(1, 400)

        self.layout_showPieChart.setContentsMargins(0, 0, 0, 0)
        self.layout_showPieChart.setSpacing(0)

        self.gridLayout_2.addLayout(self.layout_showPieChart, 0, 0, 1, 1)

        '''show number info'''
        self.widget_showProgressNumber = QtWidgets.QWidget(self.widget_showProgress)
        self.widget_showProgressNumber.setObjectName("widget_showProgressNumber")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_showProgressNumber)
        self.gridLayout.setObjectName("gridLayout")
        self.LEdit_showCheckedNum = QtWidgets.QLineEdit(self.widget_showProgressNumber)
        self.LEdit_showCheckedNum.setObjectName("LEdit_showCheckedNum")
        self.gridLayout.addWidget(self.LEdit_showCheckedNum, 1, 0, 1, 1)
        self.label_uncheckedNum = QtWidgets.QLabel(self.widget_showProgressNumber)
        self.label_uncheckedNum.setAttribute(Qt.WA_TranslucentBackground, True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_uncheckedNum.setFont(font)
        self.label_uncheckedNum.setObjectName("label_uncheckedNum")
        self.gridLayout.addWidget(self.label_uncheckedNum, 2, 0, 1, 1)
        self.label_checkedNum = QtWidgets.QLabel(self.widget_showProgressNumber)
        self.label_checkedNum.setAttribute(Qt.WA_TranslucentBackground, True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_checkedNum.setFont(font)
        self.label_checkedNum.setObjectName("label_checkedNum")
        self.gridLayout.addWidget(self.label_checkedNum, 0, 0, 1, 1)
        self.LEdit_showUncheckedNum = QtWidgets.QLineEdit(self.widget_showProgressNumber)
        self.LEdit_showUncheckedNum.setObjectName("LEdit_showUncheckedNum")
        self.gridLayout.addWidget(self.LEdit_showUncheckedNum, 3, 0, 1, 1)
        self.label_showBreakNum = QtWidgets.QLabel(self.widget_showProgressNumber)
        self.label_showBreakNum.setAttribute(Qt.WA_TranslucentBackground, True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_showBreakNum.setFont(font)
        self.label_showBreakNum.setObjectName("label_showBreakNum")
        self.gridLayout.addWidget(self.label_showBreakNum, 4, 0, 1, 1)
        self.LEdit_showBreakNum = QtWidgets.QLineEdit(self.widget_showProgressNumber)
        self.LEdit_showBreakNum.setObjectName("LEdit_showBreakNum")
        self.gridLayout.addWidget(self.LEdit_showBreakNum, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_showProgressNumber, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_4.addWidget(self.widget_showProgress, 0, 0, 1, 1)

        '''widget as background to show attendance history'''
        self.widget_showHistory = LineChartFrame([1],"","",["1"])
        self.widget_showHistory.setObjectName("widget_showHistory")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_showHistory)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_showHistoryTitle = QtWidgets.QLabel(self.widget_showHistory)

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_showHistory.setGraphicsEffect(shadow_effect)
        self.widget_showHistory.setStyleSheet("""QWidget{
                                                    background-color: rgba(255,255,255, 90);
                                                    border-radius: 8px}""")

        self.label_showHistoryTitle.setAttribute(Qt.WA_TranslucentBackground, True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_showHistoryTitle.setFont(font)
        self.label_showHistoryTitle.setObjectName("label_showHistoryTitle")
        self.gridLayout_3.addWidget(self.label_showHistoryTitle, 0, 0, 1, 1)

        '''widget to show history chart'''
        self.widget_showHistoryChart = QtWidgets.QWidget(self.widget_showHistory)
        self.widget_showHistoryChart.setObjectName("widget_showHistoryChart")
        self.widget_showHistoryChart.setAttribute(Qt.WA_TranslucentBackground, True)
        #self.widget_showHistoryChart.setStyleSheet("background-color:rgb(0,0,0);")
        
        '''set layout'''
        self.gridLayout_3.addWidget(self.widget_showHistoryChart, 1, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 4)
        self.gridLayout_4.addWidget(self.widget_showHistory, 0, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 2)

        '''show charts based on @widget_showPieChart and @widget_showHistoryChart '''

        '''set line edit style'''
        with open("Qss/line_edit_style.qss") as LEditStyle:
            self.LEdit_showBreakNum.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.LEdit_showCheckedNum.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.LEdit_showUncheckedNum.setStyleSheet(LEditStyle.read()) 
        
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.LEdit_showBreakNum.setFont(font)
        self.LEdit_showCheckedNum.setFont(font)
        self.LEdit_showUncheckedNum.setFont(font)

        '''enhance shadow effects'''
        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_showProgressNumber.setGraphicsEffect(shadow_effect)
        self.widget_showProgressNumber.setStyleSheet("""QWidget#widget_showProgressNumber{
                                                    background-color: rgba(255,255,255, 90);
                                                    border-radius: 8px}""")

        self.retranslateUi(AttendanceInfo_ui)
        QtCore.QMetaObject.connectSlotsByName(AttendanceInfo_ui)

    def retranslateUi(self, AttendanceInfo_ui):
        _translate = QtCore.QCoreApplication.translate
        AttendanceInfo_ui.setWindowTitle(_translate("AttendanceInfo_ui", "Form"))
        self.label_showPieChartTitle.setText(_translate("AttendanceInfo_ui", "今日签到情况(截至当前):"))
        self.label_uncheckedNum.setText(_translate("AttendanceInfo_ui", "今日尚未打卡人数(包括请假):"))
        self.label_checkedNum.setText(_translate("AttendanceInfo_ui", "今日已打卡人数:"))
        self.label_showBreakNum.setText(_translate("AttendanceInfo_ui", "今日请假人数:"))
        self.label_showHistoryTitle.setText(_translate("AttendanceInfo_ui", ""))


if __name__ == "__main__":
    app = QApplication( sys.argv )
    
    TestUi=QWidget()
    TestUi.main_ui=Ui_AttendanceInfo_ui()
    TestUi.main_ui.setupUi(TestUi)
    TestUi.show()

    sys.exit( app.exec_() )