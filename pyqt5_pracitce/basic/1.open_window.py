# 창 띄우기
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') # 창 이름 설정
        self.move(300, 200) # 왼쪽위로부터 창이 떨어진 길이 조정
        self.resize(1000, 200) # 가로 세로 길이 조정
        self.show()


if __name__ == '__main__': # 모듈 이름이 저장되는 내장 변수로 abc.py파일 import 해서 수행하려면 __name__을 abc로 바꾸면됌
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())