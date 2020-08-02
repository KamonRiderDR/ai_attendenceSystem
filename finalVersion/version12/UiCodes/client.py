import pymysql
import socket
import sys
import time
import json
import numpy
host=socket.gethostname()
port=9999
s = socket.socket( socket.AF_INET,socket.SOCK_STREAM )
s.connect( (host,port) )

print("ADK连接成功")
def requestAddNewManager(id,pas):


    
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("addNewManager").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    # info    第二个数据，一个列表，装有你要完成的操作的参数,即使没有参数，传一个空的过去
    info=[]
    info.append(id)
    info.append(pas)
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端

    msg=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    print("ADK接收成功，准备返回")
    return(msg)
def getMacInfo():
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("getMacInfo").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    info=[]
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    result=json.loads(result)
    print("ADK接收成功，准备返回")
    return(result)
def deleteMac(mac):

    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("deleteMac").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    info=[]
    info.append(mac)
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    #print(result)
    #result=json.loads(result)
    
    print("ADK接收成功，准备返回")
    return(result)
def addMac(mac):
    
    
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("addMac").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    info=[]
    info.append(mac)
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    #print(result)
    #result=json.loads(result)
    
    print("ADK接收成功，准备返回")
    return(result)
#请在这里添加函数，在其他py文件中直接导入 加入的函数
def getStaffInfo():
    
    
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("getStaffInfo").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    info=[]
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(10240).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    result=json.loads(result)
    
    print("ADK接收成功，准备返回")
    return(result)
def deleteStaff(staffID):
    
    
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("deleteStaff").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    info=[]
    info.append(staffID)
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    #print(result)
    #result=json.loads(result)
    
    print("ADK接收成功，准备返回")
    return(result)

def queryExistStaff(staffID):
    
    
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("queryExistStaff").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    info=[]
    info.append(staffID)
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    #print(result)
    #result=json.loads(result)
    
    print("ADK接收成功，准备返回")
    return(result)

##
##  在员工表中增加 一条包括  id  和  姓名  的记录
##
def addNewStaff(infoList):   
    
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("addNewStaff").strip()
    #data= name.strip()
    s.send(data.encode('utf-8'))
    print("发送成功")
    # info    第二个数据，一个列表，装有你要完成的操作的参数,即使没有参数，传一个空的过去
    info=infoList
    #info.append(id)
    info=json.dumps(info)#转为 json
    print("第二次发送成功")
    s.send(info.encode('utf-8'))# 发送到客户端

    #msg=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    
    print("ADK接收成功，准备返回")
    #return(msg)
def addNewSigninRecord(Info):
    
    
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("addNewSigninRecord").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    # info    第二个数据，一个列表，装有你要完成的操作的参数,即使没有参数，传一个空的过去
    info=Info

    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端

    msg=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    
    print("ADK接收成功，准备返回")
    return(msg)

def verifyStaff(Info):
    
    
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("verifyStaff").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    # info    第二个数据，一个列表，装有你要完成的操作的参数,即使没有参数，传一个空的过去

    info = Info
    #info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端

    msg=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    
    print("ADK接收成功，准备返回")
    return(msg)
def sendPicture(img):
    
    
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("sendPicture").strip()
    s.send(data.encode('utf-8'))

    info=json.dumps(img)#转为 json
    print(sys.getsizeof(info))
    #info =img
    s.send(info.encode('utf-8'))# 发送到客户端

    msg=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    
    print("ADK接收成功，准备返回")
    return("True")

def complainapply(info):    
    print("CJB连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("complainapply").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    #print("发送成功")
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    #print(result)
    #result=json.loads(result)
    print("CJB接收成功，准备返回")
    


def complainget():    
    print("CJB连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("complainget").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    info=[]
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    result=json.loads(result)
    
    print("CJB接收成功，准备返回")

    
    return result
def breakget():  
    print("CJB连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("breakget").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    info=[]
    info=json.dumps(info)#转为 json
    s.send(info.encode('utf-8'))# 发送到客户端
        
    breakresult=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    breakresult=json.loads(breakresult)
    
    print("CJB接收成功，准备返回")
    return breakresult
    

def breakdayapply(info):   
    print("CJB连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("breakdayapply").strip()
    s.send(data.encode('utf-8'))
    #print("发送成功")
    s.send(info.encode('utf-8'))# 发送到客户端
    result=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    
    print("CJB接收成功，准备返回")
    return result

def sendWav(info):
    print("ADK连接成功")
    #  data   第一个传送的数据，一个字符串，告诉服务器我需要干什么
    data= str("sendWav").strip()
    s.send(data.encode('utf-8'))
    myData=info
    print("第一个参数发送成功")
    s.send(myData)# 发送到客户端
    print("第二个参数发送成功")
    msg=s.recv(1024).decode()#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    
    print("ADK接收成功，准备返回")
    return(msg)

def selfClose():
    s.close()