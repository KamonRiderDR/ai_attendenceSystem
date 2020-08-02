# -*- coding: utf-8 -*-

# Proc_MoreSetting implementation generated from reading ui file 'proc_moresetting_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyUiWidgets.uni_showdateinfo_widget import Uni_ShowDateInfo_Widget

class Proc_MoreSetting_Ui(object):
    def setupUi(self, Proc_MoreSetting):
        Proc_MoreSetting.setObjectName("Proc_MoreSetting")
        Proc_MoreSetting.resize(1075, 715)
        Proc_MoreSetting.setStyleSheet("""QWidget#Proc_MoreSetting{
                                    alternate-background-color: rgba(240, 240, 240, 240);
                                    border-bottom-right-radius: 10px;
                                    border-bottom-left-radius: 10px;}""")

        '''init main layout'''
        self.gridLayout_5 = QtWidgets.QGridLayout(Proc_MoreSetting)
        self.gridLayout_5.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_5.setObjectName("gridLayout_5")

        '''layout to set machine setting part'''
        self.machine_setting_widget = QtWidgets.QWidget(Proc_MoreSetting)
        #self.machine_setting_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.machine_setting_widget.setObjectName("machine_setting_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.machine_setting_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.workingmachine_setting_mainlayout = QtWidgets.QVBoxLayout()
        self.workingmachine_setting_mainlayout.setObjectName("workingmachine_setting_mainlayout")

        #btn to search machine by mac addr
        '''new search area'''
        self.horizontalLayout_inside = QtWidgets.QHBoxLayout()
        self.horizontalLayout_inside.setObjectName("horizontalLayout_insode")
        self.lineEdit_search = QtWidgets.QLineEdit()
        with open("Qss\line_edit_style.qss") as LineEditStyle:
                self.lineEdit_search.setStyleSheet(LineEditStyle.read())
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_inside.addWidget(self.lineEdit_search)
        self.push_button_search = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.push_button_search.setFont(font)
        with open("Qss\push_button_style.qss") as PushButtonStyle: 
                self.push_button_search.setStyleSheet(PushButtonStyle.read())
        self.push_button_search.setObjectName("push_button_search")
        self.horizontalLayout_inside.addWidget(self.push_button_search)
        self.workingmachine_setting_mainlayout.addLayout(self.horizontalLayout_inside)

        '''add and delete machine lineedits and btns'''
        # add setting part
        self.workingmachine_add_layout = QtWidgets.QHBoxLayout()
        self.workingmachine_add_layout.setObjectName("workingmachine_add_layout")

        self.lineEditAddMac = QtWidgets.QLineEdit(self.machine_setting_widget)
        self.lineEditAddMac.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lineEditAddMac.setObjectName("lineEditAddMac")
        self.workingmachine_add_layout.addWidget(self.lineEditAddMac)

        self.pushButtonAdd = QtWidgets.QPushButton(self.machine_setting_widget)
        self.pushButtonAdd.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(10)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.workingmachine_add_layout.addWidget(self.pushButtonAdd)
        self.workingmachine_setting_mainlayout.addLayout(self.workingmachine_add_layout)

        # delete setting part
        self.workingmachine_delete_layout = QtWidgets.QHBoxLayout()
        self.workingmachine_delete_layout.setObjectName("workingmachine_delete_layout")

        self.lineEditDeleteMac = QtWidgets.QLineEdit(self.machine_setting_widget)
        self.lineEditDeleteMac.setMaximumSize(QtCore.QSize(16777215, 34))
        self.lineEditDeleteMac.setObjectName("lineEditDeleteMac")
        self.workingmachine_delete_layout.addWidget(self.lineEditDeleteMac)

        self.pushButtonDelete = QtWidgets.QPushButton(self.machine_setting_widget)
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(10)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.workingmachine_delete_layout.addWidget(self.pushButtonDelete)
        self.workingmachine_setting_mainlayout.addLayout(self.workingmachine_delete_layout)

        self.gridLayout.addLayout(self.workingmachine_setting_mainlayout, 0, 1, 1, 1)
        
        '''table view to show machines'''
        self.tableView = QtWidgets.QTableView(self.machine_setting_widget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.machine_setting_widget, 0, 0, 1, 1)

        '''outter widget to show white margins'''
        self.workingIssue_setting_widget = QtWidgets.QWidget(Proc_MoreSetting)
        #self.workingIssue_setting_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.workingIssue_setting_widget.setObjectName("workingIssue_setting_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.workingIssue_setting_widget)
        self.gridLayout_3.setObjectName("gridLayout_3")

        '''layout to set working days and time'''
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.workingdays_setting_mainlayout = QtWidgets.QVBoxLayout()
        self.workingdays_setting_mainlayout.setObjectName("workingdays_setting_mainlayout")

        # label to show A working-days setting tip
        self.workingday_tip_label = QtWidgets.QLabel(self.workingIssue_setting_widget)
        self.workingday_tip_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.workingday_tip_label.setFont(font)
        self.workingday_tip_label.setObjectName("workingday_tip_label")
        self.workingdays_setting_mainlayout.addWidget(self.workingday_tip_label)

        # calendar widget to show working days
        self.calendarWidget = QtWidgets.QCalendarWidget(self.workingIssue_setting_widget)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setObjectName("calendarWidget")

        # set calednar basic style
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(13)
        self.calendarWidget.setFont(font)
        #self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.workingdays_setting_mainlayout.addWidget(self.calendarWidget)


        '''layout of setting btns'''
        self.workingday_btn_layout = QtWidgets.QHBoxLayout()
        self.workingday_btn_layout.setObjectName("workingday_btn_layout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.workingday_btn_layout.addItem(spacerItem)
        # @pushButtonSet1: btn to set a day to working day
        self.pushButtonSet1 = QtWidgets.QPushButton(self.workingIssue_setting_widget)
        self.pushButtonSet1.setObjectName("pushButtonSet1")
        self.workingday_btn_layout.addWidget(self.pushButtonSet1)
        # @pushButtonCancel1: btn to set a day to 'day to rest'
        self.pushButtonCancel1 = QtWidgets.QPushButton(self.workingIssue_setting_widget)
        self.pushButtonCancel1.setObjectName("pushButtonCancel1")
        self.workingday_btn_layout.addWidget(self.pushButtonCancel1)
        self.workingdays_setting_mainlayout.addLayout(self.workingday_btn_layout)
        self.gridLayout_2.addLayout(self.workingdays_setting_mainlayout, 0, 0, 1, 1)

        '''layout to set valid time'''
        self.workingtime_setting_mainlayout = QtWidgets.QVBoxLayout()
        self.workingtime_setting_mainlayout.setObjectName("workingtime_setting_mainlayout")
        # label to in Proc_MoreSetting
        self.workingtime_tip_label = QtWidgets.QLabel(self.workingIssue_setting_widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.workingtime_tip_label.setFont(font)
        self.workingtime_tip_label.setObjectName("workingtime_tip_label")
        self.workingtime_setting_mainlayout.addWidget(self.workingtime_tip_label)



         # should be replaced by current day widget(item)!!
        self.widget = QtWidgets.QWidget(self.workingIssue_setting_widget)
        self.widget.setObjectName("widget")

        self.subrightlayout=QtWidgets.QVBoxLayout(self.widget)
        self.label_showMonthInfo = QtWidgets.QLabel(self.widget)
        self.label_showMonthInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showMonthInfo.setObjectName("label_showMonthInfo")
        self.subrightlayout.addWidget(self.label_showMonthInfo)
        self.label_showMonthInfo.setAttribute(Qt.WA_TranslucentBackground, True)

        # '''set img'''
        # self.label_showMonthInfo.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # self.label_showMonthInfo.setScaledContents(True)
        # self.label_showMonthInfo.setStyleSheet("border-radius:8px;")
        #print(self.label_showMonthInfo.size())

        # label to show date data
        self.label_DayInfo=Uni_ShowDateInfo_Widget()
        self.label_DayInfo.setAttribute(Qt.WA_TranslucentBackground, True)
        self.subrightlayout.addWidget(self.label_DayInfo)

        self.subrightlayout.setStretch(0,1)
        self.subrightlayout.setStretch(1,1)

        pix=QPixmap()
        img=QImage("months_imgs\Jul.PNG")
        self.label_showMonthInfo.setPixmap(pix.fromImage(img))




        self.workingtime_setting_mainlayout.addWidget(self.widget)

        '''layout to set valid start time'''
        self.start_time_edit_layout = QtWidgets.QHBoxLayout()
        self.start_time_edit_layout.setObjectName("start_time_edit_layout")

        self.labelStartTime = QtWidgets.QLabel(self.workingIssue_setting_widget)
        self.labelStartTime.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelStartTime.setFont(font)
        self.labelStartTime.setObjectName("labelStartTime")
        self.start_time_edit_layout.addWidget(self.labelStartTime)

        self.timeEdit = QtWidgets.QTimeEdit(self.workingIssue_setting_widget)
        self.timeEdit.setObjectName("timeEdit")
        self.start_time_edit_layout.addWidget(self.timeEdit)
        self.workingtime_setting_mainlayout.addLayout(self.start_time_edit_layout)

        '''layout to set valid deadline'''
        self.end_time_edit_layout = QtWidgets.QHBoxLayout()
        self.end_time_edit_layout.setObjectName("end_time_edit_layout")

        self.label = QtWidgets.QLabel(self.workingIssue_setting_widget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.end_time_edit_layout.addWidget(self.label)

        self.timeEdit_2 = QtWidgets.QTimeEdit(self.workingIssue_setting_widget)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.end_time_edit_layout.addWidget(self.timeEdit_2)
        self.workingtime_setting_mainlayout.addLayout(self.end_time_edit_layout)

        # layout to set 'valid time' setting btns
        self.workingtime_btn_layout = QtWidgets.QHBoxLayout()
        self.workingtime_btn_layout.setObjectName("workingtime_btn_layout")
        self.pushButtonSave2 = QtWidgets.QPushButton(self.workingIssue_setting_widget)
        self.pushButtonSave2.setObjectName("pushButtonSave2")
        self.workingtime_btn_layout.addWidget(self.pushButtonSave2)
        self.pushButtonReturn2 = QtWidgets.QPushButton(self.workingIssue_setting_widget)
        self.pushButtonReturn2.setObjectName("pushButtonReturn2")
        self.workingtime_btn_layout.addWidget(self.pushButtonReturn2)
        self.workingtime_setting_mainlayout.addLayout(self.workingtime_btn_layout)

        '''import national working days'''
        self.national_workingday_btn_layout = QtWidgets.QVBoxLayout()
        self.national_workingday_btn_layout.setObjectName("national_workingday_btn_layout")
        self.pushButtonImport = QtWidgets.QPushButton(self.workingIssue_setting_widget)
        self.pushButtonImport.setObjectName("pushButtonImport")

        '''layout setting (don't change it)'''
        self.national_workingday_btn_layout.addWidget(self.pushButtonImport)
        self.workingtime_setting_mainlayout.addLayout(self.national_workingday_btn_layout)
        self.workingtime_setting_mainlayout.setStretch(0, 1)
        self.workingtime_setting_mainlayout.setStretch(1, 8)
        self.workingtime_setting_mainlayout.setStretch(2, 3)
        self.workingtime_setting_mainlayout.setStretch(3, 3)
        self.workingtime_setting_mainlayout.setStretch(4, 3)
        self.workingtime_setting_mainlayout.setStretch(5, 3)
        # self.workingdays_setting_mainlayout.setStretch(0,2)
        # self.workingdays_setting_mainlayout.setStretch(1,1)
        self.gridLayout_2.setColumnStretch(0,5)
        self.gridLayout_2.setColumnStretch(1,2)
        self.gridLayout_2.addLayout(self.workingtime_setting_mainlayout, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.workingIssue_setting_widget, 1, 0, 1, 1)
        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 3)
        self.gridLayout_5.setVerticalSpacing(18)

        '''set btn font'''
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButtonAdd.setFont(font)
        self.pushButtonCancel1.setFont(font)
        self.pushButtonDelete.setFont(font)
        self.pushButtonImport.setFont(font)
        self.pushButtonReturn2.setFont(font)
        self.pushButtonSave2.setFont(font)
        self.pushButtonSet1.setFont(font)
        self.push_button_search.setFont(font)

        '''enhance shadow effect''' 
        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.machine_setting_widget.setGraphicsEffect(shadow_effect)
        self.machine_setting_widget.setStyleSheet("""QWidget#machine_setting_widget{
                                                    background-color: rgba(0,191,255,90);
                                                    border-radius: 8px}""")

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.workingIssue_setting_widget.setGraphicsEffect(shadow_effect)
        self.workingIssue_setting_widget.setStyleSheet("""QWidget#workingIssue_setting_widget{
                                                    background-color: rgba(210,105,30,90);
                                                    border-radius: 8px}""")

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget.setGraphicsEffect(shadow_effect)
        self.widget.setStyleSheet("""QWidget#widget{
                                    background-color: rgba(255,255,255,90);
                                    border-radius: 8px}""")

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.calendarWidget.setGraphicsEffect(shadow_effect)

        '''set line edit style'''
        with open("Qss\line_edit_style.qss") as LEditStyle:
            self.lineEditAddMac.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEditDeleteMac.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
        
        regx=QtCore.QRegExp("[A-Z0-9\-]+$")
        validator=QtGui.QRegExpValidator(regx, self.lineEditAddMac)
        self.lineEditAddMac.setPlaceholderText("请输入考勤机器MAC以添加该机器")
        self.lineEditAddMac.setValidator(validator)
        regx=QtCore.QRegExp("[A-Z0-9\-]+$")
        validator=QtGui.QRegExpValidator(regx, self.lineEditDeleteMac)
        self.lineEditDeleteMac.setPlaceholderText("请输入考勤机器MAC以删除该机器")
        self.lineEditDeleteMac.setValidator(validator)
        regx=QtCore.QRegExp("[0-9A-Z\-]+$")
        validator=QtGui.QRegExpValidator(regx, self.lineEdit_search)
        self.lineEdit_search.setPlaceholderText("请输入考勤机器MAC以搜索")
        self.lineEdit_search.setValidator(validator)

        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Ui")
        font.setBold(True)
        font.setPointSize(11)
        self.lineEditAddMac.setFont(font)
        self.lineEditDeleteMac.setFont(font)
        self.lineEdit_search.setFont(font)

        '''set time edit style'''
        with open("Qss/time_edit_style.qss") as TEditStyle:
            self.timeEdit.setStyleSheet(TEditStyle.read())
            TEditStyle.seek(0)
            self.timeEdit_2.setStyleSheet(TEditStyle.read())
            TEditStyle.seek(0)
        
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.timeEdit.setFont(font)
        self.timeEdit_2.setFont(font)

        '''set table view style'''
        with open("Qss/flatwhite_style.qss") as TableStyle:
            self.tableView.setStyleSheet(TableStyle.read())

        '''set calendar style'''
        with open("Qss/flatwhite_style.qss","r", encoding="utf-8") as CalendarStyle:
            self.calendarWidget.setStyleSheet(CalendarStyle.read())

        '''set btn style'''
        with open("Qss/push_button_style.qss") as BtnStyle:
            self.pushButtonAdd.setStyleSheet(BtnStyle.read())
            BtnStyle.seek(0)
            self.pushButtonSave2.setStyleSheet(BtnStyle.read())
            BtnStyle.seek(0)
            self.pushButtonSet1.setStyleSheet(BtnStyle.read())
            BtnStyle.seek(0)
            self.push_button_search.setStyleSheet(BtnStyle.read())
            BtnStyle.seek(0)

        with open("Qss/push_button_style_lightblue.qss") as BtnStyle:
            self.pushButtonImport.setStyleSheet(BtnStyle.read())
            BtnStyle.seek(0)

        with open("Qss/push_button_style_lightred.qss") as BtnStyle:
            self.pushButtonDelete.setStyleSheet(BtnStyle.read())
            BtnStyle.seek(0)
            self.pushButtonReturn2.setStyleSheet(BtnStyle.read())
            BtnStyle.seek(0)
            self.pushButtonCancel1.setStyleSheet(BtnStyle.read())

        '''connection by DR'''
        #------------信号-------------#
        #self.listWidget.clicked.connect( Proc_MoreSetting.stackedWidgetChange )
        self.pushButtonSet1.clicked.connect( Proc_MoreSetting.setWorkingDay )
        self.pushButtonCancel1.clicked.connect( Proc_MoreSetting.cancelSetWorkingDay )

        self.pushButtonSave2.clicked.connect( Proc_MoreSetting.setWorkingTime )
        self.pushButtonReturn2.clicked.connect( Proc_MoreSetting.cancelSetWorkingTime )

        self.pushButtonImport.clicked.connect( Proc_MoreSetting.workingDayImport )
        #self.pushButtonCancel3.clicked.connect( Proc_MoreSetting.cancelFunc3 )

        '''
        剩余的有空回头补
        '''
        #-------------slot end-------------#

        '''connection by ADK'''
        '''set connection'''
        self.pushButtonAdd.clicked.connect(Proc_MoreSetting.addMac)
        self.pushButtonDelete.clicked.connect(Proc_MoreSetting.deleteMac)
        self.push_button_search.clicked.connect(Proc_MoreSetting.searchMac)
        self.retranslateUi(Proc_MoreSetting)
        QtCore.QMetaObject.connectSlotsByName(Proc_MoreSetting)

    def retranslateUi(self, Proc_MoreSetting):
        _translate = QtCore.QCoreApplication.translate
        Proc_MoreSetting.setWindowTitle(_translate("Proc_MoreSetting", "Proc_MoreSetting"))
        self.push_button_search.setText(_translate("Proc_MoreSetting", "搜索"))
        self.pushButtonAdd.setText(_translate("Proc_MoreSetting", "添加考勤机器"))
        self.pushButtonDelete.setText(_translate("Proc_MoreSetting", "删除考勤机器"))
        self.workingday_tip_label.setText(_translate("Proc_MoreSetting", "工作日设置管理"))
        self.pushButtonSet1.setText(_translate("Proc_MoreSetting", "设置选中日为工作日"))
        self.pushButtonCancel1.setText(_translate("Proc_MoreSetting", "设置选中日为休息日"))
        self.workingtime_tip_label.setText(_translate("Proc_MoreSetting", "考勤时间设置管理"))
        self.labelStartTime.setText(_translate("Proc_MoreSetting", "开始时间："))
        self.label.setText(_translate("Proc_MoreSetting", "结束时间："))
        self.pushButtonSave2.setText(_translate("Proc_MoreSetting", "保存"))
        self.pushButtonReturn2.setText(_translate("Proc_MoreSetting", "返回"))
        self.pushButtonImport.setText(_translate("Proc_MoreSetting", "导入国家工作日"))
