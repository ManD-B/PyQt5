import sys

from PyQt5.QtCore import Qt, QMimeData, QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QDropEvent, QMouseEvent, QDrag

import pyautogui


class VirtualKeyboard(QWidget):

    def __init__(self):
        super(VirtualKeyboard, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setFocusPolicy(Qt.NoFocus)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAcceptDrops(True)

        self.title = '가상키보드 및 조이패드'
        self.setting = False
        self.currBtn = None
        self.allBtns = []
        self.keyBtns = []
        self.moveEn = False
        self.sizeEn = False

        self.initUI()
        self.no_focus()

    def initUI(self):
        self.setGeometry(300, 300, 700, 400)

        # setting mode background
        self.settingBackground = QLabel('', self)
        self.settingBackground.hide()
        self.settingBackground.setGeometry(0, 0, 1000, 1000)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 100)")

        # load saved data
        import os
        if os.path.exists('save.txt'):
            try:
                self.load_btns()
            except Exception as e:
                # not good 'save.txt' -> restart
                os.remove('save.txt')
                os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            # initial setting
            self.add_system_btns([600, 50], [500, 50], [self.width() - 25, 0])

            self.btnLeft = QPushButton('Left', self)
            self.btnLeft.setStyleSheet("color: rgb(255, 255, 255);"
                                       "background-color: rgba(0, 0, 0, 5);"
                                       "border: 2px solid rgb(255, 255, 255);"
                                       "border-radius: 25px")
            self.btnLeft.setGeometry(600, 300, 50, 50)

            self.btnA = QPushButton('a', self)
            self.btnA.setStyleSheet("color: rgb(255, 255, 255);"
                                    "background-color: rgba(0, 0, 0, 5);"
                                    "border: 2px solid rgb(255, 255, 255);"
                                    "border-radius: 25px")
            self.btnA.setGeometry(200, 200, 50, 50)

            self.keyBtns.append(self.btnLeft)
            self.keyBtns.append(self.btnA)

            for btn in self.keyBtns:
                # key repeat setting
                btn.setAutoRepeatInterval(5)
                btn.setAutoRepeat(True)

                self.btn_press_connect(btn)

                self.allBtns.append(btn)

        # button that drag and move window
        self.moveBtn = QLabel('---', self)
        self.moveBtn.setAlignment(Qt.AlignCenter)
        self.moveBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                   "background-color: rgba(0, 0, 0, 5);"
                                   "border: 1px solid rgb(255, 255, 255);"
                                   )
        self.moveBtn.setGeometry(0, 0, 50, 25)

        # button that adjust window size by drag
        self.sizeBtn = QLabel('---', self)
        self.sizeBtn.setAlignment(Qt.AlignCenter)
        self.sizeBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                   "background-color: rgba(0, 0, 0, 5);"
                                   "border: 1px solid rgb(255, 255, 255);"
                                   )
        self.sizeBtn.setGeometry(self.width() - 50, self.height() - 25, 50, 25)

        self.btn_press_connect(self.settingBtn)
        self.settingBtn.clicked.connect(self.setting_click)

        self.btn_press_connect(self.addBtn)
        self.addBtn.clicked.connect(self.add_click)

        self.btn_press_connect(self.closeBtn)
        self.closeBtn.clicked.connect(self.close)

        self.setWindowTitle(self.title)
        self.show()

    def btn_press_connect(self, btn):
        btn.pressed.connect(lambda: self.key_click(btn))

    def key_click(self, btn):
        self.set_currBtn(btn)

        if not self.setting and btn in self.keyBtns:
            pyautogui.press(self.convert_key_str(btn.text()))

    def set_currBtn(self, btn):
        self.currBtn = btn
        self.moveEn = False
        self.sizeEn = False

    def setting_click(self):
        """switching to normal/setting mode"""
        if self.setting:
            self.setting = False
            self.settingBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                          "background-color: rgba(0, 0, 0, 5);"
                                          "border: 2px solid rgb(255, 255, 255);"
                                          "border-radius: 4px")
            self.currBtn = None
            self.settingBackground.hide()
            self.addBtn.hide()
            self.addCombo.hide()
        else:
            self.setting = True
            self.currBtn = None
            self.settingBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                          "background-color: rgba(0, 0, 0, 100);"
                                          "border: 2px solid rgb(255, 255, 255);"
                                          "border-radius: 4px")
            self.settingBackground.resize(self.size())
            self.settingBackground.show()
            self.addBtn.show()
            self.addCombo.show()

    def add_click(self):
        """add new key button"""
        self.newBtn = QPushButton(self.addCombo.currentText(), self)
        self.newBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                  "background-color: rgba(0, 0, 0, 5);"
                                  "border: 2px solid rgb(255, 255, 255);"
                                  "border-radius: 25px")
        self.newBtn.setGeometry(500, 100, 50, 50)
        self.btn_press_connect(self.newBtn)
        self.newBtn.setAutoRepeatInterval(5)
        self.newBtn.setAutoRepeat(True)
        self.newBtn.show()
        self.keyBtns.append(self.newBtn)
        self.allBtns.append(self.newBtn)

    def convert_key_str(self, text):
        """convert key button's text into text that pyautogui serves"""
        if text == 'tab':
            return '\t'
        elif text == 'enter':
            return '\n'
        elif text == 'enter(r)':
            return '\r'
        elif text == 'space':
            return ' '
        else:
            return text

    def dropEvent(self, e: QDropEvent):
        """
        drag and drop buttons in setting mode
        (add button and add combobox move together)
        """
        if self.setting and self.currBtn is not None:
            position = e.pos()
            self.currBtn.move(position)
            if self.currBtn == self.addBtn:
                self.addCombo.move(position - QPoint(100, 0))

            self.currBtn = None

            e.setDropAction(Qt.MoveAction)
        e.accept()

    def dragEnterEvent(self, e: QMouseEvent):
        e.accept()

    def mouseMoveEvent(self, e: QMouseEvent):
        """
        key button: make meme data for drag
        move button: move window
        size button: adjust size of window
        """
        if e.buttons() == Qt.RightButton:
            return

        if self.setting:
            mime_data = QMimeData()
            drag = QDrag(self)
            drag.setMimeData(mime_data)

            drag.exec_(Qt.MoveAction)
        elif self.moveEn:
            self.move(e.globalPos() - self.mouse_position)
        elif self.sizeEn:
            self.mouse_position_move = e.globalPos() - self.pos()
            self.increaesd_size = self.mouse_position_move - self.mouse_position
            self.resize(self.width() + self.increaesd_size.x(), self.height() + self.increaesd_size.y())
            self.mouse_position = self.mouse_position_move
            self.sizeBtn.move(self.width() - 50, self.height() - 25)

            # if close button escape window range, move
            if self.closeBtn.pos().x() >= self.width() - 25:
                self.closeBtn.move(self.width() - 25, self.closeBtn.pos().y())

    def mousePressEvent(self, e: QMouseEvent):
        """
        get mouse position
        check whether move or size button by mouse's x pos
        """
        self.my_position = self.pos()
        self.mouse_position = e.globalPos() - self.my_position
        self.mid_x = self.my_position.x() + self.width()/2

        if e.globalPos().x() < self.mid_x:
            self.moveEn = True
            self.sizeEn = False
        else:
            self.sizeEn = True
            self.moveEn = False

        e.accept()

    def mouseReleaseEvent(self, e: QMouseEvent):
        self.currBtn = None

    def add_system_btns(self, settingXY, addXY, closeXY):
        """
        add system buttons(setting, add, close)
        :param settingXY: setting button position [x, y]
        :param addXY: same
        :param closeXY: same
        """
        self.settingBtn = QPushButton('설정', self)
        self.settingBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                      "background-color: rgba(0, 0, 0, 5);"
                                      "border: 2px solid rgb(255, 255, 255);"
                                      "border-radius: 4px")
        self.settingBtn.setGeometry(settingXY[0], settingXY[1], 60, 30)

        self.addBtn = QPushButton('추가', self)
        self.addBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                  "background-color: rgba(0, 0, 0, 5);"
                                  "border: 2px solid rgb(255, 255, 255);"
                                  "border-radius: 4px")
        self.addBtn.setGeometry(addXY[0], addXY[1], 60, 30)
        self.addBtn.hide()

        self.addCombo = QComboBox(self)
        self.addCombo.addItems(['tab', 'enter', 'enter(r)', 'space', '!', '"', '#', '$', '%', '&', "'", '(',
                                ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                                '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
                                'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
                                'browserback', 'browserfavorites', 'browserforward', 'browserhome',
                                'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
                                'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
                                'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
                                'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
                                'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                                'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
                                'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
                                'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
                                'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
                                'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
                                'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
                                'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
                                'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
                                'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
                                'command', 'option', 'optionleft', 'optionright'])
        self.addCombo.setStyleSheet("color: rgb(255, 255, 255);"
                                    "background-color: rgba(0, 0, 0, 5);"
                                    "border: 2px solid rgb(255, 255, 255);"
                                    "border-radius: 4px")
        self.addCombo.setGeometry(addXY[0] - 100, addXY[1], 100, 20)
        self.addCombo.hide()

        self.closeBtn = QPushButton('x', self)
        self.closeBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                    "background-color: rgba(0, 0, 0, 5);"
                                    "border: 1px solid rgb(255, 255, 255);"
                                    )
        self.closeBtn.setGeometry(closeXY[0], closeXY[1], 25, 25)

        self.allBtns.append(self.settingBtn)
        self.allBtns.append(self.addBtn)
        self.allBtns.append(self.closeBtn)

    def save_btns(self):
        """save window geometry and button's position"""
        with open('save.txt', 'wt') as fout:
            print(self.x(), self.y(), self.width(), self.height(), file=fout)

            for btn in self.allBtns:
                print(btn.text(), btn.pos().x(), btn.pos().y(), file=fout)

    def load_btns(self):
        """load data from save.txt"""
        with open('save.txt', 'rt') as fin:
            windowGeo = list(map(int, fin.readline().split()))
            self.setGeometry(windowGeo[0], windowGeo[1], windowGeo[2], windowGeo[3])

            settingXY = list(map(int, fin.readline().split()[1:3]))
            addXY = list(map(int, fin.readline().split()[1:3]))
            closeXY = list(map(int, fin.readline().split()[1:3]))

            self.add_system_btns(settingXY, addXY, closeXY)

            while True:
                line = fin.readline().split()
                if not line:
                    break

                self.newBtn = QPushButton(line[0], self)
                self.newBtn.setStyleSheet("color: rgb(255, 255, 255);"
                                          "background-color: rgba(0, 0, 0, 5);"
                                          "border: 2px solid rgb(255, 255, 255);"
                                          "border-radius: 25px")
                self.newBtn.setGeometry(int(line[1]), int(line[2]), 50, 50)
                self.btn_press_connect(self.newBtn)
                self.newBtn.setAutoRepeatInterval(5)
                self.newBtn.setAutoRepeat(True)
                self.newBtn.show()
                self.keyBtns.append(self.newBtn)
                self.allBtns.append(self.newBtn)

    def no_focus(self):
        """set window No Activate mode"""
        import ctypes
        import win32con 

        user32 = ctypes.windll.user32
        dc = user32.FindWindowW(0, self.title)
        user32.SetWindowLongPtrW(dc, win32con.GWL_EXSTYLE, user32.GetWindowLongPtrW(dc, win32con.GWL_EXSTYLE)
                                 | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_APPWINDOW)

    def closeEvent(self, e):
        self.save_btns()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VirtualKeyboard()
    ex.show()
    sys.exit(app.exec_())