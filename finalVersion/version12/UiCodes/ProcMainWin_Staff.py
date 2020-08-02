# -*- coding:utf-8 -*-
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ProcMainWin_Manager import TitleBar,ProcMainWin_ui
from PyUiWidgets.proc_mainwin_staff import Proc_MainWin_Widget_Staff
from client import selfClose
from WorksFromDR.workingSetDAO import drClose

class ProcMainWin_Staff(QWidget):
    def __init__(self, *args, **kwargs):
        super(ProcMainWin_Staff, self).__init__(*args, **kwargs)
        main_layout = QVBoxLayout(self, spacing=0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.setWindowIcon(QIcon("image\proc_mainimg.png"))

        self.background = QWidget()
        self.background.setObjectName("widget_bg")
        self.background.setStyleSheet("""QWidget#widget_bg{
            background-color:rgb(240,240,240); 
            border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;}""")
        self.TestMainWin_Staff=Proc_MainWin_Widget_Staff()

        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.TestMainWin_Staff)

        main_layout.addWidget(self.background)

        shadow_effect=QGraphicsDropShadowEffect()
        shadow_effect.setOffset(0,0)
        shadow_effect.setColor(QColor("#444444"))
        shadow_effect.setBlurRadius(5)
        self.background.setGraphicsEffect(shadow_effect)
    def closeEvent(cls, self, QCloseEvent):
        selfClose()
        drClose()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
        app.setStyleSheet(TitleBarStyleSheet.read())
    mainWnd = ProcMainWin_ui()
    mainWnd.resize(QSize(1520,900))
    mainWnd.setWidget(ProcMainWin_Staff(mainWnd))  
    mainWnd.show()
    sys.exit(app.exec_())