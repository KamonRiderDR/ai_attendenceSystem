from DataViewWidgets.barChart.createBarchart import createBarchart 
from DataViewWidgets.barChart.barchart_ui import Ui_Form
from PyQt5.QtChart import QChartView, QLineSeries, QChart
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class BarchartFrame(QWidget,Ui_Form):
    def __init__(self,data = [6,5,4],barChartTitle = "barchart",seriesName = ["S1","S2","S3"]):
        super(BarchartFrame, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.chartview.setChart(createBarchart(data,barChartTitle,seriesName))
        self.ui.chartview.setRenderHint(QPainter.Antialiasing) 
        self.show()

    def reBuild(self,data = [6,5,4],barChartTitle = "barchart",seriesName = ["S1","S2","S3"]):
        self.ui.chartview.setChart(createBarchart(data,barChartTitle,seriesName))
        self.ui.chartview.setRenderHint(QPainter.Antialiasing) 

    

if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    myshow = BarchartFrame()
    myshow.show()
    sys.exit(app.exec_())