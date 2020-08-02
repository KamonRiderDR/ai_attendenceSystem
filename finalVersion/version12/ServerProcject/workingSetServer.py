#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :workingSetServer.py
@说明    : 服务器端，与数据库直接交互
@时间    :2020/07/27 14:16:28
@作者    :dongrui
@版本    :1.4
'''
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pymysql
import socket
import sys
import time
import json
import datetime
from concurrent.futures import ThreadPoolExecutor
class workingServerClass:
    def __init__(self, *args, **kwargs):
       
        # 打开数据库连接
        self.db = pymysql.connect("localhost","root","admin123","test_db" )
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        self.serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host=socket.gethostname()#获取本地主机名
        self.port=10000
        #绑定端口号
        self.serversocket.bind((self.host,self.port))
        self.serversocket.listen(5)
        self.threadPool = ThreadPoolExecutor(max_workers=args[0], thread_name_prefix="serverThread_")
        for i in range(0,args[0]):
            self.threadPool.submit(self.startServer,i)
        #设置最大连接数
        
        #self.startServer()

    
    def startServer( self,threadID ):
        while True:
            #print('服务器启动，监听客户端链接')
            print("服务器线程_%s 启动，监听客户端链接"%(threadID))
            clientsocket,addr=self.serversocket.accept()

            while True:
                try:
                    #print("Get!")
                    #data 第二个接收到的参数，
                    test=clientsocket.recv(1024).decode()
                    data=clientsocket.recv(102400).decode()

                    data=json.loads(data)#转为json

                    flg = data[0]
                except Exception:
                    print('断开的客户端：',addr)
                    break
                reply = self.DataProcess(flg,data)#  函数的返回值

                reply = json.dumps( reply )
                if not reply:
                    clientsocket.send(str("").encode())#这个if可能不需要
                    break
                clientsocket.send(reply.encode('utf-8'))
                print("send!")
            clientsocket.close()


    #-------------根据flg确定不同的函数-----------#
    def DataProcess( self,funcID,data ):
        if funcID == "workingTimeSave":
            # 存考勤时间
            sign = self.saveWorkingTime( data )
            return sign
        elif funcID == "workingDaySave":
            # 存工作日休息日
            sign = self.saveWorkingDay( data )
            return sign
        elif funcID == "getWorkingDay":
            # 返回考勤信息
            return self.getWorkingDay()
        elif funcID == "getStaffWorkingTime":
            # 返回员工的考勤数据
            return self.getStaffWorkingTime(data)


    #-----------考勤时间的保存------------#
    def saveWorkingTime( self,time ):
        #time = time.split( '-' )
        #  reset
        sql0 = "DELETE FROM workingtime"
        self.cursor.execute( sql0 )
        self.db.commit()

        start = time[1]
        end = time[2]
        sql = "INSERT INTO workingtime VALUES ('%s','%s')"%(time[1],time[2])
        try:            
            self.cursor.execute(sql) # 执行sql语句
            self.db.commit()         # 提交到数据库执行
            print("插入成功")
        except:
            print("插入失败")
            self.db.rollback()       # 如果发生错误则回滚
        try:
            self.modifyStaffWorkingTime( time )
            return True
        except:
            return False

    #------------国家工作日的保存------------#
    def saveWorkingDay( self,dateList ):
        #  先刷新，有的数据清空
        sql = "DELETE FROM workingday"
        self.cursor.execute( sql )
        self.db.commit()
        #  保存新的日期
        today=datetime.date.today()
        todayStr = today.strftime('%Y-%m-%d')
        print(todayStr)
        try:
            #  今日之后的时间设置，之前的时间保存
            for i,item in enumerate( dateList ):
                if i >= 1:
                    date = item[0]
                    # str -> date 
                    dateTime = datetime.datetime.strptime(item[0],'%Y-%m-%d')
                    tag = item[1]
                    sql = "UPDATE workingday SET isWorkingDay=%s WHERE date='%s'"%(tag,date)

                    try:
                        self.cursor.execute( sql )
                        self.db.commit()
                        print("插入成功")
                        #  修改今日以后工作日的设定
                        self.modifyStaffWorkingDay( item,today )
                    except:
                        print("插入失败")
                        self.db.rollback() 
            return True
        except:
            return False

    #-------------获得考勤时间------------#
    def getWorkingDay(self):
        Res = []
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
            Res.append( res )

            print( res )
            print( type(res) )

        #  send data
        print(Res)
        return Res
    
       

    #-------------date -> [year/month/day]--------#
    def getDate(self,Date):
        date = Date.split('-')
        return date


    #--------修改员工的工作日表--------#
    def modifyStaffWorkingDay(self,item,today):
        #  get information
        Date = item[0]
        print(Date)
        isWorkingDay = item[1]
        date = self.getDate(Date)
        todayStr = today.strftime('%Y-%m-%d')
        print(todayStr)
        #  今日之后的时间设置，之前的时间保存
        if Date >= todayStr:
        #  search table and refresh
            sql = "SELECT * FROM signin WHERE signdate = '%s'"%(Date)
            sql2 ="UPDATE signin SET ifworkday='%s' WHERE signdate='%s'"%(isWorkingDay,Date)
            self.cursor.execute( sql2 )
            self.db.commit()

            self.cursor.execute( sql )
            self.db.commit()
            res = self.cursor.fetchall()
            print(res)
            # for it in res:
            print( "修改成功！" )

    #------------修改员工工作时间----------#
    def modifyStaffWorkingTime( self,time ):
        startTime = time[1]
        endTime = time[2]
        today=datetime.date.today()
        todayStr = today.strftime('%Y-%m-%d')
        print(todayStr)
        #  今日之后的时间设置，之前的时间保存
        sql = "UPDATE signin SET starttime = '%s',endtime = '%s' WHERE signdate >'%s'"%(startTime,endTime,todayStr)
        self.cursor.execute( sql )
        self.db.commit()

        print("工作时间修改成功！")

    #-------------获得员工工作时间-----------#
    def getStaffWorkingTime( self,data ):
        #  data -> id
        id = data[1]
        Res = []
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
            Res.append( res )
        print(Res)
        return Res

    def getStartDate( self,dateList ):
        # 上个月的日期
        year = dateList[0]
        month = dateList[1]
        day = dateList[2]

        if month == 1:
            return str( str(year-1) + '-' + str(12) + '-' + str(1) )
        else:
            return str( str(year) + '-' + str(month) + '-' + str(1) )

if __name__=="__main__":
    app=workingServerClass((2))
    
