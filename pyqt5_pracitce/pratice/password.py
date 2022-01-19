import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('관리자 환경')
        self.setGeometry(300, 300, 250, 110)

        label1 = QLabel('패스워드', self)
        label1.setAlignment(Qt.AlignCenter)

        okButton = QPushButton('확 인')

        cancelButton = QPushButton('닫 기')

        hbox = QHBoxLayout()
        hbox.addStretch(1) # 신축성있는 빈공간을 제공(창을 늘리고 줄여도 그대로)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self)
        qle.move(60, 10)
        # qle.textChanged[str].connect(self.onChanged)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())