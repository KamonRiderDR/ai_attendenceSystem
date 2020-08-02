'''**********************
*   安典坤 
*   
*   音频可视化窗口
*   用于录音的可视化
**********************'''
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from _tkinter import TclError
from pydub import AudioSegment
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import sys
import os

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QHBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import pyqtSignal

progname = os.path.basename(sys.argv[0])
progversion = "0.1"
 
class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.ax = fig.add_subplot(1,1,1)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
 
class testApplicationWindow(QWidget):

    def __init__(self):
        #QtWidgets.QWidget.__init__(self)
        super(testApplicationWindow,self).__init__()
        self.setWindowTitle("application main window")

        
        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.resize(400,500)
        vbox = QtWidgets.QVBoxLayout(self.main_widget)
        
        self.canvas =  MyMplCanvas( self.main_widget,width=6, height=6, dpi=100) ###attention###
        vbox.addWidget(self.canvas)
 
        hbox = QtWidgets.QHBoxLayout(self.main_widget)
    #打开音频文件，开始画图
    def startOpen(self,fileName):
        p = pyaudio.PyAudio()
        sound = AudioSegment.from_file(file=fileName)
        self.left = sound.split_to_mono()[0]
        fs = self.left.frame_rate
        self.size = len(self.left.get_array_of_samples())
        channels = self.left.channels
        self.stream = p.open(
            format=p.get_format_from_width(2,),
            channels=1,
            rate=50000,  # 调整播放速率
            # input=True,
            output=True,
        )
        self.stream.start_stream()
        #fig = plt.figure()
        ax = self.canvas.figure.gca(
            # projection='polar'
        )
        norm2 = plt.Normalize(-1., 1.)
        self.lc = LineCollection([], cmap='gist_ncar', norm=norm2)
        ax.set_ylim(-1.5, 1.5)
        ax.set_axis_off()
        self.window = int(0.02*fs)
        freq = np.linspace(20, 20000, self.window // 2)
        self.time = np.linspace(0, 20, self.window)
        ax.add_collection(self.lc)
        self.ani = FuncAnimation(self.canvas.figure, self.update, frames=range(0, self.size, self.window), interval=0, blit=True)
    #画图的更新函数
    def update(self,frames):
            if self.stream.is_active():
                self.slice = self.left.get_sample_slice(frames, frames + self.window)
                y = np.array(self.slice.get_array_of_samples()) / 6000 #numpy.ndarray  1 维  882列
                points = np.array([self.time, y]).T.reshape(-1, 1, 2)
                segments = np.concatenate([points[:-1], points[1:]], axis=1)
                self.lc.set_segments(segments)
                self.lc.set_array(y)
            
            return self.lc,
    def Stop(self):
        self.stream.stop_stream()
        #self.stream.close()
        #self.p.terminate()
    def getState(self,fileName):
        self.startOpen(fileName)
    def closeEvent(cls, self, QCloseEvent):
        self.stream.close()
        self.p.terminate()
    
 
if __name__ == "__main__":
    App = QApplication(sys.argv)
    aw = testApplicationWindow()
    aw.show()
    App.exit()
    sys.exit(App.exec_())
       
