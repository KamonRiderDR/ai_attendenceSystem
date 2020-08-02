# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyUiFiles.proc_mainwin_staff_ui.proc_mainwin_ui_staff import Proc_MainWin_Ui_Staff
sys.path.append('../')
from ServerProcject.calendarControl.calendarServer import CalendarServer
from PyUiWidgets.CheckIn_Win import CheckIn_Win
from PyUiWidgets.breakday_apply_win import BreakDay_Apply_Win
from PyUiWidgets.complain_apply_win import Complain_Apply_Win

from DataViewWidgets.piechart_widget.pieChartMain import PieChartFrame
from DataViewWidgets.linechart_widget.lineChartMain import LineChartFrame


class Proc_MainWin_Widget_Staff(QWidget, Proc_MainWin_Ui_Staff):
    def __init__(self):
        super(Proc_MainWin_Widget_Staff, self).__init__()

        '''init ui'''
        self.main_ui=Proc_MainWin_Ui_Staff()
        self.main_ui.setupUi(self)
        self.adjustSize()

        '''init show attendance info'''
        self.initDataCharts()

        '''set date imgs'''
        cdate=QDate.currentDate()
        self.setDateImg(cdate.month())


        '''init needed windows'''
        self.checkinwin=CheckIn_Win()
        self.breakdayapplywin=BreakDay_Apply_Win()
        self.complainapplywin=Complain_Apply_Win()

        '''init chart'''
        self.c = CalendarServer(self.main_ui.calendarWidget)

    def initDataCharts(self):
        # init pie chart
        todayData=[32,2,100-32-2]
        self.main_ui.totalattendance_container_widget.main_ui.widget_showPieChart.reBuild(todayData,["尚未打卡","请假","已打卡"])
        weekdata=[91,93,84,87,95,89,98]

        # init line chart
        # get past 7 days
        cdate=QDate.currentDate()
        weekday=[cdate.addDays(-1).toString("ddd"),
            cdate.addDays(-2).toString("ddd"),
            cdate.addDays(-3).toString("ddd"),
            cdate.addDays(-4).toString("ddd"),
            cdate.addDays(-5).toString("ddd"),
            cdate.addDays(-6).toString("ddd"),
            cdate.addDays(-7).toString("ddd")]
        self.main_ui.totalattendance_container_widget.main_ui.widget_showHistory.reBuild(weekdata,"过去一周考勤率(%)","",weekday)

        # get number of people
        # 尚未打卡人数
        self.main_ui.totalattendance_container_widget.main_ui.LEdit_showUncheckedNum.setText("64")
        self.main_ui.totalattendance_container_widget.main_ui.LEdit_showUncheckedNum.setReadOnly(True)
        #已打卡人数
        self.main_ui.totalattendance_container_widget.main_ui.LEdit_showCheckedNum.setText("112")
        self.main_ui.totalattendance_container_widget.main_ui.LEdit_showCheckedNum.setReadOnly(True)
        # 请假人数
        self.main_ui.totalattendance_container_widget.main_ui.LEdit_showBreakNum.setText("4")
        self.main_ui.totalattendance_container_widget.main_ui.LEdit_showBreakNum.setReadOnly(True)

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

    def setDateImg(self, monthnum):
        '''set img'''
        pix=QPixmap()
        monthname=self.switchif_getMonthName(monthnum)
        img=QImage("months_imgs/"+monthname+".PNG")
        self.main_ui.label_showMonthInfo.setPixmap(pix.fromImage(img))
        self.main_ui.label_showMonthInfo.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.main_ui.label_showMonthInfo.setScaledContents(True)
        self.main_ui.label_showMonthInfo.setStyleSheet("border-radius:8px;")

    def slot_GetCheckInWin(self):
        self.checkinwin.resize(1120, 700)
        self.checkinwin.show()

    def slot_BreakDayApply(self):
        self.breakdayapplywin.resize(597, 643)
        self.breakdayapplywin.show()

    def slot_ComplainApply(self):
        self.complainapplywin.resize(596, 680)
        self.complainapplywin.show()

    def pageChange(self):
        self.c.calendarPaint()
        print(self.main_ui.calendarWidget.monthShown())

        

