'''**********************
*   安典坤 
*   
*   将杨强老师的代码做了改动，用于添加员工采集员工的人脸
*   
**********************'''
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
import cv2
import os
import numpy
import sys
sys.path.append('..')
from .CaptureFacesAIStaff  import CaptureFacesAI
from facialFeatureExtraction.font_zh.FontZH import zh

class CaptureFacesDevs(QThread):

    # 定义信号发送采集的视频图像
    sign_show = pyqtSignal(int, int, int , bytes)  # 前面三个是图像高度，宽度，深度，最后是图像数据
    sign_DevReturnImg = pyqtSignal(list)
    def __init__(self, dev_id):
        super(CaptureFacesDevs, self).__init__()
        # 人脸侦测处理模块
        self.ai = CaptureFacesAI()
        # 完成摄像头初始化
        self.dev = cv2.VideoCapture(dev_id, cv2.CAP_DSHOW)   # 避免报一个警告(默认使用的不是DSHOW视频处理技术)
        # 用于控制线程优雅结束的逻辑变量
        self.isOver = False

        # 用于控制是否保存侦测的人脸的逻辑变量
        self.isSave = False  # 默认不保存
        self.imgList=[]
        self.ai.sign_ReturnImg.connect(self.getImg)
    # 线程运行函数
    def run(self):
        while not self.isOver:
            # 抓取视频
            status, img = self.dev.read()
            if not status:
                self.dev.release()
                self.exit(0)
            # 抓取图像成功后，需要侦测人脸并保存
            if self.isSave:
                img = self.ai.handle_image(img)
                #print(type(returnImg))
                if self.ai.n >=6:
                    self.isSave = False
                    self.sign_DevReturnImg.emit(self.imgList)
                # cv2.putText(imgsrc, F'采集数量:{self.n:03d}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 3)  #显示名字
                #img = zh.draw_text(img, (10, 20), F'采集中:{self.ai.n:03d}', 20, (0, 0, 255))
                img = zh.draw_text(img, (10, 20), F'采集中', 20, (0, 0, 255))
            else:
                img = zh.draw_text(img, (10, 20), F'停止采集', 20, (0, 255, 255))
            # 发送信号给窗体显示视频
            self.sign_show.emit(img.shape[0], img.shape[1], img.shape[2], img.tobytes())
            QThread.usleep(100000)

    def close(self):
        # 用来释放线程与设备
        self.isOver = True
        while self.isRunning():   # 避免提前释放设备导致run函数中的操作报错
            self.isOver = True
        if self.dev.isOpened():
            self.dev.release()

    def get_state(self, save_info):
        '''处理是否采集人脸的信号'''
        if save_info == "stop":
            self.isSave = False
        elif save_info == "continue":
            self.isSave = True
        else:
            self.isSave = True
            # 同时创建目录
            self.ai.createdir(os.path.join("./images", save_info))
    def getImg(self,img):
        self.imgList.append(img)
        
            