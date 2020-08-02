from PyQt5.QtChart import QChartView, QChart, QPieSeries, QPieSlice
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore,QtWidgets

def createPiechart(XSeries,chartName,seriesName):
        chart = QChart()
        chart.setTitle(chartName)       
        series = QPieSeries()

        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(True)
        font.setPointSize(10)

        series.setHoleSize(0.2)
        count = 0

        for i in range(len(XSeries)):
            count += XSeries[i]
        
        for i in range(len(XSeries)):
            slice1 = series.append(str(seriesName[i])+": {num:.2f}%".format(num =100* XSeries[i]/count), XSeries[i])
            slice1.setLabelFont(font)
            series.setLabelsVisible()

        series.setPieSize(0.5)
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.legend().hide()
        chart.setBackgroundVisible(False)
        
        return chart

