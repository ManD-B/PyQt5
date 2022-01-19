import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class showTime(QDialog):
    def __init__(self):

        super(showTime, self).__init__()
        self.resize(500, 400)
        self.setWindowTitle ( "label display time")
        self.label = QLabel(self)
        self.label.setFixedWidth(200)
        self.label.move(90, 80)
        self.label.setStyleSheet("QLabel{background:white;}"
                                                                             "QLabel {color: rgb (300,300,300,120); font-size: 10px; font-weight: bold; font-family: Arial;}"
                                      )
                 # Dynamic display time on the label
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.label.setText("     "+ text)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my = showTime()
    my.show()
    sys.exit(app.exec_())