import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyUiFiles.proc_mainwin_staff_ui.breakday_apply_ui import Ui_BreakDayApply
from PyUiWidgets.TitleBar import UniversalTitle_Widget

class BreakDay_Apply_Widget(QWidget,Ui_BreakDayApply):
    def __init__(self):
        super(BreakDay_Apply_Widget, self).__init__()
        self.mainUI = Ui_BreakDayApply()
        self.mainUI.setupUi(self)

    def btnapply(self):
        print("apply")
        QMessageBox.information( self,"提示","申请已提交！" )

    def btncancel(self):
        QMessageBox.information( self,"提示","已清除！" )
        print("cancel")

class BreakDay_Apply_Win(UniversalTitle_Widget):
    def __init__(self, *args, **kwargs):
        super(BreakDay_Apply_Win, self).__init__(*args, **kwargs)


        self.background = QWidget()
        self.background.setStyleSheet("background-color:rgb(235,235,235);")
        self.bdapplywidget=BreakDay_Apply_Widget()

        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.bdapplywidget)

        self.setWindowFlags (Qt.FramelessWindowHint)
        with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.setStyleSheet(TitleBarStyleSheet.read())
        self.setWidget(self.background)
        self.resize(QSize(450,700))



if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=BreakDay_Apply_Win()
    mainwin.show()
    sys.exit(app.exec_())
