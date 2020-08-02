
import sys
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore,QtWidgets

__version__ = "0.0.1"


def createLinechart(XSeries,chartName,seriesName,XName):
    chart = QChart()
    chart.setTitle(chartName)
    
    series = QLineSeries(chart)
    series.clear()
    for i, j in zip(range(len(XSeries)),XSeries,):
        series.append(i,j)
    
    axisY = QValueAxis()
    axisY.setRange(min(XSeries), max(XSeries))
    axisX = QBarCategoryAxis()
    axisX.setGridLineVisible(False)
    
    for i in XName:
        axisX.append(i)
    chart.addSeries(series)
    chart.setAxisX(axisX)
    chart.setAxisY(axisY)
    chart.setAnimationOptions(QChart.SeriesAnimations)

    chart.setBackgroundVisible(False)
    
    chart.legend().hide()

    font = QtGui.QFont()
    font.setFamily("Microsoft YaHei")
    font.setPointSize(10)
    font.setBold(True)
    axisX.setLabelsFont(font)
    axisY.setLabelsFont(font)
    chart.setTitleFont(font)

    return chart
