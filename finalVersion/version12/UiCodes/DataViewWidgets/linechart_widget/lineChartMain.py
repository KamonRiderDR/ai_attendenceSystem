from DataViewWidgets.linechart_widget.lineChart_ui import Ui_Form
from DataViewWidgets.linechart_widget.createLinechart import createLinechart
from PyQt5.QtChart import QChartView, QLineSeries, QChart
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *

class LineChartFrame(QWidget,Ui_Form):
    def __init__(self, y_data, title_name, series_name, line_name):
        super(LineChartFrame, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.chartView.setChart(createLinechart(y_data,title_name,series_name,line_name))
        self.ui.chartView.setRenderHint(QPainter.Antialiasing) 

    def reBuild(self, y_data, title_name, series_name, line_name):
        self.ui.chartView.setChart(createLinechart(y_data,title_name,series_name,line_name))
        self.ui.chartView.setRenderHint(QPainter.Antialiasing)

    

if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    myshow = LineChartFrame()
    myshow.show()
    sys.exit(app.exec_())