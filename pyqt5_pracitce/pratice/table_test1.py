import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class MainWindow(QtWidgets.QMainWindow):
    """표를 보여주는 위젯"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('선별 내역') # 창 이름 설정
        self.move(300, 200) # 왼쪽위로부터 창이 떨어진 길이 조정
        self.resize(400, 600)
        self.tableWidget = self.tableWidget() # 표 위젯 불러오기

    def tableWidget(self):
        vbox = QVBoxLayout()

        table = QTableWidget(self)
        vbox.addWidget(table)
        grid = QGridLayout() 
        vbox.addLayout(grid)
        btn1 = QPushButton("전체내용 삭제")
        grid.addWidget(btn1, 0, 0)

        table.resize(400, 600) # 가로 세로 길이 조정
        # 표의 크기를 지정
        table.setColumnCount(2)
        table.setRowCount(12)
        # 열 제목 지정
        table.setHorizontalHeaderLabels(
            ['1', '2']
        )
        table.setVerticalHeaderLabels(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        )
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 크기를 맞춰줌
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        a=80
        # 셀 내용 채우기
        table.setItem(0, 0, QTableWidgetItem(str(a)))
        table.setItem(1, 0, QTableWidgetItem('2'))
        table.setItem(0, 1, QTableWidgetItem('2%'))



        # table.setEditTriggers(QAbstractItemView.NoEditTriggers) # 편집 금지모드


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WINDOW = MainWindow()
    WINDOW.show()
    APP.exec()
