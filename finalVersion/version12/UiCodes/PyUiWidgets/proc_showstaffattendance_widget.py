import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyUiFiles.proc_showstaffattendance_ui import Ui_Proc_ShowStaffAttendanceInfo

class Proc_ShowStaffAttendance_Widget(QWidget, Ui_Proc_ShowStaffAttendanceInfo):
    def __init__(self):
        super(Proc_ShowStaffAttendance_Widget, self).__init__()

        self.mainUi=Ui_Proc_ShowStaffAttendanceInfo()
        self.mainUi.setupUi( self )


    #--------根据ID刷新内容----------#
    def refreshPage(self,info):
        self.mainUi.lineEdit_showStaffName.setText( str(info[0]) )
        self.mainUi.lineEdit_showStaffId.setText( str( info[1] ) )
        self.mainUi.lineEdit_showCheckInNum.setText( str( info[2] ) )
        self.mainUi.lineEdit_showLateNum.setText( str( info[3] ) )
        self.mainUi.lineEdit_showBreakNum.setText( str( info[4] ) )
        self.mainUi.lineEdit_showRank.setText( str( info[5] ) )

    def getStaffID( self ):
        return self.mainUi.lineEdit_showStaffId.text()


if __name__ == "__main__":
    app = QApplication( sys.argv )
    testUI = Proc_ShowStaffAttendance_Widget()
    testUI.show()
    sys.exit( app.exec_() )