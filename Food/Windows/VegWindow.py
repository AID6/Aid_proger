import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from Windows.MeetWindow import MeetWindowClass

class VegWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style = 'font-size:20px;color:green;'
        self.style_edit = 'font-size:17px;color:black;border-radius: 10px'
        self.style_btn = 'font-size:18px;color:green'
        self.style_btn_main = 'font-size:30px;color:green'
        self.style_dl = 'border: 3px solid black;font-size: 16px;background-color:rgba(255, 255, 255, 0,5);'
        self.style_1 = 'font-size:30px;color:red'

        exitAction = QAction(QIcon('exit.jpg'), '&Выйти', self)
        add_veg = QAction(QIcon('add.png'), '&Добавить', self)
        edit_veg = QAction(QIcon('edit.png'), '&Изменить', self)
        delete_veg = QAction(QIcon('delete.png'), '&Удалить', self)
        about_veg = QAction(QIcon('about.png'), '&Разрабочики', self)
        exitAction.setShortcut('Ctrl+Q')

        add_veg.triggered.connect(self.add)
        edit_veg.triggered.connect(self.edit)
        delete_veg.triggered.connect(self.delete)
        about_veg.triggered.connect(self.about)
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        actions = menubar.addMenu('Действия')
        about = menubar.addMenu('Информация')
        about.addAction(about_veg)
        actions.addAction(add_veg)
        actions.addAction(edit_veg)
        actions.addAction(delete_veg)
        file.addAction(exitAction)

        self.veg = QLabel('Выберите овощ :', self)
        self.process = QLabel('Вид обработки :', self)
        self.state = QLabel('Состояние овоща :', self)
        self.time = QLabel('Время обработки :', self)

        self.veg.setFixedSize(200, 30)
        self.process.setFixedSize(200, 30)
        self.state.setFixedSize(200, 30)
        self.time.setFixedSize(200, 30)

        self.veg.move(10, 32)
        self.process.move(10, 77)
        self.state.move(10, 122)
        self.time.move(10, 212)

        self.veg.setStyleSheet(self.style)
        self.state.setStyleSheet(self.style)
        self.process.setStyleSheet(self.style)
        self.time.setStyleSheet(self.style)

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT veg FROM tab_veg")
        veg_data = c.fetchall()
        c.close()
        conn.close()
        self.veg = []
        for i in veg_data:
            if not i in self.veg:
                self.veg.append(i)
            else:
                continue
        self.veg.sort()

        self.combo_veg = QComboBox(self)
        self.combo_veg.addItem('Какой фрукт или овощ вы хотите приготовить?')
        self.combo_veg.addItems([i[0] for i in self.veg])
        self.combo_veg.move(200, 35)
        self.combo_veg.setFixedSize(400, 30)
        self.combo_veg.setStyleSheet(self.style_edit)
        self.combo_veg.activated.connect(self.data_process)

        self.combo_process_veg = QComboBox(self)
        self.combo_process_veg.addItem('Какой вид обработки вы выбираете?')
        self.combo_process_veg.move(200, 80)
        self.combo_process_veg.setFixedSize(400, 30)
        self.combo_process_veg.setStyleSheet(self.style_edit)
        self.combo_process_veg.activated.connect(self.data_state)

        self.combo_state_veg = QComboBox(self)
        self.combo_state_veg.addItem('В каком виде вы хотите приготовить продукт?')
        self.combo_state_veg.move(200, 125)
        self.combo_state_veg.setFixedSize(400, 30)
        self.combo_state_veg.setStyleSheet(self.style_edit)
        self.combo_state_veg.activated.connect(self.state_veg)

        self.finish_label = QLabel('', self)
        self.finish_label.setFixedSize(450, 100)
        self.finish_label.move(200, 215)
        self.finish_label.setStyleSheet(self.style_dl)

        self.calculate = QPushButton('Расчитать время', self)
        self.calculate.setStyleSheet(self.style_btn)
        self.calculate.resize(175, 35)
        self.calculate.move(200, 170)
        self.calculate.clicked.connect(self.data_time)

        exit = QPushButton('Выход', self)
        exit.clicked.connect(QCoreApplication.instance().quit)
        exit.setStyleSheet(self.style_btn)
        exit.resize(90, 35)
        exit.move(555, 350)

        self.window_meet = QPushButton('Перейти к мясу', self)
        self.window_meet.clicked.connect(self.MeetWindow_fun)
        self.window_meet.setStyleSheet(self.style_btn)
        self.window_meet.resize(200, 35)
        self.window_meet.move(340, 350)

        self.false_0 = QLabel('', self)
        self.false_0.setStyleSheet(self.style_1)
        self.false_0.setFixedSize(30, 30)
        self.false_0.move(605, 40)

        self.false_1 = QLabel('', self)
        self.false_1.setStyleSheet(self.style_1)
        self.false_1.setFixedSize(30, 30)
        self.false_1.move(605, 85)

        self.false_2 = QLabel('', self)
        self.false_2.setStyleSheet(self.style_1)
        self.false_2.setFixedSize(30, 30)
        self.false_2.move(605, 130)

        self.setFixedSize(660, 400)
        self.center()
        self.setWindowIcon(QIcon('veg.jpg'))
        self.setWindowTitle('Овощи и фрукты')
        self.show()

    def state_veg(self):
        self.finish_label.setText('')
        self.false_2.setText('')
        if self.combo_state_veg.currentText() == 'В каком виде вы хотите приготовить продукт?':
            self.false_2.setText('*')

    def add(self):
        self.AddVeg = AddVegClass()
        self.AddVeg.show()
        self.close()

    def edit(self):
        self.EditVeg = EditVegClass()
        self.EditVeg.show()
        self.close()

    def delete(self):
        self.DeleteVeg = DeleteVegClass()
        self.DeleteVeg.show()
        self.close()

    def about(self):
        print('about')

    def MeetWindow_fun(self):
        from Windows.MeetWindow import MeetWindowClass
        self.meet_window = MeetWindowClass()
        self.meet_window.show()
        self.close()

    def data_time(self):
        self.finish_label.setText('')
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        list_false = (self.combo_veg.currentText(), self.combo_process_veg.currentText(), self.combo_state_veg.currentText())
        if self.combo_process_veg.currentText() == 'Какой вид обработки вы выбираете?' or self.combo_state_veg.currentText() == 'В каком виде вы хотите приготовить продукт?'\
                or self.combo_veg.currentText() == 'Какой фрукт или овощ вы хотите приготовить?':
            e = -1
            for i in list_false:
                e += 1
                if e == 0 and i == 'Какой фрукт или овощ вы хотите приготовить?':
                    self.false_0.setText('*')
                elif e == 1 and i == 'Какой вид обработки вы выбираете?':
                    self.false_1.setText('*')
                elif e == 2 and i == 'В каком виде вы хотите приготовить продукт?':
                    self.false_2.setText('*')
        else:
            c.execute("SELECT time_min, time_max, veg, process, state, state_process FROM tab_veg WHERE veg == ? and process == ? and state == ?",
                (self.combo_veg.currentText(), self.combo_process_veg.currentText(), self.combo_state_veg.currentText(), ))
            data = c.fetchall()
            c.close()
            conn.close()
            if data[0][5] != None:
                self.finish_label.setText('Выбранный овощ или фрукт: ' + data[0][2] + '\n' + 'Выбранный процесс приготовления: ' + data[0][3] + '\n'+ 'Выбранный вид продукта: ' +
                                          data[0][4] + '\n' + 'Готовить до появления: ' + data[0][5])
            elif data[0][0] == data[0][1]:
                if data[0][0] > 60:
                    self.finish_label.setText(
                        'Выбранный овощ или фрукт: ' + data[0][2] + '\n' + 'Выбранный процесс приготовления: ' + data[0][3] + '\n'
                        + 'Выбранный вид продукта: ' + data[0][4] + '\n' + 'Время приготовления: ' + str(int(data[0][0] // 60)) + ' ч' + str(int(data[0][0] % 60)) + 'мин')
                elif data[0][0] == 60 or data[0][0] == 120 or data[0][0] == 180:
                    self.finish_label.setText(
                        'Выбранный овощ или фрукт: ' + data[0][2] + '\n' + 'Выбранный процесс приготовления: ' + data[0][3] + '\n'
                        + 'Выбранный вид продукта: ' + data[0][4] + '\n' + 'Время приготовления: ' + str(int(data[0][0] // 60)) + ' ч')
                else:
                    self.finish_label.setText(
                        'Выбранный овощ или фрукт: ' + data[0][2] + '\n' + 'Выбранный процесс приготовления: ' + data[0][3] + '\n'
                        + 'Выбранный вид продукта: ' + data[0][4] + '\n' + 'Время приготовления: ' + str(int(data[0][0])) + ' мин')
            elif data[0][0] >= 60 and data[0][0] != data[0][1]:
                if data[0][0] > 60:
                    self.finish_label.setText(
                        'Выбранный овощ или фрукт: ' + data[0][2] + '\n' + 'Выбранный процесс приготовления: ' + data[0][3] + '\n'
                        + 'Выбранный вид продукта: ' + data[0][4] + '\n' + 'Время приготовления: ' + str(int(data[0][0] // 60)) + ' ч ' + str(int(data[0][0] % 60))
                         + ' мин ' + '-' + str(int(data[0][1] // 60)) + ' ч ' + str(int(data[0][1] % 60)) + ' мин ')
                else:
                    self.finish_label.setText(
                        'Выбранный овощ или фрукт: ' + data[0][2] + '\n' + 'Выбранный процесс приготовления: ' + data[0][3] + '\n'
                        + 'Выбранный вид продукта: ' + data[0][4] + '\n' + 'Время приготовления: ' + str(int(data[0][0] // 60)) + ' ч ' + str(int(data[0][0] % 60))
                         + ' мин ' + '-' + str(int(data[0][1] // 60)) + ' ч ' + str(int(data[0][1] % 60)) + ' мин ')
            elif data[0][0] >= 60 and data[0][0] == data[0][1]:
                if data[0][0] > 60:
                    self.finish_label.setText(
                        'Выбранный овощ или фрукт: ' + data[0][2] + '\n' + 'Выбранный процесс приготовления: ' + data[0][3] + '\n'
                        + 'Выбранный вид продукта: ' + data[0][4] + '\n' + 'Время приготовления: ' + str(int(
                            data[0][0] // 60)) + ' ч ' + str(int(data[0][0] % 60))+ ' мин')
            else:
                self.finish_label.setText('Выбранный овощ или фрукт: ' + data[0][2] + '\n' + 'Выбранный процесс приготовления: ' + data[0][3] + '\n'
                                          + 'Выбранный вид продукта: ' + data[0][4] + '\n' + 'Время приготовления: ' + str(data[0][0]) + ' мин ' + ' - ' + str(data[0][1]) + ' мин')

    def data_state(self):
        self.finish_label.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.combo_state_veg.clear()
        self.combo_state_veg.addItem('В каком виде вы хотите приготовить продукт?')
        if self.combo_process_veg.currentText() == 'Какой вид обработки вы выбираете?':
            self.false_1.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("SELECT state FROM tab_veg WHERE veg == ? and process == ?", (self.combo_veg.currentText(), self.combo_process_veg.currentText(), ))
            state_data = c.fetchall()
            c.close()
            conn.close()
            self.state = []
            for i in state_data:
                if not i in self.state:
                    self.state.append(i)
                else:
                    continue
            self.state.sort()
            self.combo_state_veg.addItems([i[0] for i in self.state])

    def data_process(self):
        self.finish_label.setText('')
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.combo_state_veg.clear()
        self.combo_state_veg.addItem('В каком виде вы хотите приготовить продукт?')
        self.combo_process_veg.clear()
        self.combo_process_veg.addItem('Какой вид обработки вы выбираете?')
        if self.combo_veg.currentText() == 'Какой фрукт или овощ вы хотите приготовить?':
            self.false_0.setText('*')
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("SELECT process FROM tab_veg WHERE veg == ?", (self.combo_veg.currentText(), ))
            process_data = c.fetchall()
            c.close()
            conn.close()
            self.process = []
            for i in process_data:
                if not i in self.process:
                    self.process.append(i)
                else:
                    continue
            self.process.sort()
            self.combo_process_veg.addItems([i[0] for i in self.process])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

