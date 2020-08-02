# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workingSet.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorkingSet(object):
    def setupUi(self, WorkingSet):
        WorkingSet.setObjectName("WorkingSet")
        WorkingSet.setEnabled(True)
        WorkingSet.resize(1107, 806)
        WorkingSet.setMinimumSize(QtCore.QSize(0, 0))
        WorkingSet.setMaximumSize(QtCore.QSize(99999, 99999))
        
        '''init main layout'''
        self.gridLayout = QtWidgets.QGridLayout(WorkingSet)
        self.gridLayout.setObjectName("gridLayout")

        '''init main-show label'''
        self.workingtime_tip_label = QtWidgets.QLabel(WorkingSet)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.workingtime_tip_label.setFont(font)
        self.workingtime_tip_label.setObjectName("workingtime_tip_label")
        self.gridLayout.addWidget(self.workingtime_tip_label, 0, 2, 1, 1)

        '''init btns to save and undo calendar-dates settings'''
        self.workingday_btn_layout = QtWidgets.QHBoxLayout()
        self.workingday_btn_layout.setObjectName("workingday_btn_layout")
        self.pushButtonSet1 = QtWidgets.QPushButton(WorkingSet)
        self.pushButtonSet1.setObjectName("pushButtonSet1")
        self.workingday_btn_layout.addWidget(self.pushButtonSet1)
        self.pushButtonCancel1 = QtWidgets.QPushButton(WorkingSet)
        self.pushButtonCancel1.setObjectName("pushButtonCancel1")
        self.workingday_btn_layout.addWidget(self.pushButtonCancel1)
        self.gridLayout.addLayout(self.workingday_btn_layout, 5, 0, 1, 1)

        '''init btn to import national working days settings'''
        self.national_workingday_btn_layout = QtWidgets.QVBoxLayout()
        self.national_workingday_btn_layout.setObjectName("national_workingday_btn_layout")
        self.pushButtonImport = QtWidgets.QPushButton(WorkingSet)
        self.pushButtonImport.setObjectName("pushButtonImport")
        self.national_workingday_btn_layout.addWidget(self.pushButtonImport)
        self.gridLayout.addLayout(self.national_workingday_btn_layout, 5, 2, 1, 1)
        
        '''init working-time (tip) label'''
        self.workingday_tip_label = QtWidgets.QLabel(WorkingSet)
        self.workingday_tip_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.workingday_tip_label.setFont(font)
        self.workingday_tip_label.setObjectName("workingday_tip_label")
        self.gridLayout.addWidget(self.workingday_tip_label, 0, 0, 1, 1)
        
        '''init time setting parts'''
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # delay-decisioned widget 
        self.widget = QtWidgets.QWidget(WorkingSet)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        # start time setting parts
        self.start_time_edit_layout = QtWidgets.QHBoxLayout()
        self.start_time_edit_layout.setObjectName("start_time_edit_layout")
        self.labelStartTime = QtWidgets.QLabel(WorkingSet)
        self.labelStartTime.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelStartTime.setFont(font)
        self.labelStartTime.setObjectName("labelStartTime")
        self.start_time_edit_layout.addWidget(self.labelStartTime)
        self.timeEdit = QtWidgets.QTimeEdit(WorkingSet)
        self.timeEdit.setObjectName("timeEdit")
        self.start_time_edit_layout.addWidget(self.timeEdit)
        self.verticalLayout.addLayout(self.start_time_edit_layout)
        # deadline setting parts
        self.end_time_edit_layout = QtWidgets.QHBoxLayout()
        self.end_time_edit_layout.setObjectName("end_time_edit_layout")
        self.label = QtWidgets.QLabel(WorkingSet)
        self.label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.end_time_edit_layout.addWidget(self.label)
        self.timeEdit_2 = QtWidgets.QTimeEdit(WorkingSet)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.end_time_edit_layout.addWidget(self.timeEdit_2)
        self.verticalLayout.addLayout(self.end_time_edit_layout)

        '''init time setting activate btn'''
        self.workingtime_btn_layout = QtWidgets.QHBoxLayout()
        self.workingtime_btn_layout.setObjectName("workingtime_btn_layout")
        self.pushButtonSave2 = QtWidgets.QPushButton(WorkingSet)
        self.pushButtonSave2.setObjectName("pushButtonSave2")
        self.workingtime_btn_layout.addWidget(self.pushButtonSave2)
        self.pushButtonReturn2 = QtWidgets.QPushButton(WorkingSet)
        self.pushButtonReturn2.setObjectName("pushButtonReturn2")
        self.workingtime_btn_layout.addWidget(self.pushButtonReturn2)
        self.verticalLayout.addLayout(self.workingtime_btn_layout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)

        '''init calendar widget'''
        self.calendarWidget = QtWidgets.QCalendarWidget(WorkingSet)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 1, 0, 1, 1)

        self.retranslateUi(WorkingSet)
        QtCore.QMetaObject.connectSlotsByName(WorkingSet)

    def retranslateUi(self, WorkingSet):
        _translate = QtCore.QCoreApplication.translate
        WorkingSet.setWindowTitle(_translate("WorkingSet", "Form"))
        self.workingtime_tip_label.setText(_translate("WorkingSet", "考勤时间设置管理"))
        self.pushButtonSet1.setText(_translate("WorkingSet", "设置选中日为工作日"))
        self.pushButtonCancel1.setText(_translate("WorkingSet", "设置选中日为休息日"))
        self.pushButtonImport.setText(_translate("WorkingSet", "导入国家工作日"))
        self.workingday_tip_label.setText(_translate("WorkingSet", "工作日设置管理"))
        self.labelStartTime.setText(_translate("WorkingSet", "开始时间："))
        self.label.setText(_translate("WorkingSet", "结束时间："))
        self.pushButtonSave2.setText(_translate("WorkingSet", "保存"))
        self.pushButtonReturn2.setText(_translate("WorkingSet", "返回"))
import login_rc
