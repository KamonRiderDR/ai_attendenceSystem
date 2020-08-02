import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyUiFiles.proc_login_ui import Ui_Proc_Login
from PyUiWidgets.proc_findpassword_win import Proc_FindPassword_Win
from PyUiWidgets.proc_signin_win import Proc_SignIn_Win
from ProcMainWin_Manager import ProcMainWin_Manager
from ProcMainWin_Manager import ProcMainWin_ui
from PyUiWidgets.TitleBar import UniversalTitle_Widget

class Proc_Login_Widget(QWidget, Ui_Proc_Login):
    signal_close = pyqtSignal()
    def __init__(self):
        super(Proc_Login_Widget, self).__init__()

        self.main_ui=Ui_Proc_Login()
        self.main_ui.setupUi(self)

        '''sub win'''
        self.findpasswordwidget=Proc_FindPassword_Win()
        self.mainwin=ProcMainWin_Manager()
        self.signinwin=Proc_SignIn_Win()

    def slot_FindPassword(self):
        self.findpasswordwidget.show()

    def slot_LogIn(self):
        self.mainWnd = ProcMainWin_ui()
        with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.mainWnd.setStyleSheet(TitleBarStyleSheet.read())
        self.mainWnd.resize(QSize(1500,870))
        self.mainWnd.setWidget(ProcMainWin_Manager(self.mainWnd)) 
        self.mainWnd.show()

        self.Close()

    def slot_SignIn(self):
        self.signinwin.show()

    def Close(self):
        self.close()
        self.signal_close.emit()



class Proc_Login_Win(UniversalTitle_Widget):
    def __init__(self, *args, **kwargs):
        super(Proc_Login_Win, self).__init__(*args, **kwargs)
        self.background = QWidget()
        self.background.setStyleSheet("background-color:rgb(235,235,235);")
        self.loginwidget=Proc_Login_Widget()

        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.loginwidget)

        self.setWindowFlags (Qt.FramelessWindowHint)
        with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.setStyleSheet(TitleBarStyleSheet.read())
        self.setWidget(self.background)
        self.resize(QSize(450,600))

        self.loginwidget.signal_close.connect(self.slot_close)

    def slot_close(self):
        self.close()
    

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=Proc_Login_Win()
    mainwin.show()
    sys.exit(app.exec_())
