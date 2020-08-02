#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


'''import project's ui(s)'''

from PyUiWidgets.proc_mainpage_widget import Proc_MainPage_Widget
from PyUiFiles.proc_moresetting_widget import Proc_MoreSetting_Widget
from PyUiWidgets.proc_requestsverify_widget import Proc_RequestsVerify_Widget
from PyUiWidgets.proc_staffinfo_widget import Proc_StaffInfo_Widget

class LeftTabWidget_Manager(QWidget):
    def __init__(self):
        super(LeftTabWidget_Manager, self).__init__()
        self.setObjectName('LeftTabWidget')

        self.setWindowIcon(QIcon("image\proc_mainimg.png"))

        self.setWindowTitle('LeftTabWidget')
        with open('Qss\QListWidgetQSS.qss', 'r') as f:   
            self.list_style = f.read()

        self.main_layout = QHBoxLayout(self, spacing=0)     
        self.main_layout.setContentsMargins(0,0,0,0)

        self.left_widget = QListWidget()     
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        self.right_widget = QStackedWidget()
        self.right_widget.setStyleSheet('''
            QStackedWidget{
                background-color: rgb(230,230,230);
                border-bottom-right-radius: 10px;
            }
        ''')
        self.main_layout.addWidget(self.right_widget)

        self._setup_ui()
        
    def initShowWidgets(self):
        '''staff attendance info ui'''
        self.AttendanceInfoUi=Proc_MainPage_Widget()
        self.right_widget.insertWidget(0,self.AttendanceInfoUi)
        self.AttendanceInfoUi.adjustSize()

        '''satff management ui'''
        self.StaffManageUi=Proc_StaffInfo_Widget()
        self.right_widget.insertWidget(1,self.StaffManageUi)
        self.StaffManageUi.adjustSize()

        '''reuqests vefiry ui'''
        self.requestsverifyUi=Proc_RequestsVerify_Widget()
        self.right_widget.insertWidget(2,self.requestsverifyUi)
        self.requestsverifyUi.adjustSize()

        ''''machine management ui'''
        self.SettingManageUi=Proc_MoreSetting_Widget()
        self.right_widget.insertWidget(3,self.SettingManageUi)
        self.SettingManageUi.adjustSize()
    
    def _setup_ui(self):
        self.initLeftTab()
        
        self.initShowWidgets()        

    def initLeftTab(self):
        '''load ui window'''
        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)   

        self.left_widget.setFrameShape(QListWidget.NoFrame)    

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str=["员工考勤情况","员工信息查看","员工请假申诉管理","考勤相关设置"]

        # self.left_widget.setIconSize(QSize(120,120))
        # self.item=QListWidgetItem(self.left_widget)
        # self.item.setIcon(QIcon("headimg.jpg"))
        # self.item.setSizeHint(QSize(0,180))
        # self.item.setTextAlignment(Qt.AlignCenter)

        '''set font'''
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        for i in range(4):
            self.item = QListWidgetItem(list_str[i],self.left_widget)   
            self.item.setSizeHint(QSize(30,50))
            self.item.setFont(font)
            self.item.setTextAlignment(Qt.AlignCenter)
            #self.item.setForeColor(QColor(Qt.white))  

        '''enhance shadow effect'''
        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        #shadow_effect.setBlurRadius(10)
        self.left_widget.setGraphicsEffect(shadow_effect)

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        #shadow_effect.setBlurRadius(10)
        self.right_widget.setGraphicsEffect(shadow_effect)
            

def main():
    ''' '''
    app = QApplication(sys.argv)

    main_wnd = LeftTabWidget_Manager()
    main_wnd.show()

    '''test'''

    app.exec()

if __name__ == '__main__':
    main()