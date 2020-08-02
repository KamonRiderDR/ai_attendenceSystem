'''**********************
*   安典坤 
*   录音功能的原版
*   调用音频可视化窗口
*  
**********************'''
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from _tkinter import TclError
from pydub.audio_segment import AudioSegment
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton,QWidget
from PyQt5.QtGui import QIcon
import wave 
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from soundView import testApplicationWindow
import os

from PyQt5.QtCore import pyqtSignal
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget
from concurrent.futures import ThreadPoolExecutor

class ApplicationWindow(QtWidgets.QWidget):
    sign_startOpen=pyqtSignal(str)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("test window")
        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.resize(400,600)
        

        self.threadPool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="serverThread_")

        self.openMp3=testApplicationWindow()
        self.openMp3.sign_Com.connect(self.updateState)
        self.sign_startOpen.connect(self.openMp3.getState)
        vbox = QtWidgets.QVBoxLayout(self.main_widget)
        vbox.addWidget(self.openMp3)
        self.openMp3.show()
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.chanels = 1
        self.rate = 44100
        # 录音时间
        self.recordSeconds = 20
        # 要写入的文件名
        self.wave_out_putname= "声音3文件.wav"
        # 创建PyAudio对象
        self.p = pyaudio.PyAudio()
        self.threadPool.submit(self.startMy)
    def startMy(self):
        # 打开数据流
        self.stream = self.p.open(format=self.format,
                        channels=self.chanels,
                        rate=self.rate,
                        input=True,
                        frames_per_buffer=self.chunk)
        
        self.stream.start_stream()
        print("* recording33333333333")
        self.signOver=True
        # 开始录音
        self.frames = []
        self.tempFrame=[]
        n=0
        for i in range(0, int(self.rate / self.chunk * self.recordSeconds)):
            data = self.stream.read(self.chunk)
            self.tempFrame.append(data)
            if n%20==0:
                fileName="./soundFile/sound"+str(n)+".wav"
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

        # 写入录音文件
        wf = wave.open(self.wave_out_putname, 'wb')
        wf.setnchannels(self.chanels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        self.openMp3.close()
        self.main_widget.close()
    def updateState(self):
        self.signOver=True
  
 
if __name__ == "__main__":
    App = QApplication(sys.argv)
    aw = ApplicationWindow()
    aw.show()
    App.exit()
    sys.exit(App.exec_())