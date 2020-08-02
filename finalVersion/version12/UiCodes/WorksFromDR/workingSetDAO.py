#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :workingSetDAO.py
@说明    : 考勤时间设置，与数据库直接交互
@时间    :2020/07/25 10:01:59
@作者    :dongrui
@版本    :1.0
'''
import pymysql
import socket
import sys
import time
import json

host=socket.gethostname()
port=10000
s = socket.socket( socket.AF_INET,socket.SOCK_STREAM )
s.connect( (host,port) )
#-----------保存时间------------#
def workingTimeSave( startTime,endTime ):

    print( "DR1连接成功!" )
    name = str("workingTimeSave").strip()
    s.send( name.encode('utf-8') )
    time = []
    time.append( name )
    time.append( startTime )
    time.append( endTime )
    data = json.dumps( time )
    # st = startTime.encode( 'utf-8' )
    # et = endTime.encode( 'utf-8' )
#    s.send( st )
#    s.send( et )
    s.send( data.encode('utf-8') )
    print("Send!")

    result=s.recv(102400).decode('utf-8')#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    result=json.loads(result)
    print(result)
    
    print( "DR1准备返回!" )
    return result

#---------------工作日保存----------#
def workingDaySave( dateList ):

    print( "DR2连接成功!" )
    name = str("workingDaySave").strip()
    s.send( name.encode('utf-8') )
    date = []
    date.append( name )
    for item in dateList:
        date.append( item )
    
    date = json.dumps( date )
    s.send( date.encode( 'utf-8' ) )
    print( "send!" )

    result=s.recv(102400).decode('utf-8')#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    result=json.loads(result)

    
    print( "DR2准备返回!" )
    return result


#-----------获取公司考勤情况------------#
def getWorkingDay():

    print( "DR3连接成功!" )
    name = str( "getWorkingDay" ).strip()
    s.send( name.encode('utf-8') )
    test = []
    test.append( name )
    test.append(['2020-07-17',1])
    test = json.dumps( test )
    s.send( test.encode('utf-8') )

    result=s.recv(102400).decode('utf-8')#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    result=json.loads(result)

    print( "DR3准备返回!" )
    return result

def getStaffWorkingTime( id ):

    print( "DR4连接成功!" )
    name = str( "getStaffWorkingTime" ).strip()
    s.send( name.encode('utf-8') )
    test = []
    test.append( name )
    test.append(id)
    test = json.dumps( test )
    s.send( test.encode('utf-8') )
    print("两个发送")
    result=s.recv(102400).decode('utf-8')#  类型 bytes，服务器返回值，可以没有，自己在服务器改
    result=json.loads(result)
    
    print( "DR4准备返回!" )
    return result
def drClose():
    s.close()



