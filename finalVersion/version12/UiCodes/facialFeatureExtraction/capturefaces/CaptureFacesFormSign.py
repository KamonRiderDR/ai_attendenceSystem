'''**********************
*   安典坤 
*   
*   将杨强老师的代码做了改动，用于员工考勤时采集一张员工的照片
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
from .CaptureFacesDevsSign import CaptureFacesDevs
from concurrent.futures import ThreadPoolExecutor
import pyaudio
import wave
class  CaptureFacesForm(QWidget):
    # 开始与停止采集的信号
    sign_captrue = pyqtSignal(str)
    sign_ExComplete = pyqtSignal(str)
    # 构造器，完成UI初始化，摄像头设备初始化等。
    def __init__(self):
        super(CaptureFacesForm, self).__init__()
        self.ui = Ui_CaptureFaces()
        self.ui.setupUi(self)
        self.threadPool = ThreadPoolExecutor(2, thread_name_prefix="serverThread_")

        
        # 摄像头线程创建与开启
        self.dev = CaptureFacesDevs(0)
        self.dev.sign_show.connect(self.show_video)   # 绑定信号，用于处理发送过来的视频
        self.sign_captrue.connect(self.dev.get_state) # 绑定采集控制信号到采集设备线程
        self.dev.start()
        #self.threadPool.submit(self.dev.start)
        #self.threadPool.submit(self.getAudio)
        self.sign_captrue.connect(self.getAudio)
    def getAudio(self):
        # 定义数据流块
        
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        # 录音时间
        RECORD_SECONDS = 5
        # 要写入的文件名
        WAVE_OUTPUT_FILENAME = "声音文件.wav"
        # 创建PyAudio对象
        p = pyaudio.PyAudio()

        # 打开数据流
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        # 开始录音
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        # 停止数据流
        stream.stop_stream()
        stream.close()

        # 关闭PyAudio
        p.terminate()

        # 写入录音文件
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    def closeEvent(self, e):
        # 窗体关闭前的释放工作,条件不满足可以阻止窗体关闭
        # sys.exit(0)
        self.dev.close() # 窗体退出前，先关闭线程；
        self.sign_ExComplete.emit("True")
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