import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyUiFiles.proc_signin_ui import Ui_Proc_SignIn
from PyUiWidgets.TitleBar import UniversalTitle_Widget

class Proc_SignIn_Widget(QWidget, Ui_Proc_SignIn):
    def __init__(self):
        super(Proc_SignIn_Widget, self).__init__()

        self.main_ui=Ui_Proc_SignIn()
        self.main_ui.setupUi(self)

class Proc_SignIn_Win(UniversalTitle_Widget):
    def __init__(self, *args, **kwargs):
        super(Proc_SignIn_Win, self).__init__(*args, **kwargs)
        self.background = QWidget()
        self.background.setStyleSheet("background-color:rgb(235,235,235);")
        self.SignInwidget=Proc_SignIn_Widget()

        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.SignInwidget)

        self.setWindowFlags (Qt.FramelessWindowHint)
        with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.setStyleSheet(TitleBarStyleSheet.read())
        self.setWidget(self.background)
        self.resize(QSize(450,600))

        '''set background shadow effect'''
        # shadow_effect=QGraphicsDropShadowEffect()
        # shadow_effect.setOffset(0,0)
        # shadow_effect.setColor(QColor("#444444"))
        # shadow_effect.setBlurRadius(5)
        # self.background.setGraphicsEffect(shadow_effect)

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=Proc_SignIn_Win()
    mainwin.show()
    sys.exit(app.exec_())