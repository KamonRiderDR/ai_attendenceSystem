# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAndDeleteMachine.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addAndDeleteMac(object):
    def setupUi(self, addAndDeleteMac):
        addAndDeleteMac.setObjectName("addAndDeleteMac")
        addAndDeleteMac.resize(1100, 750)
        addAndDeleteMac.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(addAndDeleteMac)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(addAndDeleteMac)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(addAndDeleteMac)
        self.tableView.setMinimumSize(QtCore.QSize(410, 500))
        self.tableView.setStyleSheet("#tableView\n"
"{border-style:thin;\n"
"}\n"
"\n"
"QTableView::pane{\n"
"border:1px solid #C0DCF2;\n"
"selection-background-color:#F2F9FF;\n"
"selection-color:rgba(193,193,193,200);\n"
"alternate-background-color:rgba(193,193,193,200);\n"
"gridline-color:rgb(255, 0, 0);\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(230, 230, 230);\n"
"}\n"
"\n"
"QTableView::item:hover{\n"
"color:rgb(255, 255, 255);\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);\n"
"background-color:rgb(230, 230, 230);\n"
"}\n"
"\n"
"QTableView::item{\n"
"padding:5px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section,QTableCornerButton:section{\n"
"padding:3px;\n"
"margin:0px;\n"
"color:rgb(255,255,255);\n"
"border:1px solid rgb(230, 230, 230);\n"
"border-left-width:0px;\n"
"border-right-width:1px;\n"
"border-top-width:0px;\n"
"border-bottom-width:1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);\n"
"    background-color: rgb(193, 193, 193);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEditAddMac = QtWidgets.QLineEdit(addAndDeleteMac)
        self.lineEditAddMac.setObjectName("lineEditAddMac")
        self.horizontalLayout.addWidget(self.lineEditAddMac)
        self.pushButtonAdd = QtWidgets.QPushButton(addAndDeleteMac)
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(16)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setStyleSheet("")
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.lineEditDeleteMac = QtWidgets.QLineEdit(addAndDeleteMac)
        self.lineEditDeleteMac.setObjectName("lineEditDeleteMac")
        self.horizontalLayout_5.addWidget(self.lineEditDeleteMac)
        self.pushButtonDelete = QtWidgets.QPushButton(addAndDeleteMac)
        font = QtGui.QFont()
        font.setFamily("Adobe 楷体 Std R")
        font.setPointSize(16)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setStyleSheet("")
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout_5.addWidget(self.pushButtonDelete)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.retranslateUi(addAndDeleteMac)
        self.pushButtonAdd.clicked.connect(addAndDeleteMac.addMac)
        self.pushButtonDelete.clicked.connect(addAndDeleteMac.deleteMac)
        QtCore.QMetaObject.connectSlotsByName(addAndDeleteMac)

    def retranslateUi(self, addAndDeleteMac):
        _translate = QtCore.QCoreApplication.translate
        addAndDeleteMac.setWindowTitle(_translate("addAndDeleteMac", "Form"))
        self.pushButton.setText(_translate("addAndDeleteMac", "PushButton"))
        self.pushButtonAdd.setText(_translate("addAndDeleteMac", "添加考勤机器"))
        self.pushButtonDelete.setText(_translate("addAndDeleteMac", "删除考勤机器"))