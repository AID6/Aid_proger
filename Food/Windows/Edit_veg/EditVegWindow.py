import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class EditVegClass(QWidget):

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
                                  'После этого заполните соотвествующие строки во второй рамке обновленными данными.', self)
        self.information.setStyleSheet(self.style_edit)
        self.information.move(10, 10)

        self.veg_label = QLabel('Какой фрукт или овощь: ', self)
        self.process_label = QLabel('Какой процесс обработки: ', self)
        self.state_label = QLabel('Состояние продукта: ', self)
        self.time_min_label = QLabel('Минимальное время в минутах: ', self)
        self.time_max_label = QLabel('Максимальное время в минутах: ', self)
        self.state_process_label = QLabel('Готовить до появлени: ', self)

        self.veg_label.move(10, 95)
        self.process_label.move(10, 140)
        self.state_label.move(10, 185)
        self.time_min_label.move(10, 233434)
        self.time_max_label.move(10, 45454)
        self.state_process_label.move(10, 230448)

        self.veg_label.setStyleSheet(self.style_btn)
        self.process_label.setStyleSheet(self.style_btn)
        self.state_label.setStyleSheet(self.style_btn)
        self.time_min_label.setStyleSheet(self.style_btn)
        self.time_max_label.setStyleSheet(self.style_btn)
        self.state_process_label.setStyleSheet(self.style_btn)

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT veg FROM tab_veg")
        data_veg = c.fetchall()
        c.close()
        conn.close()
        self.veg = []
        for i in data_veg:
            if not i in self.veg:
                self.veg.append(i)
            else:
                continue
        self.veg.sort()

        self.combo_veg = QComboBox(self)
        self.combo_veg.addItem('Какой фрукт или овощ вы хотите выбрать?')
        self.combo_veg.addItems([i[0] for i in self.veg])
        self.combo_veg.move(300, 95)
        self.combo_veg.setFixedSize(400, 30)
        self.combo_veg.setStyleSheet(self.style_edit)
        self.combo_veg.activated.connect(self.data_process)

        self.combo_process = QComboBox(self)
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.combo_process.move(300, 140)
        self.combo_process.setFixedSize(400, 30)
        self.combo_process.setStyleSheet(self.style_edit)
        self.combo_process.activated.connect(self.data_state)

        self.combo_state = QComboBox(self)
        self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
        self.combo_state.move(300, 185)
        self.combo_state.setFixedSize(400, 30)
        self.combo_state.setStyleSheet(self.style_edit)
        self.combo_state.activated.connect(self.data_output)

        self.time_min_label_output = QLabel('', self)
        self.time_max_label_output = QLabel('', self)
        self.state_process_label_output = QLabel('', self)

        self.time_min_label_output.setStyleSheet(self.style_dl)
        self.time_max_label_output.setStyleSheet(self.style_dl)
        self.state_process_label_output.setStyleSheet(self.style_dl)

        self.time_min_label_output.setFixedSize(100, 30)
        self.time_max_label_output.setFixedSize(100, 30)
        self.state_process_label_output.setFixedSize(400, 35)

        self.time_min_label_output.move(300, 320324)
        self.time_max_label_output.move(300, 365234)
        self.state_process_label_output.move(300, 320234)

        self.min_1 = QLabel('мин', self)
        self.min_2 = QLabel('мин', self)

        self.min_1.setStyleSheet(self.style_edit)
        self.min_2.setStyleSheet(self.style_edit)

        self.min_1.move(410, 32566)
        self.min_2.move(410, 37076)

        self.veg_edit = QLineEdit('', self)
        self.process_edit = QLineEdit('', self)
        self.state_edit = QLineEdit('', self)
        self.time_min_edit = QLineEdit('', self)
        self.time_max_edit = QLineEdit('', self)
        self.state_process_edit = QLineEdit('', self)

        self.veg_edit.setStyleSheet(self.style_edit)
        self.process_edit.setStyleSheet(self.style_edit)
        self.state_edit.setStyleSheet(self.style_edit)
        self.time_min_edit.setStyleSheet(self.style_edit)
        self.time_max_edit.setStyleSheet(self.style_edit)
        self.state_process_edit.setStyleSheet(self.style_edit)

        self.veg_edit.setFixedSize(580, 35)
        self.process_edit.setFixedSize(580, 35)
        self.state_edit.setFixedSize(580, 35)
        self.time_min_edit.setFixedSize(200, 35)
        self.time_max_edit.setFixedSize(200, 35)
        self.state_process_edit.setFixedSize(580, 35)


        self.veg_edit.move(740, 95)
        self.process_edit.move(740, 140)
        self.state_edit.move(740, 185)
        self.time_min_edit.move(740, 230232)
        self.time_max_edit.move(740, 275232)
        self.state_process_edit.move(740, 2303232)

        self.time_min_edit.setValidator(QDoubleValidator(0, 9999999, 1, self.time_min_edit))
        self.time_max_edit.setValidator(QDoubleValidator(0, 9999999, 1, self.time_max_edit))

        self.min_3 = QLabel('мин', self)
        self.min_4 = QLabel('мин', self)

        self.min_3.setStyleSheet(self.style_edit)
        self.min_4.setStyleSheet(self.style_edit)

        self.min_3.move(950, 2352323)
        self.min_4.move(950, 2802323)

        self.back = QPushButton('Назад', self)
        self.back.setStyleSheet(self.style)
        self.back.clicked.connect(self.MeetWindow)
        self.back.setFixedSize(100, 35)
        self.back.move(1210, 330)

        self.edit = QPushButton('Изменить', self)
        self.edit.setStyleSheet(self.style)
        self.edit.setFixedSize(150, 35)
        self.edit.move(870, 330)
        self.edit.clicked.connect(self.data_edit)

        self.clear = QPushButton('Очистить', self)
        self.clear.setStyleSheet(self.style)
        self.clear.clicked.connect(self.clear_btn)
        self.clear.setFixedSize(150, 35)
        self.clear.move(1040, 330)

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
        self.false_8.move(1290, 235)

        self.setFixedSize(1330, 380)
        self.center()
        self.setWindowIcon(QIcon('veg.jpg'))
        self.setWindowTitle('Изменение данных в раздел с фруктами и овощами')
        self.show()

    def clear_btn(self):
        self.time_min_label_output.move(12323, 2323)
        self.time_max_label_output.move(31232, 21323)
        self.min_1.move(2323, 21323)
        self.min_2.move(2133123, 2321323)
        self.time_min_label.move(23232, 213232)
        self.time_max_label.move(23232, 213232)
        self.time_min_edit.move(740, 23034324)
        self.time_max_edit.move(740, 2753243)
        self.state_process_edit.move(7402343, 2302343)
        self.state_process_label_output.move(3002323, 23032)
        self.min_3.move(950, 23534)
        self.min_4.move(950, 280234)
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')
        self.false_7.setText('')
        self.false_8.setText('')
        self.combo_veg.clear()
        self.combo_process.clear()
        self.combo_state.clear()
        self.combo_veg.addItem('Какой фрукт или овощ вы хотите выбрать?')
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
        self.state_process_label.move(2132, 213233)
        self.veg_edit.clear()
        self.process_edit.clear()
        self.state_edit.clear()
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT veg FROM tab_veg")
        data_veg = c.fetchall()
        c.close()
        conn.close()
        self.veg = []
        for i in data_veg:
            if not i in self.veg:
                self.veg.append(i)
            else:
                continue
        self.veg.sort()
        self.combo_veg.addItems([i[0] for i in self.veg])

    def MeetWindow(self):
        self.veg_window = VegWindowClass()
        self.veg_window.show()
        self.close()

    def data_process(self):
        self.time_min_label_output.move(12323, 2323)
        self.time_max_label_output.move(31232, 21323)
        self.min_1.move(2323, 21323)
        self.min_2.move(2133123, 2321323)
        self.time_min_label.move(23232, 213232)
        self.time_max_label.move(23232, 213232)
        self.time_min_edit.move(740, 23034324)
        self.time_max_edit.move(740, 2753243)
        self.time_min_edit.clear()
        self.time_max_edit.clear()
        self.state_process_edit.clear()
        self.time_min_label_output.clear()
        self.time_max_label_output.clear()
        self.state_process_label_output.clear()
        self.state_process_edit.move(7402343, 2302343)
        self.state_process_label_output.move(3002323, 23032)
        self.state_process_label.move(1232, 123213)
        self.min_3.move(950, 23534)
        self.min_4.move(950, 280234)
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')
        self.false_7.setText('')
        self.false_8.setText('')
        self.combo_state.clear()
        self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
        self.combo_process.clear()
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.veg_edit.clear()
        self.process_edit.clear()
        self.state_edit.clear()
        if self.combo_veg.currentText() == 'Какой фрукт или овощ вы хотите выбрать?':
            self.false_0.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("SELECT process FROM tab_veg WHERE veg == ?",
                      (self.combo_veg.currentText(),))
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

    def data_state(self):
        self.time_min_label.move(123, 12323)
        self.time_max_label.move(2323,213213)
        self.time_min_label_output.move(12323, 2323)
        self.time_max_label_output.move(31232, 21323)
        self.min_1.move(2323, 21323)
        self.min_2.move(2133123, 2321323)
        self.time_min_edit.move(740, 23034324)
        self.time_max_edit.move(740, 2753243)
        self.time_min_edit.clear()
        self.time_max_edit.clear()
        self.state_process_edit.clear()
        self.time_min_label_output.clear()
        self.time_max_label_output.clear()
        self.state_process_label_output.clear()
        self.state_process_edit.move(7402343, 2302343)
        self.state_process_label_output.move(3002323, 23032)
        self.state_process_label.move(1232, 123213)
        self.min_3.move(950, 23534)
        self.min_4.move(950, 280234)
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')
        self.false_7.setText('')
        self.false_8.setText('')
        self.combo_state.clear()
        self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
        self.veg_edit.clear()
        self.process_edit.clear()
        self.state_edit.clear()
        if self.combo_process.currentText() == 'Какой вид обработки вы выбираете?':
            self.false_1.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("SELECT state FROM tab_veg WHERE veg == ? and process == ?",
                      (self.combo_veg.currentText(), self.combo_process.currentText(),))
            data_state = c.fetchall()
            c.close()
            conn.close()
            self.state = []
            for i in data_state:
                if not i in self.state:
                    self.state.append(i)
                else:
                    continue
            self.state.sort()
            self.combo_state.addItems([i[0] for i in self.state])
        self.time_min_label.move(23232, 213232)
        self.time_max_label.move(23232, 213232)
        self.time_min_label_output.move(12323, 2323)
        self.time_max_label_output.move(31232, 21323)
        self.min_1.move(2323, 21323)
        self.min_2.move(2133123, 2321323)
        self.time_min_edit.move(740, 23034324)
        self.time_max_edit.move(740, 2753243)
        self.state_process_edit.move(7402343, 2302343)
        self.state_process_label_output.move(3002323, 23032)
        self.min_3.move(950, 23534)
        self.min_4.move(950, 280234)

    def data_output(self):
        self.time_min_label.move(23232, 213232)
        self.time_max_label.move(23232, 213232)
        self.time_min_label_output.move(12323, 2323)
        self.time_max_label_output.move(31232, 21323)
        self.min_1.move(2323, 21323)
        self.min_2.move(2133123, 2321323)
        self.time_min_edit.move(740, 23034324)
        self.time_max_edit.move(740, 2753243)
        self.time_min_edit.clear()
        self.time_max_edit.clear()
        self.state_process_edit.clear()
        self.time_min_label_output.clear()
        self.time_max_label_output.clear()
        self.state_process_label_output.clear()
        self.state_process_edit.move(7402343, 2302343)
        self.state_process_label_output.move(3002323, 23032)
        self.state_process_label.move(1232, 123213)
        self.min_3.move(950, 23534)
        self.min_4.move(950, 280234)
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.false_6.setText('')
        self.false_7.setText('')
        self.false_8.setText('')
        self.veg_edit.clear()
        self.process_edit.clear()
        self.state_edit.clear()
        if self.combo_state.currentText() == 'В каком виде вы хотите приготовить продукт?':
            self.false_2.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute(
                "SELECT time_min, time_max, state_process FROM tab_veg WHERE veg == ? and process == ? and state == ?",
                (self.combo_veg.currentText(), self.combo_process.currentText(), self.combo_state.currentText(),))
            data_mass = c.fetchall()
            c.close()
            conn.close()
            if data_mass[0][0] == None:
                self.state_process_label.move(10, 230)
                self.state_process_label_output.setText(' ' + data_mass[0][2])
                self.state_process_label_output.move(300, 230)
                self.state_process_edit.move(740, 230)
            else:
                self.time_min_label_output.move(300, 230)
                self.time_max_label_output.move(300, 275)
                self.time_min_label_output.setText(' ' + str(data_mass[0][0]))
                self.time_max_label_output.setText(' ' + str(data_mass[0][1]))
                self.time_min_label.move(10, 230)
                self.time_max_label.move(10, 275)
                self.min_1.move(410, 230)
                self.min_2.move(410, 275)
                self.time_min_edit.move(740, 230)
                self.time_max_edit.move(740, 275)
                self.min_3.move(950, 235)
                self.min_4.move(950, 280)

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
        edit = (self.combo_veg.currentText(), self.combo_process.currentText(), self.combo_state.currentText(), self.veg_edit.text(), self.process_edit.text(),
                self.state_edit.text(), self.time_min_edit.text(), self.time_max_edit.text(), self.state_process_edit.text(), self.state_process_label_output.text(), self.time_min_label_output.text())
        if (edit[0] == 'Какой фрукт или овощ вы хотите выбрать?') or (edit[1] == 'Какой вид обработки вы выбираете?') or \
                (edit[2] == 'В каком виде вы хотите приготовить продукт?') or ('' in edit[3:6]) or ('' in edit[6:8] and edit[9] == '') or \
                ('e' in edit[6:8] and edit[10] != '') or (edit[8] == '' and edit[9] != ''):
            e = -1
            for i in edit:
                e += 1
                if e == 0 and i == 'Какой фрукт или овощ вы хотите выбрать?':
                    self.false_0.setText('*')
                elif e == 1 and i == 'Какой вид обработки вы выбираете?':
                    self.false_1.setText('*')
                elif e == 2 and i == 'В каком виде вы хотите приготовить продукт?':
                    self.false_2.setText('*')
                elif e == 3 and i == '':
                    self.false_3.setText('*')
                elif e == 4 and i == '':
                    self.false_4.setText('*')
                elif e == 5 and i == '':
                    self.false_5.setText('*')
                elif e == 6 and edit[9] != '':
                    if edit[8] == '':
                        self.false_8.setText('*')
                elif e == 7 and self.time_min_label_output.text() != '':
                    if (edit[6] == '') or (edit[7] == '') or ('e' in edit[6]) or ('e' in edit[7]):
                        for j in range(2):
                            if (j == 0 and edit[6] == '') or (j == 0 and 'e' in edit[6]):
                                self.false_6.setText('*')
                            elif (j == 1 and edit[7] == '') or (j == 1 and 'e' in edit[7]):
                                self.false_7.setText('*')
                    elif float(edit[6]) > float(edit[7]):
                        self.false_6.setText('*')
                        self.false_7.setText('*')
        else:
            if edit[10] != '':
                if float(edit[6]) > float(edit[7]):
                    self.false_6.setText('*')
                    self.false_7.setText('*')
                else:
                    conn = sqlite3.connect('data.db')
                    c = conn.cursor()
                    c.execute(
                        "UPDATE tab_veg SET veg == ?, process == ?, state == ?, time_min == ?, time_max == ? WHERE veg == ? and process == ? and state == ?",
                        (edit[3], edit[4], edit[5], edit[6], edit[7], edit[0], edit[1], edit[2],))
                    conn.commit()
                    c.close()
                    conn.close()
                    self.combo_veg.clear()
                    self.combo_process.clear()
                    self.combo_state.clear()
                    self.combo_veg.addItem('Какой фрукт или овощ вы хотите выбрать?')
                    self.combo_process.addItem('Какой вид обработки вы выбираете?')
                    self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
                    self.time_min_label.move(23232, 213232)
                    self.time_max_label.move(23232, 213232)
                    self.time_min_label_output.move(12323, 2323)
                    self.time_max_label_output.move(31232, 21323)
                    self.min_1.move(2323, 21323)
                    self.min_2.move(2133123, 2321323)
                    self.state_process_label.move(1232, 123213)
                    self.state_process_label_output.move(3002323, 23032)
                    conn = sqlite3.connect('data.db')
                    c = conn.cursor()
                    c.execute("SELECT veg FROM tab_veg")
                    data_veg = c.fetchall()
                    c.close()
                    conn.close()
                    self.veg = []
                    for i in data_veg:
                        if not i in self.veg:
                            self.veg.append(i)
                        else:
                            continue
                    self.veg.sort()
                    self.combo_veg.addItems([i[0] for i in self.veg])
            else:
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute("UPDATE tab_veg SET veg == ?, process == ?, state == ?, state_process == ? WHERE veg == ? and process == ? and state == ?",
                    (edit[3], edit[4], edit[5], edit[8], edit[0], edit[1], edit[2], ))
                conn.commit()
                c.close()
                conn.close()
                self.combo_veg.clear()
                self.combo_process.clear()
                self.combo_state.clear()
                self.combo_veg.addItem('Какой фрукт или овощ вы хотите выбрать?')
                self.combo_process.addItem('Какой вид обработки вы выбираете?')
                self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
                self.time_min_label.move(23232, 213232)
                self.time_max_label.move(23232, 213232)
                self.time_min_label_output.move(12323, 2323)
                self.time_max_label_output.move(31232, 21323)
                self.min_1.move(2323, 21323)
                self.min_2.move(2133123, 2321323)
                self.state_process_label.move(1232, 123213)
                self.state_process_label_output.move(3002323, 23032)
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute("SELECT veg FROM tab_veg")
                data_veg = c.fetchall()
                c.close()
                conn.close()
                self.veg = []
                for i in data_veg:
                    if not i in self.veg:
                        self.veg.append(i)
                    else:
                        continue
                self.veg.sort()
                self.combo_veg.addItems([i[0] for i in self.veg])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
