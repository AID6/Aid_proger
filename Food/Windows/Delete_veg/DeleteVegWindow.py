import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DeleteVegClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style = 'font-size:17px;color:green'
        self.style_edit = 'font-size:17px;color:black;border-radius: 10px'
        self.style_btn = 'font-size:17px;color:green'
        self.style_1 = 'font-size:30px;color:red'
        self.style_dl = 'border: 3px solid black;font-size: 16px;background-color:rgba(255, 255, 255, 0,5);'

        self.information = QLabel('Выберите те данные, которые хотите удалить из этой программы.', self)
        self.information.setStyleSheet(self.style_edit)
        self.information.move(10, 10)

        self.veg_label = QLabel('Какой фрукт или овощь: ', self)
        self.process_label = QLabel('Какой процесс обработки: ', self)
        self.state_label = QLabel('Состояние продукта: ', self)
        self.time_min_label = QLabel('Минимальное время в минутах: ', self)
        self.time_max_label = QLabel('Максимальное время в минутах: ', self)
        self.state_process_label = QLabel('Готовить до появлени: ', self)

        self.veg_label.move(10, 60)
        self.process_label.move(10, 105)
        self.state_label.move(10, 150)
        self.time_min_label.move(10, 150434)
        self.time_max_label.move(10, 19554)
        self.state_process_label.move(10, 240448)

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
        self.combo_veg.move(300, 60)
        self.combo_veg.setFixedSize(400, 30)
        self.combo_veg.setStyleSheet(self.style_edit)
        self.combo_veg.activated.connect(self.data_process)

        self.combo_process = QComboBox(self)
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.combo_process.move(300, 105)
        self.combo_process.setFixedSize(400, 30)
        self.combo_process.setStyleSheet(self.style_edit)
        self.combo_process.activated.connect(self.data_state)

        self.combo_state = QComboBox(self)
        self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
        self.combo_state.move(300, 150)
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

        self.time_min_label_output.move(300, 195324)
        self.time_max_label_output.move(300, 240234)
        self.state_process_label_output.move(300, 240234)

        self.min_1 = QLabel('мин', self)
        self.min_2 = QLabel('мин', self)

        self.min_1.setStyleSheet(self.style_edit)
        self.min_2.setStyleSheet(self.style_edit)

        self.min_1.move(410, 15066)
        self.min_2.move(410, 19576)

        self.false_0 = QLabel('', self)
        self.false_0.setStyleSheet(self.style_1)
        self.false_0.setFixedSize(30, 30)
        self.false_0.move(703, 65)

        self.false_1 = QLabel('', self)
        self.false_1.setStyleSheet(self.style_1)
        self.false_1.setFixedSize(30, 30)
        self.false_1.move(703, 110)

        self.false_2 = QLabel('', self)
        self.false_2.setStyleSheet(self.style_1)
        self.false_2.setFixedSize(30, 30)
        self.false_2.move(703, 155)

        self.delete = QPushButton('Удалить', self)
        self.delete.setStyleSheet(self.style)
        self.delete.setFixedSize(130, 35)
        self.delete.move(320, 280)
        self.delete.clicked.connect(self.data_delete)

        self.back = QPushButton('Назад', self)
        self.back.setStyleSheet(self.style)
        self.back.setFixedSize(100, 35)
        self.back.move(610, 280)
        self.back.clicked.connect(self.backWindow)

        self.clear = QPushButton('Очистить', self)
        self.clear.setStyleSheet(self.style)
        self.clear.setFixedSize(130, 35)
        self.clear.move(465, 280)
        self.clear.clicked.connect(self.clear_all)

        self.setFixedSize(725, 330)
        self.center()
        self.setWindowIcon(QIcon('veg.jpg'))
        self.setWindowTitle('Удаление данных в раздел с фруктами и овощами')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clear_all(self):
        self.combo_state.clear()
        self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
        self.combo_process.clear()
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.combo_veg.clear()
        self.combo_veg.addItem('Какой фрукт или овощ вы хотите выбрать?')
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
        self.time_min_label_output.clear()
        self.time_max_label_output.clear()
        self.time_min_label_output.move(213, 213231)
        self.time_max_label_output.move(123123, 123)
        self.time_min_label.move(123, 12321)
        self.time_max_label.move(1232, 23121)
        self.min_1.move(121, 32213)
        self.min_2.move(123, 23112)
        self.state_process_label_output.clear()
        self.state_process_label_output.move(1232, 21311)
        self.state_process_label.move(12312, 213)

    def backWindow(self):
        self.veg_window = VegWindowClass()
        self.veg_window.show()
        self.close()

    def data_delete(self):
        dl = (self.combo_veg.currentText(), self.combo_process.currentText(), self.combo_state.currentText())
        if (dl[0] == 'Какой фрукт или овощ вы хотите выбрать?') or (dl[1] == 'Какой вид обработки вы выбираете?') or (dl[2] == 'В каком виде вы хотите приготовить продукт?'):
            e = -1
            for i in dl:
                e += 1
                if e == 0 and i == 'Какой фрукт или овощ вы хотите выбрать?':
                    self.false_0.setText('*')
                elif e == 1 and i == 'Какой вид обработки вы выбираете?':
                    self.false_1.setText('*')
                elif e == 2 and i == 'В каком виде вы хотите приготовить продукт?':
                    self.false_2.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("DELETE FROM tab_veg WHERE veg == ? and process == ? and state == ?",
                      (dl[0], dl[1], dl[2], ))
            conn.commit()
            c.close()
            conn.close()
            self.combo_state.clear()
            self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
            self.combo_process.clear()
            self.combo_process.addItem('Какой вид обработки вы выбираете?')
            self.combo_veg.clear()
            self.combo_veg.addItem('Какой фрукт или овощ вы хотите выбрать?')
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
            self.time_min_label_output.clear()
            self.time_max_label_output.clear()
            self.time_min_label_output.move(213, 213231)
            self.time_max_label_output.move(123123, 123)
            self.time_min_label.move(123, 12321)
            self.time_max_label.move(1232, 23121)
            self.min_1.move(121, 32213)
            self.min_2.move(123, 23112)
            self.state_process_label_output.clear()
            self.state_process_label_output.move(1232, 21311)
            self.state_process_label.move(12312, 213)

    def data_process(self):
        self.time_min_label_output.move(12323, 2323)
        self.time_max_label_output.move(31232, 21323)
        self.min_1.move(2323, 21323)
        self.min_2.move(2133123, 2321323)
        self.time_min_label.move(23232, 213232)
        self.time_max_label.move(23232, 213232)
        self.time_min_label_output.clear()
        self.time_max_label_output.clear()
        self.state_process_label_output.clear()
        self.state_process_label_output.move(3002323, 23032)
        self.state_process_label.move(1232, 123213)
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.combo_state.clear()
        self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
        self.combo_process.clear()
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
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
        self.time_min_label_output.clear()
        self.time_max_label_output.clear()
        self.state_process_label_output.clear()
        self.state_process_label_output.move(3002323, 23032)
        self.state_process_label.move(1232, 123213)
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.combo_state.clear()
        self.combo_state.addItem('В каком виде вы хотите приготовить продукт?')
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
        self.state_process_label_output.move(3002323, 23032)

    def data_output(self):
        self.time_min_label.move(23232, 213232)
        self.time_max_label.move(23232, 213232)
        self.time_min_label_output.move(12323, 2323)
        self.time_max_label_output.move(31232, 21323)
        self.min_1.move(2323, 21323)
        self.min_2.move(2133123, 2321323)
        self.time_min_label_output.clear()
        self.time_max_label_output.clear()
        self.state_process_label_output.clear()
        self.state_process_label_output.move(3002323, 23032)
        self.state_process_label.move(1232, 123213)
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
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
                self.state_process_label.move(10, 195)
                self.state_process_label_output.setText(' ' + data_mass[0][2])
                self.state_process_label_output.move(300, 195)
            else:
                self.time_min_label_output.move(300, 195)
                self.time_max_label_output.move(300, 240)
                self.time_min_label_output.setText(' ' + str(data_mass[0][0]))
                self.time_max_label_output.setText(' ' + str(data_mass[0][1]))
                self.time_min_label.move(10, 195)
                self.time_max_label.move(10, 240)
                self.min_1.move(410, 195)
                self.min_2.move(410, 240)
