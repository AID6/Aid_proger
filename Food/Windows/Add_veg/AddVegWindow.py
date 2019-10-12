import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AddVegClass(QWidget):
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

        self.information = QLabel('Чтобы добавить данные, вам следует заполнить либо все строки \nдо предпоследней включительно(включительно), либо все строки не включая время.', self)
        self.information.setStyleSheet(self.style_edit)
        self.information.move(10,10)

        self.veg_label = QLabel('Введите овощ или фрукт:', self)
        self.process_label = QLabel('Вид обработки :', self)
        self.state_label = QLabel('Состояние овоща :', self)
        self.time_min_label = QLabel('Минимальное время обработки :', self)
        self.time_max_label = QLabel('Максимальное время обработки :', self)
        self.state_process_label = QLabel('Готовить до состояния :', self)

        self.veg_label.move(10, 72)
        self.process_label.move(10, 117)
        self.state_label.move(10, 162)
        self.time_min_label.move(10, 207)
        self.time_max_label.move(10, 252)
        self.state_process_label.move(10, 297)

        self.veg_label.setStyleSheet(self.style)
        self.state_label.setStyleSheet(self.style)
        self.process_label.setStyleSheet(self.style)
        self.time_min_label.setStyleSheet(self.style)
        self.time_max_label.setStyleSheet(self.style)
        self.state_process_label.setStyleSheet(self.style)

        self.veg_add = QLineEdit('', self)
        self.process_add = QLineEdit('', self)
        self.state_add = QLineEdit('', self)
        self.time_min_add = QLineEdit('', self)
        self.time_max_add = QLineEdit('', self)
        self.state_process_add = QLineEdit('', self)

        self.time_min_add.setValidator(QDoubleValidator(0, 9999999, 1, self.time_min_add))
        self.time_max_add.setValidator(QDoubleValidator(0, 9999999, 1, self.time_max_add))

        self.veg_add.setStyleSheet(self.style_edit)
        self.state_add.setStyleSheet(self.style_edit)
        self.process_add.setStyleSheet(self.style_edit)
        self.time_min_add.setStyleSheet(self.style_edit)
        self.time_max_add.setStyleSheet(self.style_edit)
        self.state_process_add.setStyleSheet(self.style_edit)

        self.veg_add.setFixedSize(450, 35)
        self.process_add.setFixedSize(450, 35)
        self.state_add.setFixedSize(450, 35)
        self.time_min_add.setFixedSize(450, 35)
        self.time_max_add.setFixedSize(450, 35)
        self.state_process_add.setFixedSize(450, 35)

        self.veg_add.move(280, 72)
        self.process_add.move(280, 117)
        self.state_add.move(280, 162)
        self.time_min_add.move(280, 207)
        self.time_max_add.move(280, 252)
        self.state_process_add.move(280, 297)

        self.clear = QPushButton('Очистить', self)
        self.clear.setStyleSheet(self.style)
        self.clear.clicked.connect(self.clear_btn)
        self.clear.setFixedSize(150, 35)
        self.clear.move(480, 370)

        self.add = QPushButton('Добавить данные', self)
        self.add.setStyleSheet(self.style)
        self.add.clicked.connect(self.add_data)
        self.add.setFixedSize(200, 35)
        self.add.move(260, 370)

        self.back = QPushButton('Назад', self)
        self.back.setStyleSheet(self.style)
        self.back.clicked.connect(self.VegWindow_fun)
        self.back.setFixedSize(100, 35)
        self.back.move(645, 370)

        self.false_0 = QLabel('', self)
        self.false_0.setStyleSheet(self.style_1)
        self.false_0.setFixedSize(30, 30)
        self.false_0.move(735, 77)

        self.false_1 = QLabel('', self)
        self.false_1.setStyleSheet(self.style_1)
        self.false_1.setFixedSize(30, 30)
        self.false_1.move(735, 122)

        self.false_2 = QLabel('', self)
        self.false_2.setStyleSheet(self.style_1)
        self.false_2.setFixedSize(30, 30)
        self.false_2.move(735, 167)

        self.false_3 = QLabel('', self)
        self.false_3.setStyleSheet(self.style_1)
        self.false_3.setFixedSize(30, 30)
        self.false_3.move(735, 212)

        self.false_4 = QLabel('', self)
        self.false_4.setStyleSheet(self.style_1)
        self.false_4.setFixedSize(30, 30)
        self.false_4.move(735, 257)

        self.false_5 = QLabel('', self)
        self.false_5.setStyleSheet(self.style_1)
        self.false_5.setFixedSize(30, 30)
        self.false_5.move(735, 302)

        self.setFixedSize(760, 420)
        self.center()
        self.setWindowIcon(QIcon('veg.jpg'))
        self.setWindowTitle('Добавление данных в раздел фруктов и овощей')
        self.show()

    def clear_btn(self):
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        self.veg_add.clear()
        self.process_add.clear()
        self.state_add.clear()
        self.time_min_add.clear()
        self.time_max_add.clear()
        self.state_process_add.clear()

    def VegWindow_fun(self):
        self.veg_window = VegWindowClass()
        self.veg_window.show()
        self.close()

    def add_data(self):
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.false_4.setText('')
        self.false_5.setText('')
        add = (self.veg_add.text(), self.process_add.text(), self.state_add.text(), self.time_min_add.text(), self.time_max_add.text(), self.state_process_add.text(), 3, 2, 1, 1, 1)
        if ('' in add[0:3]) or ('' in add[3:5] and add[5] == '') or ('' not in add[3:5] and add[5] != '') or ('e' in add[3:5]):
            print('1')
            e = -1
            for i in add:
                e += 1
                if e == 0 and i == '':
                    self.false_0.setText('*')
                elif e == 1 and i == '':
                    self.false_1.setText('*')
                elif e == 2 and i == '':
                    self.false_2.setText('*')
                elif (e == 3 and add[5] == '' and add[3] != '' and add[4] == '') or (e == 3 and 'e' in add[4]):
                    self.false_4.setText('*')
                elif (e == 4 and add[5] == '' and add[3] == '' and add[4] != '') or (e == 4 and 'e' in add[3]):
                    self.false_3.setText('*')
                elif e == 6 and 'e' in add[3]:
                    self.false_3.setText('*')
                elif e == 10 and 'e' in add[4]:
                    self.false_4.setText('*')
                elif e == 7 and add[3] != '' and add[4] != '' and 'e' not in add[3] and 'e' not in add[4]:
                    if float(add[3]) > float(add[4]):
                        self.false_3.setText('*')
                        self.false_4.setText('*')
                elif e == 8 and add[3] != '' and add[5] != '':
                    self.false_5.setText('*')
                    self.false_3.setText('*')
                elif e == 9 and add[5] != '' and add[4] != '':
                    self.false_5.setText('*')
                    self.false_4.setText('*')
                elif (e == 5 and add[5] != '' and add[3] != '' and add[4] != '')\
                        or (e == 5 and add[5] == '' and add[3] == '' and add[4] == '') \
                        or (e == 5 and add[5] != '' and add[3] != '' and add[4] != '')\
                        or (e == 5 and add[5] != '' and add[3] != '' and add[4] == '')\
                        or (e == 5 and add[5] != '' and add[3] == '' and add[4] != ''):
                    self.false_3.setText('*')
                    self.false_4.setText('*')
                    self.false_5.setText('*')
        else:
            if add[3] != '':
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute("INSERT INTO tab_veg "
                "(veg, process, state, time_min, time_max)"
                " VALUES (?, ?, ?, ?, ?)", (add[0], add[1], add[2], add[3],  add[4], ))
                conn.commit()
                c.close()
                conn.close()
            else:
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute("INSERT INTO tab_veg "
                          "(veg, process, state, state_process)"
                          " VALUES (?, ?, ?, ?)", (add[0], add[1], add[2], add[5], ))
                conn.commit()
                c.close()
                conn.close()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
