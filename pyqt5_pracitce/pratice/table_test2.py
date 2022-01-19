import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
class MainWindow(QtWidgets.QMainWindow):
    """표를 보여주는 위젯"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle('관리자 설정') # 창 이름 설정
        self.move(100, 200) # 왼쪽위로부터 창이 떨어진 길이 조정
        self.resize(1000, 600)
        self.tableWidget = self.tableWidget() # 표 위젯 불러오기
        
    def tableWidget(self):
        self.dialog = QDialog()
        # self.dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # 제목표시줄 제거
        title = QLabel('Frame:', self.dialog)
        title.move(20, 20)
        title.setFont(QFont('Arial', 30))
        
        close_btn = QPushButton('X', self.dialog)
        close_btn.move(800,20)
        close_btn.clicked.connect(QCoreApplication.instance().quit)
        close_btn.setMaximumSize(30,30)

        table = QTableWidget(self.dialog)
        table.move(20, 100)
        table.resize(800, 600) # 가로 세로 길이 조정
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 크기를 맞춰줌
        #table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # table.setColumnWidth(2, 10) # 크기 개별 설정시 사용 
        # 표의 크기를 지정
        table.setColumnCount(12)
        table.setRowCount(16)
        # 열 제목 지정
        table.setVerticalHeaderLabels(
            ['1동', '2동', '3동','4동', '5동','6동', '7동', '8동', '9동', '10동', '11동', '12동', '13동', '14동', '15동', '합계']
        )
        table.setHorizontalHeaderLabels(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        )

        blank_len = 30
        a=10
        b=0.999
        c=1.000
        # 셀 내용 채우기
        table.setItem(0, 0, QTableWidgetItem(str(a)))
        table.setItem(0, 1, QTableWidgetItem('2'))
        table.setItem(0, 2, QTableWidgetItem(str(a) + '%'))
        table.setItem(0, 5, QTableWidgetItem(str(b))) # input로 들어와야함(추후 수정 필요)
        table.setItem(1, 5, QTableWidgetItem(str(c)))

        self.dialog.setWindowTitle('dialog')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(1000, 600) # 가로 세로 길이 조정
        self.dialog.show()

        # ckbox = QCheckBox() 
        # table.setCellWidget(2, 6, ckbox)

        # table.setItem(11, 2, QTableWidgetItem('닫기'))

if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WINDOW = MainWindow()
    WINDOW.show()
    APP.exec()