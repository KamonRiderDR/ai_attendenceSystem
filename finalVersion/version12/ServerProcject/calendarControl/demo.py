from calendarServer import CalendarServer
from calendarWidget_ui import Ui_Form
from demo_createFrame import AppFrame
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)  # app = QApplication([]) 
# 创建一个窗体
dlg = AppFrame()
# 进入消息循环
status = app.exec()
# 返回状态状态给系统
sys.exit(status)