import sys
# 추후 수정
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class VKQLineEdit(QLineEdit):
    def __init__(self, parent=None, name=None, main_window_obj=None):
        super(VKQLineEdit, self).__init__(parent)
        self.name = name
        self.setFixedHeight(40)
        self.main_window_obj = main_window_obj
        self.setFocusPolicy(Qt.ClickFocus)

    def focusInEvent(self, e):
        self.main_window_obj.keyboard_widget.current_textbox = self
        self.main_window_obj.keyboard_widget.show()

        self.setStyleSheet("border: 1px solid blue;")
        super(VKQLineEdit, self).focusInEvent(e)

    def mousePressEvent(self, e):
        self.setFocusPolicy(Qt.ClickFocus)
        super(VKQLineEdit, self).mousePressEvent(e)


class KeyboardWidget(QWidget):
    def __init__(self, parent=None):
        super(KeyboardWidget, self).__init__(parent)
        self.current_textbox = None

        self.signal_mapper = QSignalMapper(self)
        self.signal_mapper.mapped[int].connect(self.button_clicked)

        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()
    
        p = self.palette()
        p.setColor(self.backgroundRole(),Qt.white)
        self.setPalette(p)
        self.setAutoFillBackground(True)
        self.text_box = QTextEdit()
        self.text_box.setFont(QFont('Arial', 12))
        self.layout.addWidget(self.text_box, 0, 0, 1, 3)

        self.names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0']
        self.button_add()

        erase_button = QPushButton('지 움')
        erase_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        erase_button.setFont(QFont('Arial', 18))
        erase_button.KEY_CHAR = Qt.Key_Backspace
        self.layout.addWidget(erase_button, 4, 2, 1, 1)
        erase_button.clicked.connect(self.signal_mapper.map)
        self.signal_mapper.setMapping(erase_button, erase_button.KEY_CHAR)
        # erase_button.setFixedWidth(60)
        # erase_button.setFixedHeight(25)

        ok_button = QPushButton('확 인')
        ok_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        ok_button.setFont(QFont('Arial', 18))
        ok_button.KEY_CHAR = Qt.Key_Home
        self.layout.addWidget(ok_button, 5, 0, 1, 2)
        ok_button.clicked.connect(self.signal_mapper.map)
        self.signal_mapper.setMapping(ok_button, ok_button.KEY_CHAR)
        # done_button.setFixedHeight(55)
        # done_button.setFixedWidth(60)

        exit_button = QPushButton('닫 기')
        exit_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        exit_button.setFont(QFont('Arial', 18))
        exit_button.KEY_CHAR = Qt.Key_Home
        self.layout.addWidget(exit_button, 5, 2, 1, 1)
        exit_button.clicked.connect(self.signal_mapper.map)
        self.signal_mapper.setMapping(exit_button, exit_button.KEY_CHAR)
        # exit_button.setFixedWidth(60)
        exit_button.setFixedHeight(55)

        self.setGeometry(0, 0, 270, 300)

        self.setLayout(self.layout)

    def button_add(self):
        # self.names = self.names_small
        print("loe")
        positions = [(i + 1, j) for i in range(4) for j in range(3)]

        for position, name in zip(positions, self.names):

            if name == '':
                continue
            button = QPushButton(name)
            button.setFont(QFont('Arial', 30))
            # button.setFixedHeight(25)
            # button.setFixedWidth(25)
            # button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

            button.KEY_CHAR = ord(name[-1])
            button.clicked.connect(self.signal_mapper.map)
            self.signal_mapper.setMapping(button, button.KEY_CHAR)
            self.layout.addWidget(button, *position)

    def button_clicked(self, char_ord):
        txt = self.text_box.toPlainText()
        if char_ord == Qt.Key_Backspace:
            txt = txt[:-1]
        elif char_ord == Qt.Key_Enter:
            txt += chr(10)
        elif char_ord == Qt.Key_Home:
            self.current_textbox.setText(txt)
            self.text_box.setText("")
            self.hide()
            return
        else:
            txt += chr(char_ord)

        self.text_box.setText(txt)


class cQLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def __init__(self, widget):
        super().__init__(widget)

    def mousePressEvent(self, QMouseEvent):
        self.se=KeyboardWidget()
        self.se.show()
        self.clicked.emit()


class main(QMainWindow):
    def __init__(self, obj):
        super().__init__()
        self.einiUI2(obj)

    def einiUI2(self, obj):
        first_name = VKQLineEdit(name=obj, main_window_obj=self)

        main_widget = QWidget()
        layout = QGridLayout()
        layout.addWidget(first_name, 0, 0)
        self.keyboard_widget = KeyboardWidget()
        layout.addWidget(self.keyboard_widget, 0, 0, 10, 10)
        main_widget.setLayout(layout)

        self.keyboard_widget.hide()
        self.setCentralWidget(main_widget)
        # self.statusBar().showMessage('Ready')
        self.setGeometry(0, 0, 270, 400)
        self.setWindowTitle('Keyboard')
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = main(app)
    ex.show()
    sys.exit(app.exec_())