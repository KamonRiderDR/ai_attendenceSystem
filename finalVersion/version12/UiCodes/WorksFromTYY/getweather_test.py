import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.queryWeather()

    def queryWeather(self):
        print('* queryWeather  ')
        cityName = "北京"
        cityCode = self.transCityName(cityName)

        rep = requests.get('http://www.weather.com.cn/data/cityinfo/' + cityCode + '.html')
        rep.encoding = 'utf-8'
        print(rep.json())

        #msg5 = '天气: %s' % rep.json()['weatherinfo']['weather'] + '\n'

        

    def transCityName(self, cityName):
        cityCode = ''
        if cityName == '北京':
            cityCode = '101010100'
        elif cityName == '天津':
            cityCode = '101030100'
        elif cityName == '上海':
            cityCode = '101020100'

        return cityCode

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())