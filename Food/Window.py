# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Windows.MeetWindow import MeetWindowClass
from Windows.VegWindow import VegWindowClass


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style_btn = 'font-size:18px;color:green'
        self.style_btn_main = 'font-size:30px;color:green'

        self.exit = QPushButton('Выход')
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.exit.setStyleSheet(self.style_btn)
        self.exit.resize(90, 35)
        self.exit.move(10, 330)

        self.window_meet = QPushButton('Перейти к мясу', self)
        self.window_meet.clicked.connect(self.MeetWindow_fun)
        self.window_meet.setStyleSheet(self.style_btn_main)
        self.window_meet.resize(480, 100)
        self.window_meet.move(35, 40)

        self.window_veg = QPushButton('Перейти к овощам и фруктам', self)
        self.window_veg.clicked.connect(self.VegWindow_fun)
        self.window_veg.setStyleSheet(self.style_btn_main)
        self.window_veg.resize(480, 100)
        self.window_veg.move(35, 160)

        exit = QPushButton('Выход', self)
        exit.clicked.connect(QCoreApplication.instance().quit)
        exit.setStyleSheet(self.style_btn)
        exit.resize(90, 35)
        exit.move(440, 300)

        self.setFixedSize(550, 350)
        self.center()
        self.setWindowIcon(QIcon('1.jpg'))
        self.setWindowTitle('Главное окно')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def VegWindow_fun(self):
        self.VegW = VegWindowClass()
        self.VegW.show()
        self.close()

    def MeetWindow_fun(self):
        self.MeetW = MeetWindowClass()
        self.MeetW.show()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
