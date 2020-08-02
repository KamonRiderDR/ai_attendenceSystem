'''**********************
*   安典坤 
*   服务器应用
*   访问数据库，进行增删改查
*   人脸验证、人脸模型训练、声纹验证
**********************'''
import pymysql
import socket
import sys
import time
import json
import numpy
import cv2
import os
import datetime
from faceRecognizeAndTrain.trainAlexnet import ConvNetTrainer
import faceRecognizeAndTrain.trainAlexnet
from faceRecognizeAndTrain.reco import ConvNetRecognizier
from PyQt5.QtCore import pyqtSignal
from concurrent.futures import ThreadPoolExecutor

import librosa
import soundfile as sf 
import voiceRecognize.model
import scipy.misc

import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class Mymodel(object):
    """docstring for Mymodel"""
    def __init__(self, network):
        super(Mymodel, self).__init__()
 
        self.network = network
    def get_feats(self, specs):
        feats = []
        feats = self.network.predict(specs)
        return feats

# ===========================================
#            声学特征处理
# ===========================================
def wav2spec(wav):
    wav = numpy.append(wav, wav[::-1])
    wav = wav.astype(numpy.float)
    linear_spect = librosa.stft(wav, n_fft=512, win_length=400, hop_length=160).T  #快速傅里叶变换
    mag, _ = librosa.magphase(linear_spect)  
    spec_mag = mag.T
    mu = numpy.mean(spec_mag, 0, keepdims=True)
    std = numpy.std(spec_mag, 0, keepdims=True)
    specs = (spec_mag - mu) / (std + 1e-5)
    specs = numpy.expand_dims(numpy.expand_dims(specs, 0), -1)  #增加一个维度
    return specs
