import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup
import cv2
# 界面文件

from WorksFromADK.addManager.addManagerUI import Ui_addManager

class addManagerWidget(QWidget,Ui_addManager):
    def __init__(self):
        super(addManagerWidget, self).__init__()
        self.mainUI = Ui_addManager()
        self.mainUI.setupUi(self)
    def addNewManager(self):
        QMessageBox.information(self,"添加管理员","添加管理员成功！",QMessageBox.Yes)



if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    myshow = addManagerWidget()
    myshow.show()
    sys.exit(app.exec_())
