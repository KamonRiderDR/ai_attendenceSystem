import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyUiFiles.proc_mainwin_staff_ui.showmanagerinfo_ui import Ui_ShowManagerInfo
from PyUiWidgets.showsearchedstaffdata_win import ShowSearchedStaffData_Win

class ShowManager_Widget(QWidget, Ui_ShowManagerInfo):
    def __init__(self):
        super(ShowManager_Widget, self).__init__()

        self.mainUi=Ui_ShowManagerInfo()
        self.mainUi.setupUi( self )

        '''sub win'''
        self.searchedstaffwin=ShowSearchedStaffData_Win()
    
    #-------------更新-------------#
    def slot_showSearchedStaffData(self):
        id = self.mainUi.lineEdit_getStaffId.text()
        print(id)
        self.searchedstaffwin.getID( id )
        self.searchedstaffwin.show()
        

if __name__ == "__main__":
    app = QApplication( sys.argv )
    testUI = ShowManager_Widget()
    testUI.show()
    sys.exit( app.exec_() )