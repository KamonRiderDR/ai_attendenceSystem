# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proc_signin_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Proc_SignIn(object):
    def setupUi(self, Proc_SignIn):
        Proc_SignIn.setObjectName("Proc_SignIn")
        Proc_SignIn.resize(498, 665)
        self.layout_main = QtWidgets.QVBoxLayout(Proc_SignIn)
        self.layout_main.setSpacing(9)
        self.layout_main.setObjectName("layout_main")
        self.widget_top_container = QtWidgets.QWidget(Proc_SignIn)
        self.widget_top_container.setObjectName("widget_top_container")
        self.layout_top = QtWidgets.QGridLayout(self.widget_top_container)
        self.layout_top.setObjectName("layout_top")
        self.label_showTitle = QtWidgets.QLabel(self.widget_top_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_showTitle.setFont(font)
        self.label_showTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showTitle.setObjectName("label_showTitle")
        self.layout_top.addWidget(self.label_showTitle, 0, 0, 1, 1)
        self.layout_main.addWidget(self.widget_top_container)
        self.widget_centre_conatiner = QtWidgets.QWidget(Proc_SignIn)
        self.widget_centre_conatiner.setObjectName("widget_centre_conatiner")
        self.layout_centre = QtWidgets.QVBoxLayout(self.widget_centre_conatiner)
        self.layout_centre.setObjectName("layout_centre")
        self.layout_getAllInfo = QtWidgets.QGridLayout()
        self.layout_getAllInfo.setObjectName("layout_getAllInfo")
        self.label_getPassword_confirm = QtWidgets.QLabel(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_getPassword_confirm.setFont(font)
        self.label_getPassword_confirm.setObjectName("label_getPassword_confirm")
        self.layout_getAllInfo.addWidget(self.label_getPassword_confirm, 3, 0, 1, 1)
        self.label_getId = QtWidgets.QLabel(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_getId.setFont(font)
        self.label_getId.setObjectName("label_getId")
        self.layout_getAllInfo.addWidget(self.label_getId, 1, 0, 1, 1)
        self.label_getPassword = QtWidgets.QLabel(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_getPassword.setFont(font)
        self.label_getPassword.setObjectName("label_getPassword")
        self.layout_getAllInfo.addWidget(self.label_getPassword, 2, 0, 1, 1)
        self.label_getEmail = QtWidgets.QLabel(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_getEmail.setFont(font)
        self.label_getEmail.setObjectName("label_getEmail")
        self.layout_getAllInfo.addWidget(self.label_getEmail, 4, 0, 1, 1)
        self.label_getName = QtWidgets.QLabel(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_getName.setFont(font)
        self.label_getName.setObjectName("label_getName")
        self.layout_getAllInfo.addWidget(self.label_getName, 0, 0, 1, 1)
        self.lineEdit_getName = QtWidgets.QLineEdit(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getName.setFont(font)
        self.lineEdit_getName.setObjectName("lineEdit_getName")
        self.layout_getAllInfo.addWidget(self.lineEdit_getName, 0, 1, 1, 1)
        self.lineEdit_getId = QtWidgets.QLineEdit(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getId.setFont(font)
        self.lineEdit_getId.setObjectName("lineEdit_getId")
        self.layout_getAllInfo.addWidget(self.lineEdit_getId, 1, 1, 1, 1)
        self.lineEdit_getPassword = QtWidgets.QLineEdit(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getPassword.setFont(font)
        self.lineEdit_getPassword.setObjectName("lineEdit_getPassword")
        self.layout_getAllInfo.addWidget(self.lineEdit_getPassword, 2, 1, 1, 1)
        self.lineEdit_getPassword_confirm = QtWidgets.QLineEdit(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getPassword_confirm.setFont(font)
        self.lineEdit_getPassword_confirm.setObjectName("lineEdit_getPassword_confirm")
        self.layout_getAllInfo.addWidget(self.lineEdit_getPassword_confirm, 3, 1, 1, 1)
        self.lineEdit_getEmail = QtWidgets.QLineEdit(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getEmail.setFont(font)
        self.lineEdit_getEmail.setObjectName("lineEdit_getEmail")
        self.layout_getAllInfo.addWidget(self.lineEdit_getEmail, 4, 1, 1, 1)
        self.layout_centre.addLayout(self.layout_getAllInfo)
        self.layout_getConfirmCode = QtWidgets.QHBoxLayout()
        self.layout_getConfirmCode.setObjectName("layout_getConfirmCode")
        self.label_getConfirmCode = QtWidgets.QLabel(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_getConfirmCode.setFont(font)
        self.label_getConfirmCode.setObjectName("label_getConfirmCode")
        self.layout_getConfirmCode.addWidget(self.label_getConfirmCode)
        self.lineEdit_getConfirmCode = QtWidgets.QLineEdit(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getConfirmCode.setFont(font)
        self.lineEdit_getConfirmCode.setObjectName("lineEdit_getConfirmCode")
        self.layout_getConfirmCode.addWidget(self.lineEdit_getConfirmCode)
        self.btn_getConfirmCode = QtWidgets.QPushButton(self.widget_centre_conatiner)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_getConfirmCode.setFont(font)
        self.btn_getConfirmCode.setObjectName("btn_getConfirmCode")
        self.layout_getConfirmCode.addWidget(self.btn_getConfirmCode)
        self.layout_centre.addLayout(self.layout_getConfirmCode)
        self.layout_centre.setStretch(0, 5)
        self.layout_centre.setStretch(1, 1)
        self.layout_main.addWidget(self.widget_centre_conatiner)
        self.widget_bottom_container = QtWidgets.QWidget(Proc_SignIn)
        self.widget_bottom_container.setObjectName("widget_bottom_container")
        self.layout_bottom = QtWidgets.QHBoxLayout(self.widget_bottom_container)
        self.layout_bottom.setObjectName("layout_bottom")
        self.btn_signin = QtWidgets.QPushButton(self.widget_bottom_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_signin.setFont(font)
        self.btn_signin.setObjectName("btn_signin")
        self.layout_bottom.addWidget(self.btn_signin)
        self.layout_main.addWidget(self.widget_bottom_container)


        '''set line edit style'''
        with open("Qss/line_edit_style.qss") as LEditStyle:
            self.lineEdit_getConfirmCode.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_getEmail.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_getId.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_getName.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_getPassword.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_getPassword_confirm.setStyleSheet(LEditStyle.read())
            # LEditStyle.seek(0)

        '''enhance shadow effect'''
        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_centre_conatiner.setGraphicsEffect(shadow_effect)
        self.widget_centre_conatiner.setStyleSheet("""QWidget#widget_centre_conatiner{
                                                    background-color: rgba(255,255,255,90);
                                                    border-radius: 8px}""")

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_bottom_container.setGraphicsEffect(shadow_effect)

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.widget_top_container.setGraphicsEffect(shadow_effect)

        '''set btn style'''
        with open("Qss/push_button_style.qss") as BtnStyle:
            self.btn_signin.setStyleSheet(BtnStyle.read())
        with open("Qss/push_button_style_lightblue.qss") as BtnStyle:
            self.btn_getConfirmCode.setStyleSheet(BtnStyle.read())

        self.retranslateUi(Proc_SignIn)
        QtCore.QMetaObject.connectSlotsByName(Proc_SignIn)

    def retranslateUi(self, Proc_SignIn):
        _translate = QtCore.QCoreApplication.translate
        Proc_SignIn.setWindowTitle(_translate("Proc_SignIn", "Form"))
        self.label_showTitle.setText(_translate("Proc_SignIn", "<html><body></body><img src=\"C:\\Users\\k\\Documents\\GitHub\\09\\UiCodes\\image\\proc_mainimg.png\" \n"
"height=\"170\",width=\"170\"><p>996监督考勤系统</p></html>"))
        self.label_getPassword_confirm.setText(_translate("Proc_SignIn", "确认密码:"))
        self.label_getId.setText(_translate("Proc_SignIn", "账号:"))
        self.label_getPassword.setText(_translate("Proc_SignIn", "密码:"))
        self.label_getEmail.setText(_translate("Proc_SignIn", "邮箱:"))
        self.label_getName.setText(_translate("Proc_SignIn", "姓名:"))
        self.label_getConfirmCode.setText(_translate("Proc_SignIn", "验证码:"))
        self.btn_getConfirmCode.setText(_translate("Proc_SignIn", "获取验证码"))
        self.btn_signin.setText(_translate("Proc_SignIn", "注册"))

if __name__ == "__main__":
    app = QApplication( sys.argv )
    
    TestUi=QWidget()
    #TestUi.setWindowFlags (Qt.FramelessWindowHint)
    TestUi.main_ui=Ui_Proc_SignIn()
    TestUi.main_ui.setupUi(TestUi)
    TestUi.show()

    sys.exit( app.exec_() )