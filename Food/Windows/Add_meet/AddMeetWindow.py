import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AddMeetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style = 'font-size:17px;color:green'
        self.style_2 = 'font-size:10px;color:red;border-radius: 10px'
        self.style_edit = 'font-size:17px;color:black;border-radius: 10px'
        self.style_btn = 'font-size:17px;color:green'
        self.style_1 = 'font-size:30px;color:red'

        self.information = QLabel('Чтобы добавить данные в программу, вам следует заполнить '
                                  'все поля\nтеми данными, которые вы хотите добавить. \nЕсли у вас нету максимальных и минимальных данных, '
                                  'то вводите одинаковые значения.', self)
        self.information.setStyleSheet(self.style_edit)
        self.information.move(10, 10)

        self.meet_label = QLabel('Из какого мясо продукт: ', self)
        self.process_label = QLabel('Какой процесс обработки: ', self)
        self.part_label = QLabel('Название продутк: ', self)
        self.time_min_label = QLabel('Минимальное время в минутах: ', self)
        self.time_max_label = QLabel('Максимальное время в минутах: ', self)
        self.mass_min_label = QLabel('Минимальные граммовки порций: ', self)
        self.mass_max_label = QLabel('Максимальные граммовки порций: ', self)

        self.meet_label.move(10, 95)
        self.process_label.move(10, 140)
        self.part_label.move(10, 185)
        self.time_min_label.move(10, 320)
        self.time_max_label.move(10, 365)
        self.mass_min_label.move(10, 230)
        self.mass_max_label.move(10, 275)

        self.meet_label.setStyleSheet(self.style_btn)
        self.process_label.setStyleSheet(self.style_btn)
        self.part_label.setStyleSheet(self.style_btn)
        self.time_min_label.setStyleSheet(self.style_btn)
        self.time_max_label.setStyleSheet(self.style_btn)
        self.mass_min_label.setStyleSheet(self.style_btn)
        self.mass_max_label.setStyleSheet(self.style_btn)

        self.meet_add = QLineEdit('', self)
        self.process_add = QLineEdit('', self)
        self.part_add = QLineEdit('', self)
        self.time_min_add = QLineEdit('', self)
        self.time_max_add = QLineEdit('', self)
        self.mass_min_add = QLineEdit('', self)
        self.mass_max_add = QLineEdit('', self)

        self.time_min_add.setValidator(QDoubleValidator(0, 9999999, 1, self.time_min_add))
        self.time_max_add.setValidator(QDoubleValidator(0, 9999999, 1, self.time_max_add))
        self.mass_min_add.setValidator(QDoubleValidator(0, 9999999, 1, self.mass_min_add))
        self.mass_max_add.setValidator(QDoubleValidator(0, 9999999, 1, self.mass_max_add))

        self.meet_add.setStyleSheet(self.style_edit)
        self.part_add.setStyleSheet(self.style_edit)
        self.process_add.setStyleSheet(self.style_edit)
        self.time_min_add.setStyleSheet(self.style_edit)
        self.time_max_add.setStyleSheet(self.style_edit)
        self.mass_max_add.setStyleSheet(self.style_edit)
        self.mass_min_add.setStyleSheet(self.style_edit)

        self.mass_max_add.setFixedSize(500, 30)
        self.mass_min_add.setFixedSize(500, 30)
        self.meet_add.setFixedSize(500, 30)
        self.part_add.setFixedSize(500, 30)
        self.process_add.setFixedSize(500, 30)
        self.time_min_add.setFixedSize(500, 30)
        self.time_max_add.setFixedSize(500, 30)

        self.meet_add.move(290, 95)
        self.part_add.move(290, 185)
        self.process_add.move(290, 140)
        self.time_min_add.move(290, 320)
        self.time_max_add.move(290, 365)
        self.mass_min_add.move(290, 230)
        self.mass_max_add.move(290, 275)

        self.add = QPushButton('Добавить данные', self)
        self.add.setStyleSheet(self.style)
        self.add.clicked.connect(self.button)
        self.add.setFixedSize(200, 35)
        self.add.move(288, 410)

        self.clear = QPushButton('Очистить', self)
        self.clear.setStyleSheet(self.style)
        self.clear.clicked.connect(self.clear_btn)
        self.clear.setFixedSize(150, 35)
        self.clear.move(510, 410)

        self.back = QPushButton('Назад', self)
        self.back.setStyleSheet(self.style)
        #self.back.clicked.connect(self.MeetWindow)
        self.back.setFixedSize(100, 35)
        self.back.move(680, 410)

        self.false_0 = QLabel('', self)
        self.false_0.setStyleSheet(self.style_1)
        self.false_0.setFixedSize(30, 30)
        self.false_0.move(770, 98)

        self.false_1 = QLabel('', self)
        self.false_1.setStyleSheet(self.style_1)
        self.false_1.setFixedSize(30, 30)
        self.false_1.move(770, 143)

        self.false_2 = QLabel('', self)
        self.false_2.setStyleSheet(self.style_1)
        self.false_2.setFixedSize(30, 30)
        self.false_2.move(770, 188)

        self.false_3 = QLabel('', self)
        self.false_3.setStyleSheet(self.style_1)
        self.false_3.setFixedSize(30, 30)
        self.false_3.move(770, 233)

        self.false_4 = QLabel('', self)
        self.false_4.setStyleSheet(self.style_1)
        self.false_4.setFixedSize(30, 30)
        self.false_4.move(770, 278)

        self.false_5 = QLabel('', self)
        self.false_5.setStyleSheet(self.style_1)
        self.false_5.setFixedSize(30, 30)
        self.false_5.move(770, 323)

        self.false_6 = QLabel('', self)
        self.false_6.setStyleSheet(self.style_1)
        self.false_6.setFixedSize(30, 30)
        self.false_6.move(770, 368)

        self.setFixedSize(800, 460)
        self.center()
        self.setWindowIcon(QIcon('meet.jpg'))
        self.setWindowTitle('Добавление данных в раздел с мясом')
        self.show()

    #def MeetWindow(self):
        #self.meet_window = MeetWindow()
        #self.meet_window.show()
        #self.close()

    def clear_btn(self):
        self.meet_add.clear()
        self.process_add.clear()
        self.part_add.clear()
        self.mass_min_add.clear()
        self.mass_max_add.clear()
        self.time_min_add.clear()
        self.time_max_add.clear()
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')

    def button(self):
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')
        add = (self.meet_add.text(), self.process_add.text(), self.part_add.text(), self.mass_min_add.text(),  self.mass_max_add.text(), self.time_min_add.text(), self.time_max_add.text(), 3, 4)
        if '' in add or 'e' in add:
            e = -1
            for i in add:
                e += 1
                print('1')
                if e == 0 and i == '':
                    self.false_0.setText('*')
                elif e == 1 and i == '':
                    self.false_1.setText('*')
                elif e == 2 and i == '':
                    self.false_2.setText('*')
                elif (e == 3 and i == '') or (e == 3 and i == 'e'):
                    self.false_3.setText('*')
                elif (e == 4 and i == '') or (e == 4 and i == 'e'):
                    self.false_4.setText('*')
                elif (e == 5 and i == '') or (e == 5 and i == 'e'):
                    self.false_5.setText('*')
                elif (e == 6 and i == '') or (e == 6 and i == 'e'):
                    self.false_6.setText('*')
                elif e == 7 and add[3] != '' and add[4] != '' and add[3] != 'e' and add[4] != 'e':
                    if float(add[3]) > float(add[4]):
                        self.false_3.setText('*')
                        self.false_4.setText('*')
                elif e == 8 and add[5] != '' and add[6] != '' and add[5] != 'e' and add[6] != 'e':
                    if float(add[5]) > float(add[6]):
                        self.false_5.setText('*')
                        self.false_6.setText('*')
        else:
            if float(add[3]) > float(add[4]) or float(add[5]) > float(add[6]):
                for i in range(2):
                    if float(add[3]) > float(add[4]) and i == 0:
                        self.false_3.setText('*')
                        self.false_4.setText('*')
                    elif float(add[5]) > float(add[6]) and i == 1:
                        self.false_5.setText('*')
                        self.false_6.setText('*')
            else:
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute("INSERT INTO tab_meet_finish "
                "(meet, process, part, mass_4_min, mass_4_max, time_4_min, time_4_max)"
                " VALUES (?, ?, ?, ?, ?, ?, ?)", (self.meet_add.text(), self.process_add.text(), self.part_add.text(), self.mass_min_add.text(),  self.mass_max_add.text(), self.time_min_add.text(), self.time_max_add.text(), ))
                conn.commit()
                c.close()
                conn.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())