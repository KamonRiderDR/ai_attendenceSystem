import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyUiFiles.proc_mainwin_staff_ui.complain_apply_ui import Ui_Complain_Apply_Ui
from PyUiWidgets.TitleBar import UniversalTitle_Widget

class Complain_Apply_Widget(QWidget,Ui_Complain_Apply_Ui):
    def __init__(self):
        super(Complain_Apply_Widget, self).__init__()

        self.mainUI = Ui_Complain_Apply_Ui()
        self.mainUI.setupUi(self)

    def slot_cancel(self):
        self
    
    def submit(self):
        print("apply")
        QMessageBox.information( self,"提示","申诉已提交！" )

    def cancel(self):
        QMessageBox.information( self,"提示","已清空！" )
        print("cancel")



class Complain_Apply_Win(UniversalTitle_Widget):
    def __init__(self, *args, **kwargs):
        super(Complain_Apply_Win, self).__init__(*args, **kwargs)


        self.background = QWidget()
        self.background.setStyleSheet("background-color:rgb(235,235,235);")
        self.checkinwidget=Complain_Apply_Widget()

        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.checkinwidget)

        self.setWindowFlags (Qt.FramelessWindowHint)
        with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.setStyleSheet(TitleBarStyleSheet.read())
        self.setWidget(self.background)
        self.resize(QSize(450,700))

        # shadow_effect=QGraphicsDropShadowEffect()
        # shadow_effect.setOffset(0,0)
        # shadow_effect.setColor(QColor("#444444"))
        # shadow_effect.setBlurRadius(5)
        # self.background.setGraphicsEffect(shadow_effect)


if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=Complain_Apply_Win()
    mainwin.show()
    sys.exit(app.exec_())


