import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui

from PIL import Image

class EggAnnotator(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            # 윈도우 특성 설정
            self.setWindowTitle('EggAnnotator')  # 윈도우 타이클 지정
            self.setGeometry(0, 0, 1900, 1500)  # 윈도우 위치/크기 설정
            #
            self.show()
        except Exception as ex:
            print(str(ex))

def main():
    app = QApplication(sys.argv)
    win = EggAnnotator()
    win.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()