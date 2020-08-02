from DataViewWidgets.piechart_widget.pieChart_ui import Ui_PieChart
from DataViewWidgets.piechart_widget.createPiechart import createPiechart
from PyQt5.QtChart import QChartView, QLineSeries, QChart
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *

class PieChartFrame(QWidget,Ui_PieChart):
    def __init__(self, x_data, pieslice_name):
        super(PieChartFrame, self).__init__()
        self.ui = Ui_PieChart()
        self.ui.setupUi(self)
        self.ui.chartView.setChart(createPiechart(x_data,"",pieslice_name))
        self.ui.chartView.setRenderHint(QPainter.Antialiasing)  

    def reBuild(self, x_data, pieslice_name):
        self.ui.chartView.setChart(createPiechart(x_data,"",pieslice_name))
        self.ui.chartView.setRenderHint(QPainter.Antialiasing)  

    

if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    myshow = PieChartFrame()
    myshow.show()
    sys.exit(app.exec_())