'''**********************
*   安典坤 
*   员工的考勤界面
*   先是人脸验证，再声纹识别
*   还有录音的可视化
**********************'''
import sys
sys.path.append('..')
import time
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import *
import cv2
# 界面文件

from PyUiFiles.proc_mainwin_staff_ui.checkin_ui import Ui_CheckIn_Show
from PyUiWidgets.TitleBar import UniversalTitle_Widget
from facialFeatureExtraction.capturefaces.CaptureFacesFormSign import CaptureFacesForm
from client import queryExistStaff,addNewSigninRecord,sendPicture,verifyStaff,sendWav

import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from _tkinter import TclError
from pydub.audio_segment import AudioSegment
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
import wave 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyUiWidgets.soundView import testApplicationWindow
import os

from PyQt5.QtCore import pyqtSignal
import matplotlib
import random
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget
from concurrent.futures import ThreadPoolExecutor
class CheckIn_Widget(QWidget,Ui_CheckIn_Show):
    sign_startOpen=pyqtSignal(str)
    def __init__(self):
        super(CheckIn_Widget, self).__init__()
        self.mainUI = Ui_CheckIn_Show()
        self.mainUI.setupUi(self)

        #采集图片的窗口
        self.getFeatureWidget=CaptureFacesForm()

        self.mainUI.gridLayout.addWidget(self.getFeatureWidget,0,0,1,1)

        #图片采集完发送信号
        self.getFeatureWidget.dev.ai.sign_ReturnImg.connect(self.getImg)

        self.mainUI.labelTipText.hide()
        self.mainUI.labelShowNum.hide()

        #多线程，用于录音的可视化
        self.threadPool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="serverThread_")

        self.openMp3=testApplicationWindow()

        self.sign_startOpen.connect(self.openMp3.getState)

        self.mainUI.gridLayout.addWidget(self.openMp3,0,1,1,1)

        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.chanels = 1
        self.rate = 44100
        # 录音时间
        self.recordSeconds = 7
        # 要写入的文件名
        self.wave_out_putname= "PyUiWidgets/声音2文件.wav"
        # 创建PyAudio对象
        self.p = pyaudio.PyAudio()
        self.sign_startOpen.emit("PyUiWidgets/silence.wav")

        #录音函数
    def startMy(self):
        # 打开数据流
        self.stream = self.p.open(format=self.format,
                        channels=self.chanels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunk)
        
        self.stream.start_stream()
        print("* recording 22")
        self.signOver=True
        # 开始录音
        self.frames = []
        self.tempFrame=[]
        n=0
        for i in range(0, int(self.rate / self.chunk * self.recordSeconds)):
            data = self.stream.read(self.chunk)
            self.tempFrame.append(data)
            if n%20==0:
                fileName="PyUiWidgets/soundFile/sound"+str(n)+".wav"
                wf = wave.open(fileName, 'wb')
                wf.setnchannels(self.chanels)
                wf.setsampwidth(self.p.get_sample_size(self.format))
                wf.setframerate(self.rate)
            
                wf.writeframes(b''.join(self.tempFrame))
                wf.close()        
                self.tempFrame.clear()
            
                self.sign_startOpen.emit(fileName)

            self.frames.append(data)
            n=n+1
        print("* done recording")

        # 停止数据流
        self.stream.stop_stream()
        self.stream.close()

        # 关闭PyAudio
        self.p.terminate()
        #self.openMp3.close()
        self.sign_startOpen.emit("PyUiWidgets/silence.wav")

        
        # 写入录音文件
        self.wave_out_putname= "PyUiWidgets/testSoundFile/"+self.id+".wav"
        wf = wave.open(self.wave_out_putname, 'wb')
        wf.setnchannels(self.chanels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        self.mainUI.labelTipText.setText("等待验证声纹")
        self.mainUI.labelShowNum.hide()
        self.senWav()

    #将音频文件传送到服务器进行声纹验证
    def senWav(self):
        print("enter ")
        path = self.wave_out_putname

        with open(path,'rb') as f:
            print("打开了")
            message = f.read() #读出来就是字节

        print("读取到的音频文件大小为 ",sys.getsizeof(message))
        result=sendWav(message)
        print("*** ",result)
        if float(result)>0.8:
            QMessageBox.information(self,"声纹识别结果","相似度为："+result+"，通过！考勤成功！",QMessageBox.Yes)
            self.mainUI.labelTipText.setText("请读出右边的数字")
            self.mainUI.labelTipText.hide()
            self.mainUI.labelShowNum.setText('')
            self.mainUI.labelShowNum.hide()
            self.close()
        else:
            self.mainUI.labelTipText.setText("请读出右边的数字")
            self.mainUI.labelTipText.hide()
            self.mainUI.labelShowNum.setText('')
            self.mainUI.labelShowNum.hide()
            QMessageBox.information(self,"声纹识别结果","相似度为："+result+"，不通过！考勤失败！",QMessageBox.Yes)

    #打开人脸识别界面
    def turnToGetVideo(self):
        staffID=self.mainUI.lineEditGetID.text()
        ifExistStaff = queryExistStaff(staffID)
        if ifExistStaff=="False":
            QMessageBox.information(self,"考勤管理","工号错误",QMessageBox.Yes)
            self.mainUI.lineEditGetID.setText('')
           
        else: 
            self.mainUI.labelTipID.setText(ifExistStaff+" 正在考勤")
            self.getFeatureWidget.sign_captrue.emit(self.mainUI.lineEditGetID.text())
            self.getFeatureWidget.show()
            #self.getFeatureWidget.setFocus()

    #接受来自人脸采集界面传回的图片，并传到服务器进行验证          
    def getImg(self,img):
        #cv2.imwrite("test.jpg",img)
        img_list = img.tolist()

        # 字典形式保存数组
        img_dict = {}
        img_dict["content"] = img_list
        self.id=self.mainUI.lineEditGetID.text()
        img_dict["id"]=self.id
        # 保存为json格式
        info = json.dumps(img_dict)

        verifyResult=verifyStaff(info)

        if float(verifyResult)>0.8:           
            sign=QMessageBox.information(self,"人脸识别结果","相似度为："+verifyResult+"，通过！ 进入声纹识别",QMessageBox.Yes)
            num=""#生成随机数字
            for i in range(6):
                alp=str(random.randint(0,9))
                num=num+alp
            if sign==QMessageBox.Yes:
                self.mainUI.labelTipText.show()
                self.mainUI.labelShowNum.setText(num)
                self.mainUI.labelShowNum.show()
                #self.openMp3.show()
                self.threadPool.submit(self.startMy)
        else:
            self.mainUI.labelTipID.setText("请输入您的工号")

            sign=QMessageBox.information(self,"人脸识别结果","相似度为："+verifyResult+"，不通过！",QMessageBox.Yes)


class CheckIn_Win(UniversalTitle_Widget):
    def __init__(self, *args, **kwargs):
        super(CheckIn_Win, self).__init__(*args, **kwargs)

        
        self.background = QWidget()
        self.background.setStyleSheet("background-color:rgb(235,235,235);")
        self.checkinwidget=CheckIn_Widget()
        
        self.checkinwidget.resize(1100,800)
        self.resize(1100,800)
        layout = QVBoxLayout(self.background, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.checkinwidget)

        self.setWindowFlags (Qt.FramelessWindowHint)
        with open("./Qss/TitleBarQSS.qss","r",encoding='UTF-8') as TitleBarStyleSheet:
            self.setStyleSheet(TitleBarStyleSheet.read())
        self.setWidget(self.background)
        


if __name__=="__main__":
    app = QApplication(sys.argv)
    
    mainwin=CheckIn_Win()
    mainwin.show()
    sys.exit(app.exec_())
