import sys
from PyQt5 import QtWidgets, QtCore


class MainWindow(QtWidgets.QWidget):
    """메인 윈도우"""
    qss = """
        QWidget {
            color: #000000;
            background: #666;
        }
        QWidget#windowTitle {
            color: #FFFFFF;
            background: #333;
        }
        QWidget#windowTitle QLabel {
            color: #FFFFFF;
            background: #333;
        }
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet(self.qss)

        # 레이아웃과 타이틀바 위젯 생성
        window_vbox = QtWidgets.QVBoxLayout(self)
        window_vbox.setContentsMargins(0, 0, 0, 0)
        titlebar_widget = QtWidgets.QWidget()
        titlebar_widget.setObjectName("windowTitle")
        title_hbox = QtWidgets.QHBoxLayout(titlebar_widget)
        content_vbox = QtWidgets.QVBoxLayout()
        content_vbox.setContentsMargins(3, 3, 3, 3)

        # 타이틀바와 컨텐츠 박스 안의 내용물을 생성
        title_label = QtWidgets.QLabel("윈도우 이름")
        content_textedit = QtWidgets.QTextEdit()

        # 각 항목을 레이아웃에 배치
        title_hbox.addWidget(title_label)
        content_vbox.addWidget(content_textedit)
        window_vbox.addWidget(titlebar_widget)
        window_vbox.addLayout(content_vbox)

if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    WINDOW = MainWindow()
    WINDOW.show()
    APP.exec()