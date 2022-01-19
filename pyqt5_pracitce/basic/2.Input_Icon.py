import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('img/test.png'))
      # self.move(300, 200) # 왼쪽위로부터 창이 떨어진 길이 조정
      # self.resize(1000, 200) # 가로 세로 길이 조정
      self.setGeometry(300, 300, 300, 200) # 위의 두 코드를 합친것과 같은역할
      self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())