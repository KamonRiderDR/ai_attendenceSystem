from PyQt5.QtWidgets import *
from calendarWidget_ui import Ui_Form
from PyQt5.QtGui import *
from calendarServer import CalendarServer

class AppFrame(QWidget):
    def __init__(self):
        super(AppFrame, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.c = CalendarServer(self.ui.calendarWidget)
        self.show()
    
    def pageChange(self):
        self.c.calendarPaint()
        print(self.ui.calendarWidget.monthShown())