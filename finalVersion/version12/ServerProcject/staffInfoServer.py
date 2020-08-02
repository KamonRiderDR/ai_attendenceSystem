import pymysql
import socket
import sys
import time
import json
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
class StaffInfoServer:
    def __init__(self, *args, **kwargs):
        self.db = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='admin123',
                       database='test_db',
                       charset='utf8')
        self.cursor = self.db.cursor()
        self.staffNum = self.staffNumber()
        self.now = QDate.currentDate()
    
    #公司员工数
    def staffNumber(self):
        try:
            self.cursor.execute("select * from staff;" )
            return  len(self.cursor.fetchall())
        except:
            print ("Error")
            return


    #今日签到数
    def todayCheck(self):
        num = 0
        try:
            self.cursor.execute("select * from signin;" )
            now = QDate.currentDate()
            for i in self.cursor.fetchall():
                if now == i[1]:
                    num += 1
            return num 
        except:
            print ("Error")
            return
        
    #待处理请求
    def quest(self):
        num = 0
        try:
            self.cursor.execute("select * from absence;" )
            for i in self.cursor.fetchall():
                if i[5] == '1' :
                    num += 1
            print(num)
            return num
        except:
            print("Error")

    #人员变动
    def staffChange(self):
        try:
            if self.now != QDate.currentDate():
                
                return self.staffNum-self.staffNumber()
            else:
                return 0
        except:
            print("Error")
    

            

if __name__ == '__main__':
    w = workingServerClass()
    #print(w.staffNumber())
    #print(w.todayCheck())
    print(w.quest())


    
        

    
