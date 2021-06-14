import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawRect')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(180, 100, 160))
        qp.setPen(QPen(QColor(60, 60, 60), 3))
        qp.drawRect(20, 20, 100, 100)

        qp.setBrush(QColor(40, 150, 20))
        qp.setPen(QPen(Qt.blue, 2))
        qp.drawRect(180, 120, 50, 120)

        qp.setBrush(Qt.yellow)
        qp.setPen(QPen(Qt.red, 5))
        qp.drawRect(280, 30, 80, 40)

    # def draw_rect(self, qp):
    #     brush = QBrush(Qt.SolidPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(20, 10, 100, 60)
    #     qp.drawText(20, 90, 'Qt.SolidPattern')

    #     brush = QBrush(Qt.Dense1Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(150, 10, 100, 60)
    #     qp.drawText(150, 90, 'Qt.Dense1Pattern')

    #     brush = QBrush(Qt.Dense2Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(280, 10, 100, 60)
    #     qp.drawText(280, 90, 'Qt.Dense2Pattern')

    #     brush = QBrush(Qt.HorPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(20, 110, 100, 60)
    #     qp.drawText(20, 190, 'Qt.HorPattern')

    #     brush = QBrush(Qt.VerPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(150, 110, 100, 60)
    #     qp.drawText(150, 190, 'Qt.VerPattern')

    #     brush = QBrush(Qt.CrossPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(280, 110, 100, 60)
    #     qp.drawText(280, 190, 'Qt.CrossPattern')

    #     brush = QBrush(Qt.BDiagPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(20, 210, 100, 60)
    #     qp.drawText(20, 290, 'Qt.BDiagPattern')

    #     brush = QBrush(Qt.FDiagPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(150, 210, 100, 60)
    #     qp.drawText(150, 290, 'Qt.FDiagPattern')

    #     brush = QBrush(Qt.DiagCrossPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(280, 210, 100, 60)
    #     qp.drawText(280, 290, 'Qt.DiagCrossPattern')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())