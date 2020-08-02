import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import requests

from PyUiFiles.uni_showdateinfo_ui import Ui_widget_showDateInfo

class Uni_ShowDateInfo_Widget(QWidget, Ui_widget_showDateInfo):
    def __init__(self):
        super(Uni_ShowDateInfo_Widget, self).__init__()

        self.main_ui=Ui_widget_showDateInfo()
        self.main_ui.setupUi(self)

        self.queryWeather("北京")

        img_path=self.switchif_getWeatherImg(self.weather,self.temp1)
        self.setWeatherImg(img_path)

        self.main_ui.label_showweather_city.setText(self.cityName+" "+self.temp1+"-"+self.temp2)

        cdate=QDate.currentDate()
        self.main_ui.label_showToday_date.setText("<html><head/><body><p><span style=\" font-style:italic;\">"+cdate.toString("yyyy/MM/dd") +" </span></p><p><span style=\" font-style:italic;\"> "+cdate.toString("ddd")+"</span></p></body></html>")


    def switchif_getWeatherImg(self, weather, temp):
        if(weather=="晴"):
            return "image\weather_img\sunny_img.png"
        elif(weather=="多云"or weather=="多云转阴" or weather=="多云转晴" or weather=="阴"):
            return "image\weather_img\cloudy_img.png"
        elif(weather=="雨" or weather=="小雨" or weather=="中雨" or weather=="阵雨" or weather=='大雨转中雨'):
            return "image/weather_img/rainny_img.png"
        elif(weather=="雷阵雨" or weather=="暴雨" or weather=="大暴雨" or weather=="特大暴雨" or weather=="大到暴雨"
            or weather=="暴雨到大暴雨"):
            return "image\weather_img\storm_img.png"
        else:
            if(int(temp.replace('℃',""))<10):
                return "image\weather_img\cold_img.png"
            return "image\weather_img\hot_img.png"

    def queryWeather(self, city_name):
        print('* queryWeather  ')
        cityName = city_name
        cityCode = self.transCityName(cityName)

        rep = requests.get('http://www.weather.com.cn/data/cityinfo/' + cityCode + '.html')
        rep.encoding = 'utf-8'

        self.cityName=rep.json()['weatherinfo']['city']
        self.weather=rep.json()['weatherinfo']['weather']
        self.temp1=rep.json()['weatherinfo']['temp1']
        self.temp2=rep.json()['weatherinfo']['temp2']

    def transCityName(self, cityName):
        cityCode = ''
        if cityName == '北京':
            cityCode = '101010100'
        elif cityName == '天津':
            cityCode = '101030100'
        elif cityName == '上海':
            cityCode = '101020100'

        return cityCode

    def setWeatherImg(self, img_path):
        '''set img'''
        self.main_ui.label_showWeather_img.setPixmap(QPixmap.fromImage(QImage(img_path)))
        self.main_ui.label_showWeather_img.setAlignment(Qt.AlignCenter)
        self.main_ui.label_showWeather_img.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.main_ui.label_showWeather_img.setScaledContents(True)
        self.main_ui.label_showWeather_img.setStyleSheet("border-radius:8px;")

if __name__ == "__main__":
    app = QApplication( sys.argv )
    testUI = Uni_ShowDateInfo_Widget()
    testUI.show()
    sys.exit( app.exec_() )