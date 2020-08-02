# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from DataViewWidgets.piechart_widget.pieChartMain import PieChartFrame
from DataViewWidgets.linechart_widget.lineChartMain import LineChartFrame
sys.path.append('../')
from ServerProcject.staffInfoServer import StaffInfoServer
from ServerProcject.calendarControl.calendarServer import CalendarServer
from PyUiFiles.proc_mainpage_ui import Ui_Proc_MainPage

class Proc_MainPage_Widget(QWidget, Ui_Proc_MainPage):
    def __init__(self):
        super(Proc_MainPage_Widget, self).__init__()

        self.main_ui=Ui_Proc_MainPage()
        self.main_ui.setupUi(self)

        self.setAPieChart([96,3],["考勤率",""])
        self.setBPieChart([4,99],["请假率",""])
        self.setBarChart([101,97,96,89,97,89,99],"过去一周请假人数")

        cdate=QDate.currentDate()
        self.setDateImgs(cdate.month())
        self.staffInfoServer = StaffInfoServer()
        self.setStaffInfo()
        self.c = CalendarServer(self.main_ui.calendarWidget)

    def setStaffInfo(self):
        self.main_ui.label_topBar_totalNum_num.setText(str(self.staffInfoServer.staffNumber()))
        self.main_ui.label_topBar_checkedNum_num.setText(str(self.staffInfoServer.todayCheck()))
        self.main_ui.label_topBar_requestNum_num.setText(str(self.staffInfoServer.quest()))
        self.main_ui.label_topBar_personChgNum_num.setText(str(self.staffInfoServer.staffChange()))

    def pageChange(self):
        self.c.calendarPaint()
        print(self.main_ui.calendarWidget.monthShown())

    def setAPieChart(self, x_data, slice_name):
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.main_ui.widget_showPieChart_aRate.reBuild(x_data,slice_name)
        self.main_ui.widget_showPieChart_aRate.ui.chartView.chart().setTitle("本周考勤率(%)")
        self.main_ui.widget_showPieChart_aRate.ui.chartView.chart().setTitleFont(font)
        series=self.main_ui.widget_showPieChart_aRate.ui.chartView.chart().series()[0]
        series.slices()[0].setColor(QColor(127,255,0))
        series.slices()[1].setColor(QColor(85,107,47))
        series.slices()[1].setLabelVisible(False)

    def setBPieChart(self, x_data, slice_name):
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.main_ui.widget_showPieChart_bRate.reBuild(x_data,slice_name)
        self.main_ui.widget_showPieChart_bRate.ui.chartView.chart().setTitle("本周请假率(%)")
        self.main_ui.widget_showPieChart_bRate.ui.chartView.chart().setTitleFont(font)
        series=self.main_ui.widget_showPieChart_bRate.ui.chartView.chart().series()[0]
        series.slices()[0].setColor(QColor(255,69,0))
        series.slices()[1].setColor(QColor(188,143,143))
        series.slices()[1].setLabelVisible(False)

    def setBarChart(self, data, title):
        cdate=QDate.currentDate()
        weekday=[cdate.addDays(-1).toString("ddd"),
            cdate.addDays(-2).toString("ddd"),
            cdate.addDays(-3).toString("ddd"),
            cdate.addDays(-4).toString("ddd"),
            cdate.addDays(-5).toString("ddd"),
            cdate.addDays(-6).toString("ddd"),
            cdate.addDays(-7).toString("ddd")]

        self.main_ui.widget_showBarChart.reBuild(data, title, weekday)

    def switchif_getMonthName(self, monthnum):
        if(monthnum==1):
            return "Jan"
        elif(monthnum==2):
            return "Feb"
        elif(monthnum==3):
            return "Mar"
        elif(monthnum==4):
            return "Apr"
        elif(monthnum==5):
            return "May"
        elif(monthnum==6):
            return "Jun"
        elif(monthnum==7):
            return "Jul"
        elif(monthnum==8):
            return "Aug"
        elif(monthnum==9):
            return "Sep"
        elif(monthnum==10):
            return "Oct"
        elif(monthnum==11):
            return "Nov"
        elif(monthnum==12):
            return "Dec"
        else:
            return ""

    def setDateImgs(self, monthnum):
        pix=QPixmap()
        monthname=self.switchif_getMonthName(monthnum)

        img=QImage("months_imgs/"+monthname+".PNG")

        self.main_ui.label_showDate_month.setPixmap(pix.fromImage(img))
        self.main_ui.label_showDate_month.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.main_ui.label_showDate_month.setScaledContents(True)
        self.main_ui.label_showDate_month.setStyleSheet("border-radius:8px;")

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=Proc_MainPage_Widget()
    mainwin.show()
    sys.exit(app.exec_())
