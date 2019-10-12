import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DeleteMeetClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style = 'font-size:17px;color:green'
        self.style_2 = 'font-size:10px;color:red;border-radius: 10px'
        self.style_edit = 'font-size:17px;color:black;border-radius: 10px'
        self.style_btn = 'font-size:17px;color:green'
        self.style_1 = 'font-size:30px;color:red'
        self.style_dl = 'border: 3px solid black;font-size: 16px;background-color:rgba(255, 255, 255, 0,5);'

        self.information = QLabel('Выберите те данные, которые хотите удалить из этой программы.', self)
        self.information.setStyleSheet(self.style_edit)
        self.information.move(10, 10)

        self.meet_label = QLabel('Из какого мясо продукт: ', self)
        self.process_label = QLabel('Какой процесс обработки: ', self)
        self.part_label = QLabel('Название продутк: ', self)
        self.time_min_label = QLabel('Минимальное время в минутах: ', self)
        self.time_max_label = QLabel('Максимальное время в минутах: ', self)
        self.mass_min_label = QLabel('Минимальные граммовки n порций: ', self)
        self.mass_max_label = QLabel('Максимальные граммовки n порций: ', self)

        self.meet_label.move(10, 65)
        self.process_label.move(10, 110)
        self.part_label.move(10, 155)
        self.time_min_label.move(10, 290)
        self.time_max_label.move(10, 335)
        self.mass_min_label.move(10, 200)
        self.mass_max_label.move(10, 245)

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
        self.combo_meet.move(300, 65)
        self.combo_meet.setFixedSize(400, 30)
        self.combo_meet.setStyleSheet(self.style_edit)
        self.combo_meet.activated.connect(self.data_process)

        self.combo_process = QComboBox(self)
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.combo_process.move(300, 110)
        self.combo_process.setFixedSize(400, 30)
        self.combo_process.setStyleSheet(self.style_edit)
        self.combo_process.activated.connect(self.data_part)

        self.combo_part = QComboBox(self)
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
        self.combo_part.move(300, 155)
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

        self.mass_min_label.move(300, 200)
        self.mass_max_label.move(300, 245)
        self.time_min_label.move(300, 290)
        self.time_max_label.move(300, 335)

        self.gr_1 = QLabel('гр', self)
        self.gr_1_1 = QLabel('гр', self)
        self.min_1 = QLabel('мин', self)
        self.min_1_1 = QLabel('мин', self)

        self.gr_1.setStyleSheet(self.style_edit)
        self.gr_1_1.setStyleSheet(self.style_edit)
        self.min_1.setStyleSheet(self.style_edit)
        self.min_1_1.setStyleSheet(self.style_edit)

        self.gr_1.move(410, 205)
        self.gr_1_1.move(410, 250)
        self.min_1.move(410, 295)
        self.min_1_1.move(410, 340)

        self.delete = QPushButton('Удалить', self)
        self.delete.setStyleSheet(self.style)
        self.delete.clicked.connect(self.deleteMeet)
        self.delete.setFixedSize(120, 35)
        self.delete.move(285, 380)

        self.back = QPushButton('Назад', self)
        self.back.setStyleSheet(self.style)
        self.back.clicked.connect(self.MeetWindow)
        self.back.setFixedSize(100, 35)
        self.back.move(605, 380)

        self.clear = QPushButton('Очистить', self)
        self.clear.setStyleSheet(self.style)
        self.clear.clicked.connect(self.clear_btn)
        self.clear.setFixedSize(150, 35)
        self.clear.move(430, 380)

        self.false_0 = QLabel('', self)
        self.false_0.setStyleSheet(self.style_1)
        self.false_0.setFixedSize(30, 30)
        self.false_0.move(705, 70)

        self.false_1 = QLabel('', self)
        self.false_1.setStyleSheet(self.style_1)
        self.false_1.setFixedSize(30, 30)
        self.false_1.move(705, 115)

        self.false_2 = QLabel('', self)
        self.false_2.setStyleSheet(self.style_1)
        self.false_2.setFixedSize(30, 30)
        self.false_2.move(705, 160)

        self.setFixedSize(725, 430)
        self.center()
        self.setWindowIcon(QIcon('meet.jpg'))
        self.setWindowTitle('Удаление данных в разделе с мясом')
        self.show()

    def clear_btn(self):
        self.combo_meet.clear()
        self.combo_process.clear()
        self.combo_part.clear()
        self.combo_meet.addItem('Из какого мяса продукт?')
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
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
        self.mass_min_label.setText('')
        self.mass_max_label.setText('')
        self.time_min_label.setText('')
        self.time_max_label.setText('')


    def MeetWindow(self):
        self.meet_window = MeetWindowClass()
        self.meet_window.show()
        self.close()

    def deleteMeet(self):
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        delete = (self.combo_meet.currentText(), self.combo_process.currentText(), self.combo_part.currentText())
        if self.combo_part.currentText() == 'Какой продукт вы хотите обработать?' or self.combo_process.currentText() == 'Какой вид обработки вы выбираете?' or self.combo_meet.currentText() == 'Из какого мяса продукт?':
            e = -1
            for i in delete:
                e += 1
                if e == 0 and i == 'Из какого мяса продукт?':
                    self.false_0.setText('*')
                elif e == 1 and i == 'Какой вид обработки вы выбираете?':
                    self.false_1.setText('*')
                elif e == 2 and i == 'Какой продукт вы хотите обработать?':
                    self.false_2.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("DELETE FROM tab_meet_finish WHERE meet == ? and process == ? and part == ?",
                      (self.combo_meet.currentText(), self.combo_process.currentText(), self.combo_part.currentText(), ))
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

    def data_process(self):
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
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
        self.false_1.setText('')
        self.false_2.setText('')
        self.combo_part.clear()
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
        if self.combo_process.currentText() == 'Какой вид обработки вы выбираете?' or self.combo_meet.currentText() == 'Из какого мяса продукт?':
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