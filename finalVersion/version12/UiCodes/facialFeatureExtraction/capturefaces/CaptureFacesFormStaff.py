'''**********************
*   安典坤 
*   
*   将杨强老师的代码做了改动，用于添加员工采集员工的人脸
*   
**********************'''
import PyQt5
from PyQt5.QtWidgets import QDialog,QWidget
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap
import sys, os
import numpy as np
import cv2
from .CaptureFacesUI import Ui_CaptureFaces
from .CaptureFacesDevsStaff import CaptureFacesDevs

class  CaptureFacesForm(QWidget):
    # 开始与停止采集的信号
    sign_captrue = pyqtSignal(str)
    sign_ExComplete = pyqtSignal(str)
    # 构造器，完成UI初始化，摄像头设备初始化等。
    def __init__(self):
        super(CaptureFacesForm, self).__init__()
        self.ui = Ui_CaptureFaces()
        self.ui.setupUi(self)
        
        # 摄像头线程创建与开启
        self.dev = CaptureFacesDevs(0)
        self.dev.sign_show.connect(self.show_video)   # 绑定信号，用于处理发送过来的视频
        self.sign_captrue.connect(self.dev.get_state) # 绑定采集控制信号到采集设备线程
        self.dev.start()
    def letDevRun(self):
        self.sign_captrue.emit('testName')
    # Ctrl + G / Ctrl + S按键处理
    #def keyReleaseEvent(self, e):
    #    # Ctrl + G重新开始采集处理
    #    if e.modifiers() == Qt.ControlModifier and e.key()==Qt.Key_G:

    #        self.name = 'testName'
    #        # 释放窗体
    #        # 发送信号开始采集-发送字符串
    #        self.sign_captrue.emit(self.name)
    #    if e.modifiers() == Qt.ControlModifier and e.key()==Qt.Key_R:
    #        # 继续采集
    #        self.sign_captrue.emit("continue") 
    #    # Ctrl + S暂停采集
    #    if e.modifiers() == Qt.ControlModifier and e.key()==Qt.Key_S:
    #        # 发送信号给采集线程，停止保存侦测到的人脸图像
    #        self.sign_captrue.emit("stop")  # 发送停止的信号

    def closeEvent(self, e):
        # 窗体关闭前的释放工作,条件不满足可以阻止窗体关闭
        # sys.exit(0)
        self.dev.close() # 窗体退出前，先关闭线程；
        #self.sign_ExComplete.emit("True")
    def keyPressEvent(self, e):
        # 阻止按照ESC键关闭窗体
        pass

    # 显示摄像头发送过来的图像
    def show_video(self, h, w, d, bytes_video):
        self.img_bytes = bytes_video
        self.img_shape = (h, w, d)
        # 显示图像到标签框
        image = QImage(bytes_video, w, h, d * w, QImage.Format_BGR888)    # 把字节转换为QImage对象
        pixmap = QPixmap.fromImage(image)                                 # 把QImage转换为QPixmap
        self.ui.lbl_video.setPixmap(pixmap)                               # QLabel只接受QPixmap类型的图像
        self.ui.lbl_video.setScaledContents(True)                         # 根据QLabel大小缩放图像