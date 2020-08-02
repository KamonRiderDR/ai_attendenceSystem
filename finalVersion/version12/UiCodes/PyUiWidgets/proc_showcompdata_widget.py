import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyUiFiles.proc_showcompdata_ui import Ui_Proc_ShowCompData


class Proc_ShowCompData_Widget(QWidget, Ui_Proc_ShowCompData):
    def __init__(self):
        super(Proc_ShowCompData_Widget, self).__init__()

        self.mainUi=Ui_Proc_ShowCompData()
        self.mainUi.setupUi( self )
        '''
        false data
        '''
        name1 = "许德勤"
        name2 = "赵德生"
        rateSignin = "94%"
        rateBreak = "3%"
        data = []
        data.append( name1 )
        data.append( name2 )
        data.append( rateSignin )
        data.append( rateBreak )

        self.refreshTotalData( data )



    def refreshTotalData(self,info):
        #  self.lineEdit_showAverageBreak.setReadOnly(True)
        # self.lineEdit_showAverageCheck.setReadOnly(True)
        # self.lineEdit_showBottomRank.setReadOnly(True)
        # self.lineEdit_showTopRank.setReadOnly(True)

        self.mainUi.lineEdit_showTopRank.setText( str(info[0]) )
        self.mainUi.lineEdit_showBottomRank.setText( str(info[1]) )
        self.mainUi.lineEdit_showAverageCheck.setText( str(info[2]) )
        self.mainUi.lineEdit_showAverageBreak.setText( str(info[3]) )

if __name__ == "__main__":
    app = QApplication( sys.argv )
    testUI = Proc_ShowCompData_Widget()
    testUI.show()
    sys.exit( app.exec_() )