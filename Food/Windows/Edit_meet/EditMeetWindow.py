import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class EditMeetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style = 'font-size:20px;color:green'
        self.style_2 = 'font-size:10px;color:red;border-radius: 10px'
        self.style_edit = 'font-size:17px;color:black;border-radius: 10px'
        self.style_btn = 'font-size:17px;color:green'
        self.style_dl = 'border: 3px solid black;font-size: 16px;background-color:rgba(255, 255, 255, 0,5);'
        self.style_1 = 'font-size:30px;color:red'

        self.information = QLabel('Чтобы изменить данные, вам следует выбрать нынишние данные в первой рамке. '
                                  'После этого заполните строки во второй рамке обновленными данными.', self)
        self.information.setStyleSheet(self.style_edit)
        self.information.move(10, 10)

        self.meet_label = QLabel('Из какого мясо продукт: ', self)
        self.process_label = QLabel('Какой процесс обработки: ', self)
        self.part_label = QLabel('Название продутк: ', self)
        self.time_min_label = QLabel('Минимальное время в минутах: ', self)
        self.time_max_label = QLabel('Максимальное время в минутах: ', self)
        self.mass_min_label = QLabel('Минимальные граммовки n порций: ', self)
        self.mass_max_label = QLabel('Максимальные граммовки n порций: ', self)

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

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT meet FROM tab_meet_finish")
        data_meet = c.fetchall()
        c.close()
        conn.close()
        self.meet = []
        for i in data_meet:
            if not i in self.meet:
                self.meet.append(i)
            else:
                continue
        self.meet.sort()

        self.combo_meet = QComboBox(self)
        self.combo_meet.addItem('Из какого мяса продукт?')
        self.combo_meet.addItems([i[0] for i in self.meet])
        self.combo_meet.move(300, 95)
        self.combo_meet.setFixedSize(400, 30)
        self.combo_meet.setStyleSheet(self.style_edit)
        self.combo_meet.activated.connect(self.data_process)

        self.combo_process = QComboBox(self)
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.combo_process.move(300, 140)
        self.combo_process.setFixedSize(400, 30)
        self.combo_process.setStyleSheet(self.style_edit)
        self.combo_process.activated.connect(self.data_part)

        self.combo_part = QComboBox(self)
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
        self.combo_part.move(300, 185)
        self.combo_part.setFixedSize(400, 30)
        self.combo_part.setStyleSheet(self.style_edit)
        self.combo_part.activated.connect(self.data_output)

        self.mass_min_label = QLabel('', self)
        self.mass_max_label = QLabel('', self)
        self.time_min_label = QLabel('', self)
        self.time_max_label = QLabel('', self)

        self.mass_min_label.setStyleSheet(self.style_dl)
        self.mass_max_label.setStyleSheet(self.style_dl)
        self.time_min_label.setStyleSheet(self.style_dl)
        self.time_max_label.setStyleSheet(self.style_dl)

        self.mass_min_label.setFixedSize(100, 30)
        self.mass_max_label.setFixedSize(100, 30)
        self.time_min_label.setFixedSize(100, 30)
        self.time_max_label.setFixedSize(100, 30)

        self.mass_min_label.move(300, 230)
        self.mass_max_label.move(300, 275)
        self.time_min_label.move(300, 320)
        self.time_max_label.move(300, 365)

        self.gr_1 = QLabel('гр', self)
        self.gr_1_1 = QLabel('гр', self)
        self.min_1 = QLabel('мин', self)
        self.min_1_1 = QLabel('мин', self)

        self.gr_1.setStyleSheet(self.style_edit)
        self.gr_1_1.setStyleSheet(self.style_edit)
        self.min_1.setStyleSheet(self.style_edit)
        self.min_1_1.setStyleSheet(self.style_edit)

        self.gr_1.move(410, 235)
        self.gr_1_1.move(410, 280)
        self.min_1.move(410, 325)
        self.min_1_1.move(410, 370)

        self.meet_edit = QLineEdit('', self)
        self.process_edit = QLineEdit('', self)
        self.part_edit = QLineEdit('', self)
        self.mass_min_edit = QLineEdit('', self)
        self.mass_max_edit = QLineEdit('', self)
        self.time_min_edit = QLineEdit('', self)
        self.time_max_edit = QLineEdit('', self)

        self.meet_edit.setStyleSheet(self.style_edit)
        self.process_edit.setStyleSheet(self.style_edit)
        self.part_edit.setStyleSheet(self.style_edit)
        self.mass_min_edit.setStyleSheet(self.style_edit)
        self.mass_max_edit.setStyleSheet(self.style_edit)
        self.time_min_edit.setStyleSheet(self.style_edit)
        self.time_max_edit.setStyleSheet(self.style_edit)

        self.meet_edit.setFixedSize(580, 35)
        self.process_edit.setFixedSize(580, 35)
        self.part_edit.setFixedSize(580, 35)
        self.mass_min_edit.setFixedSize(200, 35)
        self.mass_max_edit.setFixedSize(200, 35)
        self.time_min_edit.setFixedSize(200, 35)
        self.time_max_edit.setFixedSize(200, 35)

        self.meet_edit.move(740, 95)
        self.process_edit.move(740, 140)
        self.part_edit.move(740, 185)
        self.mass_min_edit.move(740, 230)
        self.mass_max_edit.move(740, 275)
        self.time_min_edit.move(740, 320)
        self.time_max_edit.move(740, 365)

        self.time_min_edit.setValidator(QDoubleValidator(0, 9999999, 1, self.time_min_edit))
        self.time_max_edit.setValidator(QDoubleValidator(0, 9999999, 1, self.time_max_edit))
        self.mass_min_edit.setValidator(QDoubleValidator(0, 9999999, 1, self.mass_min_edit))
        self.mass_max_edit.setValidator(QDoubleValidator(0, 9999999, 1, self.mass_max_edit))

        self.gr_2 = QLabel('гр', self)
        self.gr_2_1 = QLabel('гр', self)
        self.min_2 = QLabel('мин', self)
        self.min_2_1 = QLabel('мин', self)

        self.gr_2.setStyleSheet(self.style_edit)
        self.gr_2_1.setStyleSheet(self.style_edit)
        self.min_2.setStyleSheet(self.style_edit)
        self.min_2_1.setStyleSheet(self.style_edit)

        self.gr_2.move(950, 235)
        self.gr_2_1.move(950, 280)
        self.min_2.move(950, 325)
        self.min_2_1.move(950, 370)

        self.back = QPushButton('Назад', self)
        self.back.setStyleSheet(self.style)
        self.back.clicked.connect(self.MeetWindow)
        self.back.setFixedSize(100, 35)
        self.back.move(1210, 410)

        self.edit = QPushButton('Изменить', self)
        self.edit.setStyleSheet(self.style)
        self.edit.setFixedSize(150, 35)
        self.edit.move(870, 410)
        self.edit.clicked.connect(self.data_edit)

        self.clear = QPushButton('Очистить', self)
        self.clear.setStyleSheet(self.style)
        self.clear.clicked.connect(self.clear_btn)
        self.clear.setFixedSize(150, 35)
        self.clear.move(1040, 410)

        self.false_0 = QLabel('', self)
        self.false_0.setStyleSheet(self.style_1)
        self.false_0.setFixedSize(30, 30)
        self.false_0.move(703, 100)

        self.false_1 = QLabel('', self)
        self.false_1.setStyleSheet(self.style_1)
        self.false_1.setFixedSize(30, 30)
        self.false_1.move(703, 145)

        self.false_2 = QLabel('', self)
        self.false_2.setStyleSheet(self.style_1)
        self.false_2.setFixedSize(30, 30)
        self.false_2.move(703, 190)

        self.false_3 = QLabel('', self)
        self.false_3.setStyleSheet(self.style_1)
        self.false_3.setFixedSize(30, 30)
        self.false_3.move(1290, 100)

        self.false_4 = QLabel('', self)
        self.false_4.setStyleSheet(self.style_1)
        self.false_4.setFixedSize(30, 30)
        self.false_4.move(1290, 145)

        self.false_5 = QLabel('', self)
        self.false_5.setStyleSheet(self.style_1)
        self.false_5.setFixedSize(30, 30)
        self.false_5.move(1290, 190)

        self.false_6 = QLabel('', self)
        self.false_6.setStyleSheet(self.style_1)
        self.false_6.setFixedSize(30, 30)
        self.false_6.move(915, 235)

        self.false_7 = QLabel('', self)
        self.false_7.setStyleSheet(self.style_1)
        self.false_7.setFixedSize(30, 30)
        self.false_7.move(915, 280)

        self.false_8 = QLabel('', self)
        self.false_8.setStyleSheet(self.style_1)
        self.false_8.setFixedSize(30, 30)
        self.false_8.move(915, 325)

        self.false_9 = QLabel('', self)
        self.false_9.setStyleSheet(self.style_1)
        self.false_9.setFixedSize(30, 30)
        self.false_9.move(915, 370)

        self.setFixedSize(1330, 460)
        self.center()
        self.setWindowIcon(QIcon('meet.jpg'))
        self.setWindowTitle('Изменение данных в раздел с мясом')
        self.show()

    def clear_btn(self):
        self.meet_edit.clear()
        self.process_edit.clear()
        self.part_edit.clear()
        self.mass_min_edit.clear()
        self.mass_max_edit.clear()
        self.time_min_edit.clear()
        self.time_max_edit.clear()

    def MeetWindow(self):
        self.meet_window = MeetWindowClass()
        self.meet_window.show()
        self.close()

    def data_process(self):
        self.mass_min_label.setText('')
        self.mass_max_label.setText('')
        self.time_min_label.setText('')
        self.time_max_label.setText('')
        self.false_0.setText('')
        self.combo_part.clear()
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
        self.combo_process.clear()
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        if self.combo_meet.currentText() == 'Из какого мяса продукт?':
            self.false_0.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("SELECT process FROM tab_meet_finish WHERE meet == ?",
                      (self.combo_meet.currentText(),))
            data_process = c.fetchall()
            self.process = []
            for i in data_process:
                if not i in self.process:
                    self.process.append(i)
                else:
                    continue
            self.process.sort()
            self.combo_process.addItems([i[0] for i in self.process])
            c.close()
            conn.close()
        self.mass_min_label.setText('')
        self.mass_max_label.setText('')
        self.time_min_label.setText('')
        self.time_max_label.setText('')

    def data_part(self):
        self.mass_min_label.setText('')
        self.mass_max_label.setText('')
        self.time_min_label.setText('')
        self.time_max_label.setText('')
        self.false_1.setText('')
        self.combo_part.clear()
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
        if self.combo_process.currentText() == 'Какой вид обработки вы выбираете?':
            self.false_1.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("SELECT part FROM tab_meet_finish WHERE meet == ? and process == ?",
                      (self.combo_meet.currentText(), self.combo_process.currentText(), ))
            data_part = c.fetchall()
            c.close()
            conn.close()
            self.part = []
            for i in data_part:
                if not i in self.part:
                    self.part.append(i)
                else:
                    continue
            self.part.sort()
            self.combo_part.addItems([i[0] for i in self.part])
        self.mass_min_label.setText('')
        self.mass_max_label.setText('')
        self.time_min_label.setText('')
        self.time_max_label.setText('')

    def data_output(self):
        self.mass_min_label.setText('')
        self.mass_max_label.setText('')
        self.time_min_label.setText('')
        self.time_max_label.setText('')
        self.false_2.setText('')
        if self.combo_part.currentText() == 'Какой продукт вы хотите обработать?':
            self.false_2.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute(
                "SELECT mass_4_min, mass_4_max, time_4_min, time_4_max FROM tab_meet_finish WHERE meet == ? and process == ? and part == ?",
                (self.combo_meet.currentText(), self.combo_process.currentText(), self.combo_part.currentText(),))
            data_mass = c.fetchall()
            c.close()
            conn.close()
            self.mass_min_label.setText(' ' + str(data_mass[0][0]))
            self.mass_max_label.setText(' ' + str(data_mass[0][1]))
            self.time_min_label.setText(' ' + str(data_mass[0][2]))
            self.time_max_label.setText(' ' + str(data_mass[0][3]))

    def data_edit(self):
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')
        self.false_7.setText('')
        self.false_8.setText('')
        self.false_9.setText('')
        edit = (self.combo_meet.currentText(), self.combo_process.currentText(), self.combo_part.currentText(), self.meet_edit.text(), self.process_edit.text(),
                self.part_edit.text(), self.mass_min_edit.text(), self.mass_max_edit.text(), self.time_min_edit.text(), self.time_max_edit.text(), 4, 3)
        if (edit[2] == 'Какой продукт вы хотите обработать?') or ('' in edit[3:10]) or (edit[1] == 'Какой вид обработки вы выбираете?') or (edit[0] == 'Из какого мяса продукт?')\
                or ('e' in edit[6:10]):
            print('1')
            e = -1
            for i in edit:
                e += 1
                if e == 0 and i == 'Из какого мяса продукт?':
                    self.false_0.setText('*')
                elif e == 1 and i == 'Какой вид обработки вы выбираете?':
                    self.false_1.setText('*')
                elif e == 2 and i == 'Какой продукт вы хотите обработать?':
                    self.false_2.setText('*')
                elif e == 3 and i == '':
                    self.false_3.setText('*')
                elif e == 4 and i == '':
                    self.false_4.setText('*')
                elif e == 5 and i == '':
                    self.false_5.setText('*')
                elif (e == 6 and i == '') or (e == 6 and i == 'e'):
                    self.false_6.setText('*')
                elif (e == 7 and i == '') or (e == 7 and i == 'e'):
                    self.false_7.setText('*')
                elif (e == 8 and i == '') or (e == 8 and i == 'e'):
                    self.false_8.setText('*')
                elif (e == 9 and i == '') or (e == 9 and i == 'e'):
                    self.false_9.setText('*')
                elif e == 10 and edit[6] != '' and edit[7] != '' and edit[6] != 'e' and edit[7] != 'e':
                    if float(edit[6]) > float(edit[7]):
                        self.false_6.setText('*')
                        self.false_7.setText('*')
                elif e == 11 and edit[8] != '' and edit[9] != '' and edit[8] != 'e' and edit[9] != 'e':
                    if float(edit[8]) > float(edit[9]):
                        self.false_8.setText('*')
                        self.false_9.setText('*')
        else:
            print('2')
            if float(edit[6]) > float(edit[7]) or float(edit[8]) > float(edit[9]):
                for i in range(2):
                    if float(edit[6]) > float(edit[7]) and i == 0:
                        self.false_6.setText('*')
                        self.false_7.setText('*')
                    elif float(edit[8]) > float(edit[9]) and i == 1:
                        self.false_8.setText('*')
                        self.false_9.setText('*')
            else:
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute("UPDATE tab_meet_finish SET meet == ?, process == ?, part == ?, mass_4_min == ?, mass_4_max == ?, time_4_min == ?, time_4_max == ?  WHERE meet == ? and process == ? and part == ?",
                          (edit[3], edit[4], edit[5], edit[6], edit[7], edit[8], edit[9], edit[0], edit[1], edit[2], ))
                conn.commit()
                c.close()
                conn.close()
                self.combo_part.clear()
                self.combo_part.addItem('Какой продукт вы хотите обработать?')
                self.combo_process.clear()
                self.combo_process.addItem('Какой вид обработки вы выбираете?')
                self.combo_meet.clear()
                self.combo_meet.addItem('Из какого мяса продукт?')
                self.mass_min_label.setText('')
                self.mass_max_label.setText('')
                self.time_min_label.setText('')
                self.time_max_label.setText('')
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute("SELECT meet FROM tab_meet_finish")
                data_meet = c.fetchall()
                c.close()
                conn.close()
                self.meet = []
                for i in data_meet:
                    if not i in self.meet:
                        self.meet.append(i)
                    else:
                        continue
                self.meet.sort()
                self.combo_meet.addItems([i[0] for i in self.meet])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
