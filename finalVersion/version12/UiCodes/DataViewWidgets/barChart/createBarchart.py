from PyQt5.QtChart import QChartView, QChart, QBarSet, QBarSeries, QBarCategoryAxis,QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5 import QtGui, QtCore, QtWidgets

def createBarchart(XSeries,chartName,seriesName):
    chart = QChart()
    chart.setTitle(chartName)
    chart.setAnimationOptions(QChart.SeriesAnimations)
    categories = seriesName
    axis = QBarCategoryAxis()
    axis.append(categories)
    axis.setGridLineVisible(False)
    chart.createDefaultAxes()
    axisY = QValueAxis()
    axisY.setGridLineVisible(False)
    axisY.setRange(0,max(XSeries))
    set0 = QBarSet("")
    for i in XSeries:
        set0.append(i)
    series = QBarSeries()
    series.append(set0)
    chart.setAxisX(axis, series)
    chart.setAxisY(axisY)
    chart.legend().setVisible(False)
    chart.legend().setAlignment(Qt.AlignBottom)
    
    chart.addSeries(series)
    chart.setBackgroundVisible(False)

    font = QtGui.QFont()
    font.setFamily("Microsoft YaHei")
    font.setPointSize(10)
    font.setBold(True)
    axis.setLabelsFont(font)
    axisY.setLabelsFont(font)
    font = QtGui.QFont()
    font.setFamily("Microsoft YaHei")
    font.setPointSize(13)
    font.setBold(True)
    chart.setTitleFont(font)

    return chart 


'''
class Window(QChartView):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(400, 300)
        # 抗锯齿
        self.setRenderHint(QPainter.Antialiasing)

        # 图表
        chart = QChart()
        self.setChart(chart)
        # 设置标题
        chart.setTitle('Simple barchart example')
        # 开启动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # 添加Series
        series = self.getSeries()
        chart.addSeries(series)
        # 分类
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        # 分类x轴
        axis = QBarCategoryAxis()
        axis.append(categories)
        # 创建默认轴线
        chart.createDefaultAxes()
        # 替换默认x轴
        chart.setAxisX(axis, series)
        # 显示图例
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

    def getSeries(self):
        # 创建5个柱子
        set0 = QBarSet('Jane')
        set1 = QBarSet('John')
        set2 = QBarSet('Axel')
        set3 = QBarSet('Mary')
        set4 = QBarSet('Samantha')

        # 添加数据
        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5
        set3 << 5 << 6 << 7 << 3 << 4 << 5
        set4 << 9 << 7 << 5 << 3 << 1 << 2

        # 创建柱状条
        series = QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
        return series


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
'''