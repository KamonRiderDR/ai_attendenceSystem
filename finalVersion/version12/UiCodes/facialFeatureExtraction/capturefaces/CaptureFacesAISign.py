'''**********************
*   安典坤 
*   
*   将杨强老师的代码做了改动，用于员工考勤时采集一张员工的照片
*   
**********************'''
import cv2
import os
import numpy as np
import random
from PyQt5.QtCore import pyqtSignal,Qt,QObject
# 数据文件的路径，相对于当前文件目录下的data目录
current_dir = os.path.dirname(__file__)
# 生成数据文件的绝对路径(在window下存在汉字路径问题，需要设置系统为utf-8编码)
mod_file = os.path.join(current_dir, "data/haarcascade_frontalface_alt2.xml")


class CaptureFacesAI(QObject):
    sign_ReturnImg = pyqtSignal(np.ndarray)
    def __init__(self):
        super(CaptureFacesAI, self).__init__()
        # 采集的图像大小
        self.imgsize = 60
        # 采集的图像数目
        self.n = 0
        # 人脸侦测对象 # 因为汉字路径问题，所以直接使用相对路径，这个安装后需要注意
        # self.harr = cv2.CascadeClassifier("capturefaces/data/haarcascade_frontalface_alt2.xml")
        self.harr = cv2.CascadeClassifier(mod_file)
    
    def relight(self, imgsrc, alpha=1, bias=0):
        '''图像亮度'''
        imgsrc = imgsrc.astype(float)
        imgsrc = imgsrc * alpha + bias
        imgsrc[imgsrc < 0] = 0
        imgsrc[imgsrc > 255] = 255
        imgsrc = imgsrc.astype(np.uint8)
        #print(imgsrc)
        return imgsrc

    def createdir(self, imgpath):
        '''创建目录存放采集图像'''
        if not os.path.exists(imgpath):
            os.makedirs(imgpath)
        self.img_path = imgpath
        self.n = 0    # 创建新的目录重新计数
    
    def handle_image(self, imgsrc):
        '''侦测人脸，并做灰度处理后，保存'''
        # 转换为灰度
        gray_img = cv2.cvtColor(imgsrc, cv2.COLOR_BGR2GRAY)
        # 侦测人脸
        faces = self.harr.detectMultiScale(gray_img, 1.3, 5)
        # 循环处理人脸（缩放，灰度变化，保存）
        if len(faces) == 1:  # 如果识别出多个人脸，不处理
            for f_x, f_y, f_w, f_h in faces:
                face = imgsrc[f_y:f_y+f_h, f_x:f_x+f_w]
                face = cv2.resize(face, (self.imgsize, self.imgsize))
                # 对图像进行灰度处理, 产生3个灰度处理（这样处理今后训练出来的AI模型，对灰度具有一定的泛化能力）
                face = self.relight(face, random.uniform(0.5, 1.5), random.randint(-50, 50))
                #print(type(face))#numpy.ndarray
                cv2.imwrite(os.path.join(self.img_path, F"{self.n:03d}_1.jpg"), face)
                self.sign_ReturnImg.emit(face)
                #face = self.relight(face, random.uniform(0.5, 1.5), random.randint(-50, 50))
                #cv2.imwrite(os.path.join(self.img_path, F"{self.n:03d}_2.jpg"), face)

                #face = self.relight(face, random.uniform(0.5, 1.5), random.randint(-50, 50))
                #cv2.imwrite(os.path.join(self.img_path, F"{self.n:03d}_3.jpg"), face)
                # 标记人脸
                imgsrc = cv2.rectangle(imgsrc, (f_x, f_y), (f_x + f_w, f_y + f_h), (255, 0, 0), 1)
        
            self.n += 1
        # 返回标记过的图像
        return imgsrc
    