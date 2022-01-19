import os, sys, traceback
import threading
from enum import Enum
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from PyQt5.QtCore import Qt, QDateTime, QTimer, QSize, QDate
from PyQt5.QtWidgets import QMenu, QSizePolicy, QSpacerItem, QWidget, QLabel, QWidget, QLineEdit, QPushButton, QShortcut, QCheckBox, QHBoxLayout, QHeaderView, QDialog, QTableWidgetItem, QTableWidget, QCalendarWidget, QMainWindow, QApplication, QTextBrowser, QTextEdit, QComboBox
from PyQt5.QtGui import QIcon, QKeySequence, QFont, QPixmap
import datetime
import glob

i = 0
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        img = glob.glob('./egg_img/*.jpg')
        global i
        pixmap = QPixmap(img[i])

        #elif e.key() == Qt.Key_C:
        self.img = QLabel(self)
        self.img.setPixmap(pixmap)
        self.img.resize(780,1000)
        self.img.move(0,0)
        self.img.repaint()

        self.setGeometry(500, 30, 780, 1000)
        self.setWindowTitle('QPixmap')

    def keyPressEvent(self, e):
        global i
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_M:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()
        elif e.key() == Qt.Key_V:
            i = i + 1
            print(i)
        elif e.key() == Qt.Key_B:
            i = i - 1
            print(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
