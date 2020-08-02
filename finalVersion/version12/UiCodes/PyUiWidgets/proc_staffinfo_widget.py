import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
import pymysql
import socket
import sys
import time
import json

from PyUiFiles.proc_staffinfo_ui import Ui_Proc_StaffInfo
from PyUiWidgets.proc_addstaff_win import Proc_AddStaff_Win
from UiCodes.WorksFromDR import workingSetDAO as workingDAO

class Proc_StaffInfo_Widget(QWidget, Ui_Proc_StaffInfo):
    def __init__(self):
        super(Proc_StaffInfo_Widget, self).__init__()

        '''init ui'''
        self.main_ui=Ui_Proc_StaffInfo()
        self.main_ui.setupUi(self)
        self.adjustSize()

         # 打开数据库连接
        self.db = pymysql.connect("localhost","root","admin123","test_db" )
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

        self.initTableView()

        #  初始化折线图
        self.weekdata = []
        # self.getWeekData()
        self.weekdata = workingDAO.getWorkingDay()
        self.staffData = []
        self.staffData = workingDAO.getStaffWorkingTime( '213180008' )

        self.reBuildCompCharts(  )
        self.reBuildStaffChart(  )
        #  end

        '''sub win'''
        self.addstaffwin=Proc_AddStaff_Win()

    #---------画折线图：公司的考勤----------#
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
        self.main_ui.widget_totalHistoryChart.reBuild(self.weekdata,"公司过去一周考勤率(%)","考勤率",weekday)

    #---------画折线图：员工的考勤----------#
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
        self.main_ui.widget_showStaffHistoryChart.reBuild(self.staffData, "该员工过去六月考勤次数", "考勤次数", weekday)

    def slot_showAddStaffWin(self):
        self.addstaffwin.show()

    def slot_searchForStaffInfo(self):
        text = self.main_ui.lineEditSearch.text()
        #  判断是否为学号
        if text[0:5] == '21318' and len(text) == 9:
            #self.getStaffData( text )
            self.staffData = workingDAO.getStaffWorkingTime(text)
            self.reBuildStaffChart()
            print( text )
            self.reBuildStaffChart()
            info = self.getStaffAllData( str(text) )
            self.main_ui.refreshStaffData( info )
            self.main_ui.lineEditSearch.setText("")
        else:
            QMessageBox.information( self,"提示","无效的学号，请重新输入" )
            self.main_ui.lineEditSearch.setText("")

    #------------tableview点击选择员工-------#
    def tableViewSelectStaff(self):
        row = self.main_ui.tableView.currentIndex().row()
        print( row )
        model = self.main_ui.tableView.model()
        element = model.index( row,0 ).data()
        print( element )
        
        #  更新 -> 画两张图，更新一个表
        self.staffData = workingDAO.getStaffWorkingTime( element )
        self.reBuildCompCharts(  )
        self.reBuildStaffChart(  )

        info = self.getStaffAllData( str( element ) )
        self.main_ui.refreshStaffData( info )
        self.main_ui.lineEditSearch.setText("")



    def slot_deleteStaff(self):
        return 


    '''
    功能函数与图表绘制
    @作者    :dongrui
    @版本    :1.0
    '''
    
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
            

    #------------获得正确的时间跨度-----------#
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

    #-----------初始化tableview的数据---------#
    def initTableView( self ):
        headers = [ "ID","姓名","adnum" ]        
        sql = "SELECT *FROM staff"
        self.cursor.execute( sql )
        self.db.commit()
        res = self.cursor.fetchall()
        
        i = 0
        for element in res:
            i += 1
        
        model=QStandardItemModel(i,3)#存储任意结构数据
        model.setHorizontalHeaderLabels( headers )

        #水平方向标签拓展剩下的窗口部分，填满表格
        self.main_ui.tableView.horizontalHeader().setStretchLastSection(True)
        #水平方向，表格大小拓展到适当的尺寸   
        self.main_ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        print("!")

        for row in range(i):
            for column in range(3):
                e = QStandardItem( res[row][column] )
                model.setItem( row,column,e )
        self.main_ui.tableView.horizontalHeader().setSectionResizeMode( QHeaderView.Stretch )
        self.main_ui.tableView.setModel( model )

        

        


if __name__ == "__main__":
    app = QApplication( sys.argv )
    testUI = Proc_StaffInfo_Widget()
    testUI.show()
    sys.exit( app.exec_() )