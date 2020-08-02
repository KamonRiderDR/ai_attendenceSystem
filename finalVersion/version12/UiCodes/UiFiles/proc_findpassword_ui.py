# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proc_findpassword_ui.ui'
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
from PyQt5.QtChart import *


class Ui_Proc_FindPassword(object):
    def setupUi(self, Proc_FindPassword):
        Proc_FindPassword.setObjectName("Proc_FindPassword")
        Proc_FindPassword.resize(441, 575)
        self.layout_main = QtWidgets.QVBoxLayout(Proc_FindPassword)
        self.layout_main.setObjectName("layout_main")
        self.widget_top_container = QtWidgets.QWidget(Proc_FindPassword)
        self.widget_top_container.setObjectName("widget_top_container")
        self.layout_widgetTopContainer = QtWidgets.QHBoxLayout(self.widget_top_container)
        self.layout_widgetTopContainer.setObjectName("layout_widgetTopContainer")
        self.label_showTitle = QtWidgets.QLabel(self.widget_top_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_showTitle.setFont(font)
        self.label_showTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showTitle.setObjectName("label_showTitle")
        self.layout_widgetTopContainer.addWidget(self.label_showTitle)
        self.layout_main.addWidget(self.widget_top_container)
        self.widget_centre_container = QtWidgets.QWidget(Proc_FindPassword)
        self.widget_centre_container.setObjectName("widget_centre_container")
        self.layout_widgetCentreContainer = QtWidgets.QVBoxLayout(self.widget_centre_container)
        self.layout_widgetCentreContainer.setObjectName("layout_widgetCentreContainer")
        self.layout_getInfo = QtWidgets.QGridLayout()
        self.layout_getInfo.setObjectName("layout_getInfo")
        self.label_getEmail = QtWidgets.QLabel(self.widget_centre_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_getEmail.setFont(font)
        self.label_getEmail.setObjectName("label_getEmail")
        self.layout_getInfo.addWidget(self.label_getEmail, 0, 0, 1, 1)
        self.label_getPassword_confirm = QtWidgets.QLabel(self.widget_centre_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_getPassword_confirm.setFont(font)
        self.label_getPassword_confirm.setObjectName("label_getPassword_confirm")
        self.layout_getInfo.addWidget(self.label_getPassword_confirm, 2, 0, 1, 1)
        self.label_getPassword = QtWidgets.QLabel(self.widget_centre_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_getPassword.setFont(font)
        self.label_getPassword.setObjectName("label_getPassword")
        self.layout_getInfo.addWidget(self.label_getPassword, 1, 0, 1, 1)
        self.lineEdit_getEmail = QtWidgets.QLineEdit(self.widget_centre_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getEmail.setFont(font)
        self.lineEdit_getEmail.setObjectName("lineEdit_getEmail")
        self.layout_getInfo.addWidget(self.lineEdit_getEmail, 0, 1, 1, 1)
        self.lineEdit_getPassword = QtWidgets.QLineEdit(self.widget_centre_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getPassword.setFont(font)
        self.lineEdit_getPassword.setObjectName("lineEdit_getPassword")
        self.layout_getInfo.addWidget(self.lineEdit_getPassword, 1, 1, 1, 1)
        self.lineEdit_getPassword_confirm = QtWidgets.QLineEdit(self.widget_centre_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getPassword_confirm.setFont(font)
        self.lineEdit_getPassword_confirm.setObjectName("lineEdit_getPassword_confirm")
        self.layout_getInfo.addWidget(self.lineEdit_getPassword_confirm, 2, 1, 1, 1)
        self.layout_widgetCentreContainer.addLayout(self.layout_getInfo)
        self.layout_confirmCodeBtn = QtWidgets.QHBoxLayout()
        self.layout_confirmCodeBtn.setObjectName("layout_confirmCodeBtn")
        self.lineEdit_getConfirmCode = QtWidgets.QLineEdit(self.widget_centre_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_getConfirmCode.setFont(font)
        self.lineEdit_getConfirmCode.setObjectName("lineEdit_getConfirmCode")
        self.layout_confirmCodeBtn.addWidget(self.lineEdit_getConfirmCode)
        self.btn_getConfirmCode = QtWidgets.QPushButton(self.widget_centre_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_getConfirmCode.setFont(font)
        self.btn_getConfirmCode.setObjectName("btn_getConfirmCode")
        self.layout_confirmCodeBtn.addWidget(self.btn_getConfirmCode)
        self.layout_widgetCentreContainer.addLayout(self.layout_confirmCodeBtn)
        self.layout_widgetCentreContainer.setStretch(0, 3)
        self.layout_widgetCentreContainer.setStretch(1, 1)
        self.layout_main.addWidget(self.widget_centre_container)
        self.widget_bottom_container = QtWidgets.QWidget(Proc_FindPassword)
        self.widget_bottom_container.setObjectName("widget_bottom_container")
        self.layout_widgetBottomContainer = QtWidgets.QHBoxLayout(self.widget_bottom_container)
        self.layout_widgetBottomContainer.setObjectName("layout_widgetBottomContainer")
        self.btn_findpassword = QtWidgets.QPushButton(self.widget_bottom_container)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_findpassword.setFont(font)
        self.btn_findpassword.setObjectName("btn_findpassword")
        self.layout_widgetBottomContainer.addWidget(self.btn_findpassword)
        self.layout_main.addWidget(self.widget_bottom_container)

        '''set btn style'''
        with open("Qss/push_button_style.qss") as BtnStyle:
            self.btn_findpassword.setStyleSheet(BtnStyle.read())
        with open("Qss/push_button_style_lightblue.qss") as BtnStyle:
            self.btn_getConfirmCode.setStyleSheet(BtnStyle.read())

        '''set line edit style'''
        with open("Qss/line_edit_style.qss") as LEditStyle:
            self.lineEdit_getConfirmCode.setStyleSheet(LEditStyle.read())
            LEditStyle.seek(0)
            self.lineEdit_getEmail.setStyleSheet(LEditStyle.read())
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
        self.widget_centre_container.setGraphicsEffect(shadow_effect)
        self.widget_centre_container.setStyleSheet("""QWidget#widget_centre_container{
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

        self.retranslateUi(Proc_FindPassword)
        QtCore.QMetaObject.connectSlotsByName(Proc_FindPassword)

    def retranslateUi(self, Proc_FindPassword):
        _translate = QtCore.QCoreApplication.translate
        Proc_FindPassword.setWindowTitle(_translate("Proc_FindPassword", "Form"))
        self.label_showTitle.setText(_translate("Proc_FindPassword", "<html><body></body><img src=\"C:\\Users\\k\\Documents\\GitHub\\09\\UiCodes\\image\\proc_mainimg.png\" \n"
"height=\"190\",width=\"190\"><p>996监督考勤系统--找回密码</p></html>"))
        self.label_getEmail.setText(_translate("Proc_FindPassword", "您的邮箱:"))
        self.label_getPassword_confirm.setText(_translate("Proc_FindPassword", "确认新密码:"))
        self.label_getPassword.setText(_translate("Proc_FindPassword", "新密码:"))
        self.btn_getConfirmCode.setText(_translate("Proc_FindPassword", "获取验证码"))
        self.btn_findpassword.setText(_translate("Proc_FindPassword", "找回密码"))


if __name__ == "__main__":
    app = QApplication( sys.argv )
    
    TestUi=QWidget()
    TestUi.main_ui=Ui_Proc_FindPassword()
    TestUi.main_ui.setupUi(TestUi)
    TestUi.show()

    sys.exit( app.exec_() )