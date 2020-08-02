#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :showsearchedstaffdata_win.py
@说明    : 新增加功能
@时间    :2020/07/31 21:46:50
@作者    :dongrui
@版本    :1.0
'''

import sys
import datetime
import pymysql
import socket
import time
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyUiFiles.proc_mainwin_staff_ui.showsearchedstaffdata_ui import Ui_ShowSearchedStaffData
from PyUiWidgets.TitleBar import UniversalTitle_Widget
#import workingSetDAO as workingDAO

print("2 widgetS!")

class ShowSearchedStaffData_Widget(QWidget, Ui_ShowSearchedStaffData):
    def __init__(self):
        super(ShowSearchedStaffData_Widget, self).__init__()

        self.mainUI = Ui_ShowSearchedStaffData()
        self.mainUI.setupUi(self)
        self.id = '213180005'

        # 打开数据库连接
        self.db = pymysql.connect("localhost","root","admin123","test_db" )
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        
        #  初始化折线图
        self.weekdata = []
        self.staffData = []
        self.getWeekData()
        self.getStaffData(id)
    
        '''init charts'''
        self.reBuildCompCharts()
        self.reBuildStaffChart()

    def reBuildCompCharts(self):
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
        self.mainUI.widget_totalHistoryChart.reBuild(self.weekdata,"公司过去一周考勤率(%)","考勤率",weekday)

    def getID( self,id ):
        self.id = id
        self.getStaffData( self.id )
        self.reBuildStaffChart()
        

    def reBuildStaffChart(self):
        # init line chart
        # get past 7 days
        cdate=QDate.currentDate()
        weekday=[cdate.addMonths(-1).toString("MM"),
            cdate.addMonths(-2).toString("MM"),
            cdate.addMonths(-3).toString("MM"),
            cdate.addMonths(-4).toString("MM"),
            cdate.addMonths(-5).toString("MM"),
            cdate.addMonths(-6).toString("MM"),]
        self.mainUI.widget_showStaffHistoryChart.reBuild(self.staffData, "您过去六月考勤次数", "考勤次数", weekday)


    #----------获取一周内的数据----------#
    def getWeekData( self ):
        cdate=QDate.currentDate()
        for i in range(1,7):
            #  get date
            cdate = cdate.addDays(-1)
            dateStr = cdate.toString("yyyy-MM-dd")
            print( dateStr )

            # 查表
            sql = "SELECT count(*) FROM signin WHERE signdate = '%s' AND ifworkday = 1"%(dateStr)
            self.cursor.execute( sql )
            self.db.commit()
            res = (self.cursor.fetchall()[0])[0]
            self.weekdata.append( res )

            print( res )
            print( type(res) )


    #----------员工整体考勤情况，以月计算---------#
    def getStaffData( self,id ):
         cdate=QDate.currentDate()
         for i in range( 1,6 ):
             #  get data
            cdate = cdate.addMonths(-1)
            dateStr = cdate.toString("yyyy-MM-dd")
            dateList = dateStr.split('-')
            startDate = self.getStartDate( dateList )
            if i == 1:
                endDate = dateStr
            else:
                endDate = str( str(dateList[0]) + '-' + str(dateList[1]) + '-' + str(1) )
            
            print(startDate + endDate)

            #  查表
            sql = "SELECT count(*) FROM signin WHERE signdate > '%s' AND signdate < '%s' AND id = '%s'"%(startDate,endDate,id)
            self.cursor.execute( sql )
            self.db.commit()
            res = (self.cursor.fetchall()[0])[0]
            self.staffData.append( res )
            

    def getStartDate( self,dateList ):
        # 上个月的日期
        year = dateList[0]
        month = dateList[1]
        day = dateList[2]

        if month == 1:
            return str( str(year-1) + '-' + str(12) + '-' + str(1) )
        else:
            return str( str(year) + '-' + str(month) + '-' + str(1) )


    #-------------获取员工所有的数据-----------#
    def getStaffAllData( self,id ):
        info = []
        '''
        name
        ID
        signinTimes
        late
        absence
        rank
        '''

        sql1 = "SELECT *FROM staff WHERE id = '%s' "%( id )
        self.cursor.execute( sql1 )
        self.db.commit()

        Res = self.cursor.fetchall()
        print( Res )
        res = self.cursor.fetchall()[0]
        name = res[1]

        # 获得这个月的考勤次数
        cdate=QDate.currentDate()
        dateStr = cdate.toString("yyyy-MM-dd")
        dateList = dateStr.split('-')
        startDate = self.getStartDate( dateList )
        print( startDate + " " + dateStr )

        #  signin times
        sql2 = "SELECT count(*) FROM signin WHERE signdate > '%s' AND signdate < '%s' AND id = '%s' AND stat = 0"%(startDate,dateStr,id)
        self.cursor.execute( sql2 )
        self.db.commit()
        res2 = (self.cursor.fetchall()[0])[0]
        signinTimes = res2

        #  late times
        sql3 = "SELECT count(*) FROM signin WHERE signdate > '%s' AND signdate < '%s' AND id = '%s' AND stat = 1"%(startDate,dateStr,id)
        self.cursor.execute( sql3 )
        self.db.commit()
        res3 = (self.cursor.fetchall()[0])[0]
        lateTimes = res3

        #  absence
        totalDays = dateList[2]
        absence = int(totalDays) - res2 - res3

        #  rank 
        rank = absence+1

        info.append( name )
        info.append( id )
        info.append( signinTimes )
        info.append( lateTimes )
        info.append( absence )
        info.append( rank )

        print( info )
        print( type(info) )

        return info

        

class ShowSearchedStaffData_Win(UniversalTitle_Widget):
    def __init__(self, *args, **kwargs):
        super(ShowSearchedStaffData_Win, self).__init__(*args, **kwargs)


        self.background = QWidget()
        self.background.setStyleSheet("background-color:rgb(235,235,235);")
        self.showsearchedstaffdatawidget=ShowSearchedStaffData_Widget()#  数据画图

        self.id = '213180005'

        #self.info = self.showsearchedstaffdatawidget.getStaffAllData( id )

        #  显示
        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.showsearchedstaffdatawidget)

        self.setWindowFlags (Qt.FramelessWindowHint)
        with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.setStyleSheet(TitleBarStyleSheet.read())
        self.setWidget(self.background)
        self.resize(QSize(1100,700))

        '''set background shadow effect'''
        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.background.setGraphicsEffect(shadow_effect)
   
    def getID(self,id):
        self.id = id
        self.showsearchedstaffdatawidget.getID( id )


if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=ShowSearchedStaffData_Win()
    mainwin.show()
    sys.exit(app.exec_())