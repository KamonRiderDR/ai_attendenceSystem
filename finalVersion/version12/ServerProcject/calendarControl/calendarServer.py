# -*- encoding: utf-8 -*-

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

class CalendarServer:
    def __init__(self, qcalendarWidget,workerId = '213180001'):
        self.db = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='admin123',
                       database='test_db',
                       charset='utf8')
        self.calendarWidget = QCalendarWidget()
        self.calendarWidget = qcalendarWidget
        self.id = workerId
        self.checkDate = []
        self.monthHoliday = []
        self.holidayFormat = QTextCharFormat()
        self.checkFormat = QTextCharFormat()
        self.originFormat = QTextCharFormat()
        self.originFormat.setBackground(QColor(255, 233, 237))
        self.cursor = self.db.cursor()
        self.currentMonth = self.calendarWidget.monthShown()
        self.calendarPaint()
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat(QCalendarWidget.NoVerticalHeader))


    def calendarPaint(self):

        self.cursor.execute("select * from workingday;" )
        self.date = self.cursor.fetchall()
        #print(self.date)
        
        self.holidayFormat.setBackground(QColor(216, 249, 216))
        for i,j in self.date:
            #print(j == "1",i.month == self.currentMonth)
            if j == "1":
                print(i,j)
                #self.calendarWidget.paintCell(painter1,QRect(0,0,50,50),i)
                self.monthHoliday.append(i)
                print(i)
                self.calendarWidget.setDateTextFormat(i,self.holidayFormat)
            if j == '0':
                self.calendarWidget.setDateTextFormat(i, self.originFormat)
        print("\n\n")    

        #print(self.monthHoliday)
        self.cursor.execute("select * from signin;" )
        self.signin = self.cursor.fetchall()
        self.checkFormat.setForeground(QColor(190, 48, 77))
        for i in self.signin:
            if i[0] == self.id :
                self.checkDate.append(i[1])
                #print(self.calendarWidget.dateTextFormat(i[1]))
                if self.calendarWidget.dateTextFormat(i[1]) == self.holidayFormat:
                    self.checkFormat.setBackground(QColor(216, 249, 216))
                    self.calendarWidget.setDateTextFormat(i[1],self.checkFormat)
                    #self.calendarWidget.paintCell(painter1,QRect(0,0,50,50),i[1])
                else:
                    #self.calendarWidget.paintCell(painter1,QRect(0,0,50,50),i[1])
                    self.calendarWidget.setDateTextFormat(i[1],self.checkFormat)
                    self.calendarWidget.setDateTextFormat(i[1], self.originFormat)
    

if __name__=="__main__":
    app=CalendarServer()