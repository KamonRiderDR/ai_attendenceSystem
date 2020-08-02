# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyUiFiles.proc_requestsverify_ui import Ui_Requests_Verify

class Proc_RequestsVerify_Widget(QWidget, Ui_Requests_Verify):
    def __init__(self):
        super(Proc_RequestsVerify_Widget, self).__init__()

        self.mainUi=Ui_Requests_Verify()
        self.mainUi.setupUi( self )

    def complainpass(self):
        QMessageBox.information(self,"提示","申诉已通过！" ) 
        return
        
    def complaindeny(self):
        QMessageBox.information(self,"提示","申诉已驳回！" ) 
        return

    def breakpass(self):
        QMessageBox.information(self,"提示","请假申请已通过！" ) 
        return

    def breakdeny(self,widget_breakday_container):
        QMessageBox.information(self,"提示","请假申请已驳回！" ) 
        return


if __name__ == "__main__":
    app = QApplication( sys.argv )
    testUI = Proc_RequestsVerify_Widget()
    testUI.show()
    sys.exit( app.exec_() )