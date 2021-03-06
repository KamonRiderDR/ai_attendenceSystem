# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowSearchedStaffData_ui.ui'
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
from PyUiWidgets.proc_showstaffattendance_widget import Proc_ShowStaffAttendance_Widget
from PyUiWidgets.proc_showcompdata_widget import Proc_ShowCompData_Widget

class Ui_ShowSearchedStaffData(object):
    def setupUi(self, ShowSearchedStaffData):
        ShowSearchedStaffData.setObjectName("ShowSearchedStaffData")
        ShowSearchedStaffData.resize(948, 608)
        self.layout_main = QtWidgets.QGridLayout(ShowSearchedStaffData)
        self.layout_main.setObjectName("layout_main")
        self.widget_showCalendar_container = QtWidgets.QWidget(ShowSearchedStaffData)
        self.widget_showCalendar_container.setObjectName("widget_showCalendar_container")


        self.layout_left = QtWidgets.QGridLayout(self.widget_showCalendar_container)
        self.layout_left.setObjectName("layout_left")
        self.widget_showHistoryChart_container = QtWidgets.QWidget(self.widget_showCalendar_container)
        self.widget_showHistoryChart_container.setObjectName("widget_showHistoryChart_container")
        self.layout_widgetShowHistoryChartContainer=QGridLayout(self.widget_showHistoryChart_container)

        self.widget_totalHistoryChart = LineChartFrame([1],"1","1",["1"])
        self.widget_totalHistoryChart.setObjectName("widget_totalHistoryChart")
        self.widget_totalHistoryChart.setStyleSheet("""QWidget{background-color: rgba(255,255,255,0);}""")

        self.layout_widgetShowHistoryChartContainer.addWidget(self.widget_totalHistoryChart)

        self.layout_left.addWidget(self.widget_showHistoryChart_container, 1, 0, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget_showCalendar_container)
        self.calendarWidget.setObjectName("calendarWidget")
        self.layout_left.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.layout_left.setRowStretch(0, 1)
        self.layout_left.setRowStretch(1, 1)
        self.layout_main.addWidget(self.widget_showCalendar_container, 0, 0, 1, 1)

        self.widget_showStaffData_container = QtWidgets.QWidget(ShowSearchedStaffData)
        self.widget_showStaffData_container.setObjectName("widget_showStaffData_container")
        self.layout_widgetShowStaffDataContainer=QVBoxLayout(self.widget_showStaffData_container)

        '''chart'''
        self.widget_showStaffHistoryChart = LineChartFrame([1],"1","1",["1"])
        self.widget_showStaffHistoryChart.setObjectName("widget_showStaffHistoryChart")

        self.widget_showStaffHistoryChart.setAttribute(Qt.WA_TranslucentBackground, True)
        self.widget_showStaffHistoryChart.setStyleSheet("""QWidget{background-color: rgba(255,255,255,0)}""")

        self.layout_widgetShowStaffDataContainer.addWidget(self.widget_showStaffHistoryChart)
        
        self.widget_showStaffDataChart=QWidget()
        self.widget_showStaffDataChart.setObjectName("widget_showStaffDataChart")
        self.layout_showStaffDataChart=QGridLayout(self.widget_showStaffDataChart)
        
        self.showstaffattendancewidget=Proc_ShowStaffAttendance_Widget()
        self.showstaffattendancewidget.setObjectName("showstaffattendancewidget")
        self.layout_showStaffDataChart.addWidget(self.showstaffattendancewidget)

        self.layout_widgetShowStaffDataContainer.addWidget(self.widget_showStaffDataChart)

        self.layout_widgetShowStaffDataContainer.setContentsMargins(9,9,9,9)
        self.layout_widgetShowStaffDataContainer.setStretch(0,2)
        self.layout_widgetShowStaffDataContainer.setStretch(1,3)

        '''layout settings'''
        self.layout_main.addWidget(self.widget_showStaffData_container, 0, 1, 1, 1)
        self.layout_main.setColumnStretch(0, 3)
        self.layout_main.setColumnStretch(1, 2)

        '''set calendar style'''
        with open("Qss/flatwhite_style.qss") as CalendarStyle:
            self.calendarWidget.setStyleSheet(CalendarStyle.read())

        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        self.calendarWidget.setFont(font)

        '''enhanced shadow effects'''
        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_showStaffData_container.setGraphicsEffect(shadow_effect)
        self.widget_showStaffData_container.setStyleSheet("""QWidget#widget_showStaffData_container{
                                background-color: rgba(127,255,0,90);
                                border-radius: 8px}""")
        
        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_showCalendar_container.setGraphicsEffect(shadow_effect)
        self.widget_showCalendar_container.setStyleSheet("""QWidget#widget_showCalendar_container{
                                background-color: rgba(255,69,0,90);
                                border-radius: 8px}""")

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_showHistoryChart_container.setGraphicsEffect(shadow_effect)
        self.widget_showHistoryChart_container.setStyleSheet("""QWidget#widget_showHistoryChart_container{
                                background-color: rgba(255,255,255,90);
                                border-radius: 8px}""")

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_showStaffDataChart.setGraphicsEffect(shadow_effect)
        self.widget_showStaffDataChart.setStyleSheet("""QWidget#widget_showStaffDataChart{
                                background-color: rgba(255,255,255,90);
                                border-radius: 8px}""")

        self.retranslateUi(ShowSearchedStaffData)
        QtCore.QMetaObject.connectSlotsByName(ShowSearchedStaffData)

    def retranslateUi(self, ShowSearchedStaffData):
        _translate = QtCore.QCoreApplication.translate
        ShowSearchedStaffData.setWindowTitle(_translate("ShowSearchedStaffData", "Form"))

if __name__ == "__main__":
    app = QApplication( sys.argv )
    
    TestUi=QWidget()
    TestUi.main_ui=Ui_ShowSearchedStaffData()
    TestUi.main_ui.setupUi(TestUi)
    TestUi.show()

    sys.exit( app.exec_() )
