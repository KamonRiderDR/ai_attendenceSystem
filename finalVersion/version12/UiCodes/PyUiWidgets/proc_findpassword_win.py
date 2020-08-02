import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyUiFiles.proc_findpassword_ui import Ui_Proc_FindPassword
from PyUiWidgets.TitleBar import UniversalTitle_Widget

class Proc_FindPassword_Widget(QWidget, Ui_Proc_FindPassword):
    def __init__(self):
        super(Proc_FindPassword_Widget, self).__init__()

        self.main_ui=Ui_Proc_FindPassword()
        self.main_ui.setupUi(self)

class Proc_FindPassword_Win(UniversalTitle_Widget):
    def __init__(self, *args, **kwargs):
        super(Proc_FindPassword_Win, self).__init__(*args, **kwargs)
        self.background = QWidget()
        self.background.setStyleSheet("background-color:rgb(235,235,235);")
        self.FindPasswordwidget=Proc_FindPassword_Widget()

        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.FindPasswordwidget)

        self.setWindowFlags (Qt.FramelessWindowHint)
        with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.setStyleSheet(TitleBarStyleSheet.read())
        self.setWidget(self.background)
        self.resize(QSize(450,600))

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=Proc_FindPassword_Win()
    mainwin.show()
    sys.exit(app.exec_())