class serverClass:
    def __init__(self, *args, **kwargs):
   
        # 打开数据库连接
        self.db = pymysql.connect("localhost","root","admin123","test_db" )
        
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        self.serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host=socket.gethostname()#获取本地主机名
        self.port=9999
        #绑定端口号
        self.serversocket.bind((self.host,self.port))

        #设置最大连接数
        self.serversocket.listen(5)
        self.lastName=''
        self.lastID=""

        #人脸模型训练和人脸验证
        self.tarinNet=ConvNetTrainer()
        self.tarinNet.sign_ReturnStaffInfo.connect(self.updateStaffIdentifyInfo)
        self.recoStaff=ConvNetRecognizier()
        
        #开启多线程
        self.threadPool = ThreadPoolExecutor(max_workers=args[0], thread_name_prefix="serverThread_")
        for i in range(0,args[0]-1):
            self.threadPool.submit(self.startServer,i)

    #服务器线程       
    def startServer(self,threadID):
        while True:
            print("服务器线程_%s 启动，监听客户端链接"%(threadID))
            clientsocket,addr=self.serversocket.accept()
            while True:
                try:
                    #flg 第一个接收到的参数，表示动作
                    flg=clientsocket.recv(1024)
                    print(flg.decode())
                    #data 第二个接收到的参数，
                    data=clientsocket.recv(4000000)
                except Exception:
                    print('断开的客户端：',addr)
                    break

                reply=self.getData(flg.decode(),data)#  函数的返回值
                if not reply:
                    clientsocket.send(str("").encode())#这个if可能不需要
                    break
                clientsocket.send(reply.encode('utf-8'))
            clientsocket.close()
    
    def getData(self,requestID,data):
        #print(requestID)
        if requestID=="getStaffInfo":
            return self.getStaffInfo()
        elif requestID=="addNewManager":
            return self.addNewManager(data)
        elif requestID=="getMacInfo":
            return self.getMacInfo()
        elif requestID=="deleteMac":
            return self.deleteMac(data)
        elif requestID=="addMac":
            return self.addMac(data)
        elif requestID=="deleteStaff":
            return self.deleteStaff(data)
        elif requestID=="queryExistStaff":
            return self.queryExistStaff(data)
        elif requestID=="addNewStaff":
            return self.addNewStaff(data)
        elif requestID=="addNewSigninRecord":
            return self.addNewSigninRecord(data)
        elif requestID=="sendPicture":
            #self.threadPool.submit(self.getPicture,data)
            self.getPicture(data)
            return "True"
        elif requestID=="verifyStaff":
            return self.verifyStaff(data)
        #陈嘉博的
        elif requestID=="breakdayapply":
            return self.breakdayapply(data)
        elif requestID=="complainapply":
            return self.complainapply(data)
        elif requestID=="complainget":
            return self.complainget()
        elif requestID=="breakget":
            return self.breakget()
        elif requestID=="sendWav":
            return self.getWav(data)
        else :
            return "error"
    #########陈嘉博的函数
    def complainget(self):
        sql = "SELECT * FROM complain "
        #try:
        self.cursor.execute(sql)# 执行SQL语句
        results = self.cursor.fetchall()# 获取所有记录列表
        results = json.dumps(results)#  类型  str 
        #print(results)
        return results

    def breakget(self):
        sql = "SELECT * FROM absence"
        #try:
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        results = list(results)
        global i
        i=0
        for record in results:
            results[i]=list(results[i])
            results[i][3]=datetime.datetime.strftime(results[i][3],"%Y-%m-%d")
            results[i][4]=datetime.datetime.strftime(results[i][4],"%Y-%m-%d")
            i=i+1
        #print(results)
        results = json.dumps(results)#  类型  str
        #print(results)
        return results

    def complainapply(self,data):
        data=json.loads(data)
        #print(data[0],data[1],data[2],data[3],data[4])
        sql = "INSERT INTO complain(id,name,reason,else,specify)VALUES ('%s','%s','%s','%s','%s')"%(data[0],data[1],data[2],data[3],data[4])
        try:            
            self.cursor.execute(sql) 
            self.db.commit()         
            print("插入成功")
            return True
        except:
            print("插入失败")
            self.db.rollback()       # 如果发生错误则回滚
            return False

    def breakdayapply(self,data):
        data=json.loads(data)
        sql = "INSERT INTO signin(id,sname,reason,starttime,endtime,stat,latetime)VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(data[0],data[1],data[2],data[3],data[4],'','')
    #安典坤的函数

    #向数据库中添加新的管理员记录
    def addNewManager(self,data):
        data=json.loads(data)
        sql = "INSERT INTO ad(username,adname, passwords)VALUES ('%s','%s','%s')"%(data[0],'',data[1])
        try:            
            self.cursor.execute(sql) 
            self.db.commit()         
            print("插入成功")
            return "True"
        except:
            print("插入失败")
            self.db.rollback()       # 如果发生错误则回滚
            return "False"
    #从数据库中查询考勤机器信息
    def getMacInfo(self):
        sql = "SELECT * FROM legaladress "
        #try:
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        results = json.dumps(results)#  类型  str 

        return results
    #从数据库中删除考勤机器
    def deleteMac(self,data):
        data=json.loads(data)
        sql = "DELETE FROM legaladress WHERE MAC = '%s'" % (str(data[0]))
        try:            
            self.cursor.execute(sql) 
            self.db.commit()         # 提交到数据库执行
            print("删除成功")
            return "True"
        except:
            print("删除失败")
            self.db.rollback()       # 如果发生错误则回滚
            return "False"
    #向数据库中增加考勤机器
    def addMac(self,data):
        data=json.loads(data)
        sql = "INSERT INTO legaladress (MAC) VALUES ('%s')"%(data[0])
        try:            
            self.cursor.execute(sql) 
            self.db.commit()         
            print("添加成功")
            return "True"
        except:
            print("添加失败")
            self.db.rollback()       # 如果发生错误则回滚
            return "False"
    #从数据库中获取员工信息
    def getStaffInfo(self):
        sql = "SELECT * FROM staff "
        #try:
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        results = json.dumps(results)#  类型  str 

        return results
    #从数据库中删除员工
    def deleteStaff(self,data):
        data=json.loads(data)
        sql = "DELETE FROM staff WHERE id = '%s'" % (str(data[0]))
        try:            
            self.cursor.execute(sql) 
            self.db.commit()         
            print("删除成功")
            return "True"
        except:
            print("删除失败")
            self.db.rollback()       # 如果发生错误则回滚
            return "False"
    #查询员工是否存在，是则返回员工姓名，否则返回False
    def queryExistStaff(self,data):
        data=json.loads(data)
        print(str(data[0]))
        sql = "SELECT * FROM staff Where id = '%s'"%(str(data[0]))
        #try:
        self.cursor.execute(sql)
        results = self.cursor.fetchall()#tuple
        print("执行完")
        for id,name,sname,classID in results:
            self.lastID=id
            print(name)
            return name
        #if results:
        #    self.lastID=str(data[0])
        #    print(str(results[1]))
        #    return str(results[1])          
        #else:
        #    print("没有该员工")           
        #    return "False"
        return "False"
    #向数据库中增加新的员工
    def addNewStaff(self,data):
        data=json.loads(data)
        self.makeStaffDir(data[0])
        print("创建文件夹成功")
        sql = "INSERT INTO staff(id,sname, adnum)VALUES ('%s','%s','%s')"%(data[1],data[0],'')
        try:            
            self.cursor.execute(sql) 
            self.db.commit()         
            print("插入成功")
            return "True"
        except:
            print("插入失败")
            self.db.rollback()       # 如果发生错误则回滚
            return "False"
    def addNewSigninRecord(self,data):
        sql = "INSERT INTO signin ( id, signdate, ifworkday, starttime, endtime, stat, latetime) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
        try:            
            self.cursor.execute(sql) 
            self.db.commit()         
            print("插入成功")
            return "True"
        except:
            print("插入失败")
            self.db.rollback()       # 如果发生错误则回滚
            return "False"
    #获取员工的600张左右的人脸图像，保存到本地，然后开始训练人脸模型
    def getPicture(self,allImg):
        imgList = json.loads(allImg)
        n=0
        for image in imgList:
            img = numpy.asarray(image)
        # 还原图片
            picName=str("images/"+str(self.lastName)+"/"+str(n)+".jpg")
            cv2.imencode('.jpg',img)[1].tofile(picName)
            n=n+1
        print("写入图片成功,开始训练")

        self.tarinNet.train(epoch=10)
    #创建文件夹，存放照片    
    def makeStaffDir(self,name):
        self.lastName=name
        os.makedirs("./images/"+name)
        return "True"
    def updateStaffIdentifyInfo(self,info):
        for (name,classID) in info.items():
            print(name,classID)
    #验证员工的人脸，更新考勤数据
    def verifyStaff(self,data):
        info=json.loads(data.decode())
        id = info["id"]
        img_list=info["content"]
        img = numpy.asarray(img_list)
        cls_id, prob = self.recoStaff.recoginize(img)

        sql = "SELECT * FROM staff Where id = '%s'"%(id)
        #try:
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        curDateTime=time.strftime("%Y-%m-%d", time.localtime())
        curTime=time.strftime("%H:%M:%S", time.localtime())

        for record in results:
            print("被检测员工的class ID：  ",record[3])#str
            print("实际检测出的class ID：  ",cls_id)#numpy.int64
            print(prob)
            if str(record[3])==str(cls_id) and float(prob)>0.8:
                print("考勤成功")
                sql2 = "SELECT * FROM signin Where id = '%s' and signdate = '%s' "%(id,curDateTime)
                self.cursor.execute(sql2)
                result2 = self.cursor.fetchall()
                print(len(result2))
                if  lem(result2)==0:
                    print("没有找到考勤表中相应的记录，失败")
                    return "0"
                for record2 in result2:
                    #print(record2[4])

                    endTime=str(record2[4])
                    if endTime>curTime:
                        print("未迟到")
                        sql3 = "UPDATE signin set stat = '%s' Where id = '%s' and signdate = '%s' "%("2",id,curDateTime)
                        self.cursor.execute(sql3)
                        self.db.commit()
                        return "prob"
                    else:
                        print("迟到")
                        endTime=datetime.datetime.strptime(str(record2[4]),"%H:%M:%S")
                        curTime=datetime.datetime.strptime(curTime,"%H:%M:%S")

                        lateMin=int((curTime-endTime).seconds/60)#迟到的时间转为分钟
                        print("迟到",str(lateMin))

                        sql3 = "UPDATE signin set stat = '%s' ,latetime = '%s' Where id = '%s' and signdate = '%s' "%("1",str(lateMin),id,curDateTime)
                        self.cursor.execute(sql3)
                        self.db.commit()
                        print("return True")
                        return "prob"

            else:
                print("考勤发生错误")
                return "0"
    #获得员工考勤时的音频文件，并进行验证
    def getWav(self,data):
        print("音频文件大小为  ",sys.getsizeof(data))
        with open("tempTestAudio/"+self.lastID+".wav",'ab') as f:
            f.write(data)
        print("音频已写完")

        print("开始验证！！！")
        os.environ["CUDA_VISIBLE_DEVICES"] = "0" # 如有GPU的话取消注释该行，GPU会加速特征提取.
        print("使用GPU")
        network_eval = model.vggvox_resnet2d_icassp(input_dim=(257, None, 1),num_class=5994, mode='eval')
        print("加载权重文件")
        network_eval.load_weights(os.path.join('model/weights.h5'), by_name=True)
        print("构造模型")
        my_model = Mymodel(network_eval)

        wav1_path = "audio/"+self.lastID+".wav"
        wav2_path = "tempTestAudio/"+self.lastID+".wav"
        print("读取音频",wav1_path,wav2_path)
        audio1, sr = sf.read(wav1_path) # sr 采样率
        audio2, sr = sf.read(wav2_path)
        print("\n*\n*\n*\n*\n  获得音频")
        spec1 = wav2spec(audio1)
        spec2 = wav2spec(audio2)
        t0 = time.time()
        feat1 = my_model.get_feats(spec1)
        t1 = time.time()
        print("{} 语音时长: {}s，提取该语音所需时间: {} s".format(wav1_path, len(audio1)/sr, t1-t0))
        feat2 = my_model.get_feats(spec2)
        print("{} 语音时长: {}s，提取该语音所需时间: {} s".format(wav2_path, len(audio2)/sr, time.time()-t1))

        # 打分，参考阈值为0.82左右，即小于0.82则认为不是同一个说话人
        score = numpy.sum(feat1*feat2) 
        print(score)
        return str(score)
if __name__=="__main__":
    app=serverClass((4))
    
