# -*- coding: utf-8 -*-

import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2 
import csv
import pymysql
import socket
import sys
import time
import json
import datetime

sys.path.append("..")
from PyUiFiles.proc_moresetting_ui import Proc_MoreSetting_Ui
from UiCodes.WorksFromDR.ImportWorkingDay import HolidayRequest
from UiCodes.WorksFromDR import workingSetDAO as workingDAO
from client import getMacInfo,deleteMac,addMac

class Proc_MoreSetting_Widget(QWidget, Proc_MoreSetting_Ui):
    def __init__(self):
        super(Proc_MoreSetting_Widget,self).__init__()
        
        '''initiation by DR'''
        self.mainUI = Proc_MoreSetting_Ui()
        self.mainUI.setupUi( self )
        self.setWindowOpacity(0.99)
        
        img1 = QImage(  )
        img1.load( "./image/workingWidget2.jpg" )
        img2  =QImage()
        img2.load("./image/workingWidget.jpg" )
        
        self.data = []
        self.dataSave = []
        
        #  设置初始的考勤时间
        file = open('./WorksFromDR/workingTime.txt','r')
        res = file.readlines()
        print(type(res))
        start = res[0].rstrip().split(':')
        end = res[1].split(':')
        print( start )
        print( end )
        self.mainUI.timeEdit.setTime( QTime(int( start[0] ),int( start[1] ) ) )
        self.mainUI.timeEdit_2.setTime( QTime(int( end[0] ),int( end[1] )) )
        file.close()

        self.setWindowFlags( QtCore.Qt.WindowStaysOnTopHint )
        self.readFromCSV()

        cdate=QDate.currentDate()   #获取今天的日期
        format=QTextCharFormat()     
        format.setBackground(QColor(95,158,160))  #设置格式，颜色自选
        self.mainUI.calendarWidget.setDateTextFormat(cdate, format) #生效配置
        '''initiaion by TYY'''
        cdate=QDate.currentDate()
        self.setDateImgs(cdate.month())

        #workingDAO.getWorkingDay()
        #workingDAO.getStaffWorkingTime( '213180001' )
   
        '''initiation by ADK'''
        self.macInfo=[]
        self.setMacInfo()

        
    def setMacInfo(self):
        self.macInfo=getMacInfo()       
        self.model=QStandardItemModel(len(self.macInfo),1)#存储任意结构数据
        self.model.setHorizontalHeaderLabels(['物理地址'])
        #水平方向标签拓展剩下的窗口部分，填满表格
        self.mainUI.tableView.horizontalHeader().setStretchLastSection(True)
        #水平方向，表格大小拓展到适当的尺寸   
        self.mainUI.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for index,mac in enumerate(self.macInfo):
            item=QStandardItem(''.join(mac))
            self.model.setItem(index,0,item)

        self.mainUI.tableView.setModel(self.model)
    
        

        #workingDAO.getWorkingDay()
        #workingDAO.getStaffWorkingTime( '213180001' )

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

        self.mainUI.label_showMonthInfo.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.mainUI.label_showMonthInfo.setScaledContents(True)
        self.mainUI.label_showMonthInfo.setStyleSheet("border-radius:8px;")


    '''
    @文件    :proc_moresetting_widget.py
    @说明    :工作时间相关的功能实现
    @时间    :2020/07/27 10:47:54
    @作者    :DR
    @版本    :1.4
    '''
    '''slot function by DR'''
    #-----------槽函数--------------#    
    #-------------导入国家工作日-------------#
    def workingDayImport( self ):
        HolidayImport = HolidayRequest( '2020' )
        HolidayImport.parseHTML()

        # 数据的保存和日历的重绘
        self.dataSave = HolidayImport.dataSave #---> mysql
        print( type(self.dataSave) )
        self.data = HolidayImport.dataRes
        print( self.data )
        print("paint!")

        # repaint calendar
        self.paintCalendar()

        try:
        # 与数据库交互
            workingDAO.workingDaySave( self.dataSave )
            QMessageBox.information( self,"提示","工作日已经导入！" )
        except:
            QMessageBox.information( self,"提示","设置失败，请查看连接后重试" )

    def cancelFunc3( self ):
        print( "取消导入工作日！" )
        QMessageBox.information( self,"提示","已经取消导入国家工作日！" )
        

    #------------设定选中为工作日------------#
    def setWorkingDay( self ):
        print( "Save Working day!" )
        workingDate = self.mainUI.calendarWidget.selectedDate()
        year = workingDate.year()
        month = workingDate.month()
        day = workingDate.day()
        print( year + month + day )

        
        date = datetime.datetime(year,month,day)
        Date = date.strftime('%Y-%m-%d')
        print( type(Date) )
        
        today = datetime.date.today()
        todayStr = today.strftime( '%Y-%m-%d' )

        if self.judgeWorkingDay( Date,todayStr ) == True:

            #  send new msg
            res = []
            res.append( [Date,1] )
            try :
                #  存入csv文件
                filename = "./WorksFromDR/2020Holiday.csv"
                #headers = ['Date' , 'Tag']
                #csvFile = open( filename,'a',newline='')
                with open( filename,"a+",newline='') as csvFile:
                    csvWrite = csv.writer( csvFile ) 
                   
                    csvWrite.writerows(res)
                    print("Open!")
                    #f_csv.writerows(res)
                    print( "添加成功！" )

                    # repaint()
                cmdFormat = QtGui.QTextCharFormat()
                brush = QtGui.QBrush()
                brush.setColor( QtGui.QColor( "LightGreen" ) )
                cmdFormat.setBackground( brush )
                self.mainUI.calendarWidget.setDateTextFormat( workingDate,cmdFormat )
                    
                workingDAO.workingDaySave( res )

                QMessageBox.information( self,"提示","%s 设定为工作日"%(Date)  )

            except:
                QMessageBox.information( self,"提示","设置失败，请查看连接后重试" )

        else:
            QMessageBox.information( self,"提示","无效的工作日设定！" )    
    
    #---------------设定该日期休息------------------#
    def cancelSetWorkingDay( self ):
        print( "Save Resting day!" )
        workingDate = self.mainUI.calendarWidget.selectedDate()
        year = workingDate.year()
        month = workingDate.month()
        day = workingDate.day()
        print( str(year) + str(month) + str(day) )

        date = datetime.datetime(year,month,day)
        Date = date.strftime('%Y-%m-%d')
        print( type(Date) )
        today = datetime.date.today()
        todayStr = today.strftime('%Y-%m-%d')

        if self.judgeWorkingDay( Date,todayStr ) == True:
             #  send new msg
            res = []
            res.append( [Date,0] )

            try:
                #  存入csv文件
                filename = "./WorksFromDR/2020Holiday.csv"
                #headers = ['Date' , 'Tag']
                #csvFile = open( filename,'a',newline='')
                with open( filename,"a+",newline='') as csvFile:
                    csvWrite = csv.writer( csvFile ) 
                   
                    csvWrite.writerows(res)
                    print("Open!")
                    #f_csv.writerows(res)
                    print( "添加成功！" )

                # repaint()
                cmdFormat = QtGui.QTextCharFormat()
                brush = QtGui.QBrush()
                brush.setColor( QtGui.QColor( "LightBlue" ) )
                cmdFormat.setBackground( brush )
                self.mainUI.calendarWidget.setDateTextFormat( workingDate,cmdFormat )

                workingDAO.workingDaySave( res )
                
                QMessageBox.information( self,"提示","%s设定为休息日"%(Date)  )
            except:
                QMessageBox.information(self,"提示","设置失败，请查看连接后重试")
        else:
            QMessageBox.information( self,"提示","无效的休息日设定！" )    

    #------------设定该时间段考勤----------------#
    def setWorkingTime( self ):
        self.mainUI.timeEdit.setEnabled(True)
        self.mainUI.timeEdit_2.setEnabled(True)
        # 获取TimeEdit的时间
        startTime = self.mainUI.timeEdit.time()
        endTime = self.mainUI.timeEdit_2.time()

        startTimeHour = startTime.hour()
        startTimeMinute = startTime.minute()

        endTimeHour = endTime.hour()
        endTimeMinute = endTime.minute()

        print(startTimeHour + startTimeMinute)
        print( startTime )
        print( endTimeHour + endTimeMinute )
        print( endTime )

        startTimeSave = str("%s:%s"%(startTimeHour,startTimeMinute))
        endTimeSave = str("%s:%s"%(endTimeHour,endTimeMinute))
        self.mainUI.timeEdit.setEnabled(True)
        self.mainUI.timeEdit_2.setEnabled(True)

       
        try:
            workingDAO.workingTimeSave( startTimeSave,endTimeSave )
            #  保存到txt中，开机读取
            file = open('./WorksFromDR/workingTime.txt','w')
            #  先清空
            file.truncate()
            file.writelines( startTimeSave )
            file.writelines('\n')
            file.writelines( endTimeSave )
            file.close()
            QMessageBox.information( self,"提示","考勤时间已重新设定！" )
        except:
            QMessageBox.information( self,"提示","设置失败，请检查连接后重试" )    

    def cancelSetWorkingTime( self ):
        QMessageBox.information( self,"提示","已经取消考勤时间的设定！" )
        
     #------------end slot-------------------#


    '''
    部分功能模块的函数
    '''
   
    def paintCalendar( self ):
        # ---read data----#
        print("start painting!")
        for dataTemp in self.data:
            #dataTemp = self.data[index]
            #print(dataTemp)
            dataStr = ''.join(dataTemp)
            data = dataStr.split( "-" ) 
            #print( data )
            year = int(data[0])
            month = int(data[1])
            day = int(data[2])
            dateTemp = QDate( year,month,day )
            cmdFormat = QtGui.QTextCharFormat()
            brush = QtGui.QBrush()
            brush.setColor( QtGui.QColor(127,255,170) )
            cmdFormat.setBackground( brush )
            self.mainUI.calendarWidget.setDateTextFormat( dateTemp,cmdFormat )
        print("end painting!")


    def paintCalendarSingle( self,date,number ):
        cmdFormat = QtGui.QTextCharFormat()
        if number == 0:
            # rest -> LightBlue
            brush = QtGui.QBrush()
            brush.setColor( QtGui.QColor(255,192,203,90) )
            cmdFormat.setBackground( brush )
            self.mainUI.calendarWidget.setDateTextFormat( date,cmdFormat )
        else:
            # rest -> LightPink
            brush = QtGui.QBrush()
            brush.setColor( QtGui.QColor(144,238,144,90) )
            cmdFormat.setBackground( brush )
            self.mainUI.calendarWidget.setDateTextFormat( date,cmdFormat )


    #-----读取CSV的内容进行重绘
    def readFromCSV(self):
        filename = "./WorksFromDR/2020Holiday.csv"
        csvFile = open( filename,encoding='utf-8' )
        csvReader = csv.reader( csvFile )
        print (csvReader)
        for i,rows in enumerate(csvReader):
            if i >= 1:
                # read data
                date = rows[0]
                isWorkingDay = rows[1]
                
                date = date.split('-')
                year = int(date[0])
                month = int(date[1])
                day = int(date[2])
               # self.dataSave.append( [rows[0],rows[1]] )
                dateRes = QDate( year,month,day )
                self.paintCalendarSingle( dateRes,int(rows[1]) )
       # workingDAO.workingDaySave( self.dataSave )


    #------------判断工作日与休息日是否在范围之内------------#
    def judgeWorkingDay( self,Date,today ):
        DateList = Date.split('-')
        todayList = today.split('-')
        print(DateList)
        print(todayList)
        if DateList[0] < todayList[0]:
            return False
        elif DateList[0] > todayList[0]:
            return True
        elif DateList[1] < todayList[1]:
            return False
        elif DateList[1] > todayList[1]:
            return True
        elif DateList[2] < todayList[2]:
            return False
        else:
             return True

      #-----------判断工作时间是否符合要求-----------#
    def judgeWorkingTime(self,startTime,endTime):
        startTimeHour = startTime.hour()
        startTimeMin = startTime.minute()
        print(startTime)
        print(endTime)
        endTimeHour = endTime.hour()
        endTimeMin = endTime.minute()
        # 判断
        if startTime.hour() < 7 or endTimeHour >= 9:
            return False
        elif startTimeHour < endTimeHour:
            return True
        elif startTimeHour >endTimeHour:
            return False
        elif startTimeMin < endTimeMin:
            return True
        else:
            return False

    #----------重新设定考勤时间------------#
    def resetWorkingTime( self ):
        self.mainUI.timeEdit.setTime( QTime(7,30) )
        self.mainUI.timeEdit_2.setTime( QTime(8,0) )
        



    '''slot functions by ADK'''
    def addMac(self):
        mac=self.mainUI.lineEditAddMac.text()
        result=addMac(mac)
        if result=="True":
            QMessageBox.information(self,"考勤机器管理","添加机器成功！",QMessageBox.Yes)
            self.setMacInfo()
        else:
            QMessageBox.information(self,"考勤机器管理","添加机器失败！！！",QMessageBox.Yes)
        self.mainUI.lineEditAddMac.setText('')
    def deleteMac(self):
        mac=self.mainUI.lineEditDeleteMac.text()
        result=deleteMac(mac)
        if result=="True":
            QMessageBox.information(self,"考勤机器管理","删除机器成功！",QMessageBox.Yes)
            self.setMacInfo()
        else:
            QMessageBox.information(self,"考勤机器管理","删除机器失败！！！",QMessageBox.Yes)
        self.mainUI.lineEditDeleteMac.setText('')
    def searchMac(self):
        target=self.mainUI.lineEdit_search.text()
        idx=0
        for index,mac in enumerate(self.macInfo):
            if target in str(''.join(mac)):
                idx=idx+1
        #self.macInfo=getMacInfo()       
        self.model=QStandardItemModel(idx,1)#存储任意结构数据
        #self.model.clear()
        self.model.setHorizontalHeaderLabels(['物理地址'])
        #水平方向标签拓展剩下的窗口部分，填满表格
        #self.mainUI.tableView.horizontalHeader().setStretchLastSection(True)
        #水平方向，表格大小拓展到适当的尺寸   
        #self.mainUI.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        idx=0
        for index,mac in enumerate(self.macInfo):
            if target in str(''.join(mac)):
                item=QStandardItem(''.join(mac))
                self.model.setItem(idx,0,item)
                idx=idx+1
        self.mainUI.tableView.setModel(self.model)
          

if __name__ == "__main__":
    app = QApplication( sys.argv )
    testUI = Proc_MoreSetting_Widget()
    testUI.show()
    sys.exit( app.exec_() )
