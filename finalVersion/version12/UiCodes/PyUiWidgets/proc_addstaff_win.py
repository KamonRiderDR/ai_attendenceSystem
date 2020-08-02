'''**********************
*   安典坤 
*   添加员工
*   采集员工的人脸，600张图片，以及员工的个人信息，传到服务器
*   
**********************'''
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy
# 界面文件
sys.path.append('..')
from client import getStaffInfo,deleteStaff,queryExistStaff,addNewStaff,sendPicture
from facialFeatureExtraction.capturefaces.CaptureFacesFormStaff import CaptureFacesForm

from PyUiFiles.proc_addstaff_ui import Ui_Proc_addStaff
from PyUiWidgets.TitleBar import UniversalTitle_Widget

class Proc_AddStaff_Widget(QWidget, Ui_Proc_addStaff):
    def __init__(self):
        super(Proc_AddStaff_Widget, self).__init__()
        self.mainUI = Ui_Proc_addStaff()
        self.mainUI.setupUi(self)
        

        self.getFeatureWidget=CaptureFacesForm()
        self.mainUI.layout_widgetShowCaptureFrames.addWidget(self.getFeatureWidget, 0, 0, 1, 1)
        self.getFeatureWidget.dev.sign_DevReturnImg.connect(self.getStaffPic)
        self.mainUI.btn_start.clicked.connect(self.turnToGetFacialInfo)
    def setStaffInfo(self):
        staffInfo=getStaffInfo()
        print(type(staffInfo))
        self.model=QStandardItemModel(len(staffInfo),2)#存储任意结构数据
        self.model.setHorizontalHeaderLabels(['工号','姓名','所属管理员账户'])
        #水平方向标签拓展剩下的窗口部分，填满表格
        self.mainUI.tableView.horizontalHeader().setStretchLastSection(True)
        #水平方向，表格大小拓展到适当的尺寸   
        self.mainUI.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        idx=0
        for record in staffInfo:
                itemID=QStandardItem(''.join(record[0]))
                itemName=QStandardItem(''.join(record[1]))
                itemAD=QStandardItem(''.join(record[2]))
                self.model.setItem(idx,0,itemID)
                self.model.setItem(idx,1,itemName)
                self.model.setItem(idx,2,itemAD)
                idx=idx+1
        self.mainUI.tableView.setModel(self.model)
    def turnToGetFacialInfo(self):
        staffID=self.mainUI.LEdit_getId.text()
        ifExistStaff = queryExistStaff(staffID)
        if ifExistStaff=="True":
            QMessageBox.information(self,"员工管理","失败，该员工已存在！！！",QMessageBox.Yes)
            self.mainUI.LEdit_getId.setText('')
            return

        self.getFeatureWidget.letDevRun()

    def addStaffInfoToServer(self):
        print("图像提取结束")
        staffID=self.mainUI.LEdit_getId.text()
        staffName=self.mainUI.LEdit_getName.text()
        result=addNewStaff(staffID,staffName)
        if result=="True":
            QMessageBox.information(self,"员工信息管理","添加新员工成功！",QMessageBox.Yes)
            #self.setStaffInfo()
        else:
            QMessageBox.information(self,"员工信息管理","添加新员工失败！！！",QMessageBox.Yes)

        self.mainUI.LEdit_getName.setText('')
        self.mainUI.LEdit_getId.setText('')

    def deleteStaff(self):
        staffID=self.mainUI.lineEditDeleteID.text()
        ifExistStaff = queryExistStaff(staffID)
        if ifExistStaff=="False":
            QMessageBox.information(self,"员工管理","失败，该员工不存在！！！",QMessageBox.Yes)
            self.mainUI.lineEditDeleteID.setText('')
            return
        result=deleteStaff(staffID)
        if result=="True":
            QMessageBox.information(self,"员工管理","删除员工成功！",QMessageBox.Yes)
            #self.setStaffInfo()
        else:
            QMessageBox.information(self,"员工管理","删除员工失败！！！",QMessageBox.Yes)
        self.mainUI.lineEditDeleteID.setText('')
    def getStaffPic(self,imgList):
        #n=1
        #for img in imgList:
        #    cv2.imwrite(str(n)+".jpg",img)
        #    n=n+1
        #self.getFeatureWidget.close()
        staffName=self.mainUI.LEdit_getName.text()
        staffInfo=[]
        staffInfo.append(staffName)
        staffInfo.append(self.mainUI.LEdit_getId.text())
        addNewStaff(staffInfo)
        print("添加员工记录成功")
        iList=[]
        n=0
        for img in imgList:
            #cv2.imwrite(str(n)+".jpg",img)
            n=n+1
            img=img.tolist()
            iList.append(img)
        result=sendPicture(iList)
        print("写入图片成功")
        print("win返回值",result)
        if result=="True":
            QMessageBox.information(self,"员工信息管理","添加新员工成功！",QMessageBox.Yes)
            #self.setStaffInfo()
        else:
            QMessageBox.information(self,"员工信息管理","添加新员工失败！！！",QMessageBox.Yes)


class Proc_AddStaff_Win(UniversalTitle_Widget):
    def __init__(self, *args, **kwargs):
        super(Proc_AddStaff_Win, self).__init__(*args, **kwargs)
        self.background = QWidget()
        self.background.setStyleSheet("background-color:rgb(235,235,235);")
        self.addstaffwidget=Proc_AddStaff_Widget()

        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.addstaffwidget)

        self.setWindowFlags (Qt.FramelessWindowHint)
        with open("Qss\TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.setStyleSheet(TitleBarStyleSheet.read())
        self.setWidget(self.background)
        self.resize(QSize(450,700))

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=Proc_AddStaff_Win()
    mainwin.show()
    sys.exit(app.exec_())