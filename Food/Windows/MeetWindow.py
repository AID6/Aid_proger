import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from Windows.VegWindow import VegWindowClass

class MeetWindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.style = 'font-size:20px;color:green;'
        self.style_sb = 'color: green; font-size: 16px;'
        self.style_edit = 'font-size:17px; color:black; border-radius: 10px'
        self.style_btn = 'font-size:18px; color:green'
        self.style_btn_main = 'font-size:30px; color:green'
        self.style_dl = 'border: 3px solid black; font-size: 16px;background-color:rgba(255, 255, 255, 0,5);'
        self.style_1 = 'font-size:30px;c olor:red'

        exitAction = QAction(QIcon('exit.jpg'), '&Выйти', self)
        add_meet = QAction(QIcon('add.png'), '&Добавить', self)
        edit_meet = QAction(QIcon('edit.png'), '&Изменить', self)
        delete_meet = QAction(QIcon('delete.png'), '&Удалить', self)
        about_meet = QAction(QIcon('about.png'), '&Разрабочики', self)
        exitAction.setShortcut('Ctrl+Q')

        #add_meet.triggered.connect(self.add)
        #edit_meet.triggered.connect(self.edit)
        #delete_meet.triggered.connect(self.delete)
        #exitAction.triggered.connect(qApp.quit)
        #about_meet.triggered.connect(self.about)

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        actions = menubar.addMenu('Действия')
        about = menubar.addMenu('Информация')
        about.addAction(about_meet)
        actions.addAction(add_meet)
        actions.addAction(edit_meet)
        actions.addAction(delete_meet)
        file.addAction(exitAction)

        self.meet = QLabel('Вид мяса :', self)
        self.process = QLabel('Вид обработки :', self)
        self.part = QLabel('Обрабатываемый продукт :', self)
        self.mass = QLabel('Масса продукта :', self)
        self.time = QLabel('Время обработки :', self)

        self.meet.setFixedSize(270, 30)
        self.part.setFixedSize(270, 30)
        self.process.setFixedSize(270, 30)
        self.mass.setFixedSize(270, 30)
        self.time.setFixedSize(270, 30)

        self.meet.move(10, 32)
        self.process.move(10, 77)
        self.part.move(10, 122)
        self.mass.move(10, 167)
        self.time.move(10, 212)

        self.meet.setStyleSheet(self.style)
        self.part.setStyleSheet(self.style)
        self.process.setStyleSheet(self.style)
        self.mass.setStyleSheet(self.style)
        self.time.setStyleSheet(self.style)

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
        self.combo_meet.move(280, 35)
        self.combo_meet.setFixedSize(400, 30)
        self.combo_meet.setStyleSheet(self.style_edit)
        self.combo_meet.activated.connect(self.data_process)

        self.combo_process = QComboBox(self)
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        self.combo_process.move(280, 80)
        self.combo_process.setFixedSize(400, 30)
        self.combo_process.setStyleSheet(self.style_edit)
        self.combo_process.activated.connect(self.data_part)

        self.combo_part = QComboBox(self)
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
        self.combo_part.move(280, 125)
        self.combo_part.setFixedSize(400, 30)
        self.combo_part.setStyleSheet(self.style_edit)
        self.combo_part.activated.connect(self.data_end)

        self.edit_mass = QLineEdit(self)
        self.edit_mass.setValidator(QDoubleValidator(0, 9999999, 1, self.edit_mass))
        self.edit_mass.resize(80, 30)
        self.edit_mass.move(280, 170)
        self.edit_mass.setStyleSheet(self.style_edit)

        exit = QPushButton('Выход', self)
        exit.clicked.connect(QCoreApplication.instance().quit)
        exit.setStyleSheet(self.style_btn)
        exit.resize(90, 35)
        exit.move(605, 350)

        self.window_veg = QPushButton('Перейти к овощам и фруктам', self)
        self.window_veg.clicked.connect(self.VegWindow_fun)
        self.window_veg.setStyleSheet(self.style_btn)
        self.window_veg.resize(300, 35)
        self.window_veg.move(287, 350)

        self.finish_label = QLabel('', self)
        self.finish_label.setFixedSize(460, 100)
        self.finish_label.move(230, 212)
        self.finish_label.setStyleSheet(self.style_dl)

        self.calculate = QPushButton('Расчитать время', self)
        self.calculate.clicked.connect(self.to_calculate)
        self.calculate.setStyleSheet(self.style_btn)
        self.calculate.resize(175, 35)
        self.calculate.move(420, 170)

        self.gg_label = QLabel('грамм', self)
        self.gg_label.move(364, 175)
        self.gg_label.setStyleSheet(self.style_btn)

        self.false_0 = QLabel('', self)
        self.false_0.setStyleSheet(self.style_1)
        self.false_0.setFixedSize(30, 30)
        self.false_0.move(685, 40)

        self.false_1 = QLabel('', self)
        self.false_1.setStyleSheet(self.style_1)
        self.false_1.setFixedSize(30, 30)
        self.false_1.move(685, 85)

        self.false_2 = QLabel('', self)
        self.false_2.setStyleSheet(self.style_1)
        self.false_2.setFixedSize(30, 30)
        self.false_2.move(685, 130)

        self.false_3 = QLabel('', self)
        self.false_3.setStyleSheet(self.style_1)
        self.false_3.setFixedSize(30, 30)
        self.false_3.move(345, 175)

        self.setFixedSize(710, 400)
        self.center()
        self.setWindowIcon(QIcon('meet.jpg'))
        self.setWindowTitle('Мясо')
        self.show()

    def data_end(self):
        self.finish_label.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        if self.combo_part.currentText() == 'Какой продукт вы хотите обработать?':
            self.false_2.setText('*')

    def edit(self):
        self.EditMeet = EditMeetClass()
        self.EditMeet.show()
        self.close()

    def delete(self):
        self.DeleteMeet = DeleteMeetClass()
        self.DeleteMeet.show()
        self.close()

    def about(self):
        print('about')
    def add(self):
        self.AddMeet = AddMeetClass()
        self.AddMeet.show()
        self.close()

    def VegWindow_fun(self):
        from Windows.VegWindow import VegWindowClass
        self.VegW = VegWindowClass()
        self.VegW.show()
        self.close()

    def to_calculate(self):
        self.finish_label.setText('')
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT mass_4_min, mass_4_max, time_4_min, time_4_max, meet, process, part FROM tab_meet_finish WHERE meet == ? AND process == ? AND part == ?",
                  (self.combo_meet.currentText(), self.combo_process.currentText(), self.combo_part.currentText(), ))
        data = c.fetchall()
        c.close()
        conn.close()
        list_false = (self.combo_meet.currentText(), self.combo_process.currentText(), self.combo_part.currentText(), self.edit_mass.text())
        if self.edit_mass.text() == '' or self.combo_meet.currentText() == 'Из какого мяса продукт?' or self.combo_process.currentText() == 'Какой вид обработки вы выбираете?' or self.combo_part.currentText() == 'Какой продукт вы хотите обработать?':
            e = -1
            for i in list_false:
                e += 1
                if e == 0 and i == 'Из какого мяса продукт?':
                    self.false_0.setText('*')
                elif e == 1 and i == 'Какой вид обработки вы выбираете?':
                    self.false_1.setText('*')
                elif e == 2 and i == 'Какой продукт вы хотите обработать?':
                    self.false_2.setText('*')
                elif e == 3 and i == '':
                    self.false_3.setText('*')
        else:
            k_min, k_max, e = float(data[0][0] / data[0][2]), float(data[0][1] / data[0][3]), int(self.edit_mass.text())
            meet_process_part = 'Мясо: ' + data[0][4] + '\n' + 'Вид обработки: ' + data[0][5] + '\n' + 'Продукт: ' + data[0][6] + '\n'
            if e > 1000:
                mass = 'Масса продукта: ' + str(e // 1000) + ' кг ' + str(e % 1000) + ' гр ' + '\n'
                if int(e) > data[0][0] and int(e) < data[0][1]:
                    x = float((data[0][1] - data[0][0]) / 2)
                    m = float(e - data[0][0])
                    if float(m) > float(x):
                        if int(e / k_max) > 60:
                            time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' ч ' + str(int((e / k_max) % 60)) + ' мин'
                        elif int(e / k_max) == 60:
                            time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round((e / k_max) % 60, 1)) + ' мин'
                    elif float(m < x):
                        if float(e / k_min) > 60:
                            time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' ч ' + str(int((e / k_min) % 60)) + ' мин'
                        elif int(e / k_min) == 60:
                            time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round((e / k_min) % 60, 1)) + ' мин'
                    elif float(m == x):
                        if float(e / ((k_min + k_max) / 2)) > 60:
                            time = 'Время обаботки: ' + str(int((e / ((k_min + k_max) / 2)) // 60)) + ' ч ' + str(int(e / ((k_min + k_max) / 2) % 60)) + ' мин'
                        elif int((e / ((k_min + k_max) / 2))) == 60:
                            time = 'Время обаботки: ' + str(int((e / ((k_min + k_max) / 2)) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round(e / ((k_min + k_max) / 2) % 60, 1)) + ' мин'
                elif int(e) == 0:
                    self.finish_label.setText('Люди пока что\n не научились\nделать еду\n из ничего))')
                elif int(e) <= data[0][0]:
                    if int(e / k_min) > 60:
                        time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' ч ' + str(int((e / k_min) % 60)) + ' мин'
                    elif int(e / k_min) == 60:
                        time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' час '
                    else:
                        time = 'Время обаботки: ' + str(round((e / k_min) % 60, 1)) + ' мин'
                elif int(e) >= data[0][1]:
                    if int(e / k_max) > 60:
                        time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' ч ' + str(int((e / k_max) % 60)) + ' мин'
                    elif int(e / k_max) == 60:
                        time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' час '
                    else:
                        time = 'Время обаботки: ' + str(round((e / k_max) % 60, 1)) + ' мин'
            elif e == 1000:
                mass = 'Масса продукта: ' + str(e // 1000) + ' кг ' + '\n'
                if int(e) > data[0][0] and int(e) < data[0][1]:
                    x = float((data[0][1] - data[0][0]) / 2)
                    m = float(e - data[0][0])
                    if float(m) > float(x):
                        if int(e / k_max) > 60:
                            time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' ч ' + str(int((e / k_max) % 60)) + ' мин'
                        elif int(e / k_max) == 60:
                            time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round((e / k_max) % 60, 1)) + ' мин'
                    elif float(m < x):
                        if float(e / k_min) > 60:
                            time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' ч ' + str(int((e / k_min) % 60)) + ' мин'
                        elif int(e / k_min) == 60:
                            time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round((e / k_min) % 60, 1)) + ' мин'
                    elif float(m == x):
                        if float(e / ((k_min + k_max) / 2)) > 60:
                            time = 'Время обаботки: ' + str(int((e / ((k_min + k_max) / 2)) // 60)) + ' ч ' + str(int((e / ((k_min + k_max) / 2)) % 60)) + ' мин'
                        elif int((e / ((k_min + k_max) / 2))) == 60:
                            time = 'Время обаботки: ' + str(int((e / ((k_min + k_max) / 2)) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round((e / ((k_min + k_max) / 2)) % 60, 1)) + ' мин'
                elif int(e) == 0:
                    self.finish_label.setText('Люди пока что\n не научились\nделать еду\n из ничего))')
                    pass
                elif int(e) <= data[0][0]:
                    if int(e / k_min) > 60:
                        time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' ч ' + str(int((e / k_min) % 60)) + ' мин'
                    elif int(e / k_min) == 60:
                        time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' час '
                    else:
                        time = 'Время обаботки: ' + str(round((e / k_min) % 60, 1)) + ' мин'
                elif int(e) >= data[0][1]:
                    if int(e / k_max) > 60:
                        time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' ч ' + str(int((e / k_max) % 60)) + ' мин'
                    elif int(e / k_max) == 60:
                        time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' час '
                    else:
                        time = 'Время обаботки: ' + str(round((e / k_max) % 60, 1)) + ' мин'
            else:
                mass = 'Масса продукта: ' + str(e) + ' гр ' + '\n'
                if int(e) > data[0][0] and int(e) < data[0][1]:
                    x = float((data[0][1] - data[0][0]) / 2)
                    m = float(e - data[0][0])
                    if float(m) > float(x):
                        if int(e / k_max) > 60:
                            time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' ч ' + str(int((e / k_max) % 60)) + ' мин'
                        elif int(e / k_max) == 60:
                            time = 'Время обаботки: ' + str(int((e/ k_max) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round((e / k_max) % 60, 1)) + ' мин'
                    elif float(m < x):
                        if float(e / k_min) > 60:
                            time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' ч ' + str(int((e / k_min) % 60)) + ' мин'
                        elif int(e / k_min) == 60:
                            time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round((e / k_min) % 60, 1)) + ' мин'
                    elif float(m == x):
                        if float(e / ((k_min + k_max) / 2)) > 60:
                            time = 'Время обаботки: ' + str(int(e / ((k_min + k_max) / 2) // 60)) + ' ч ' + str(int(e / ((k_min + k_max) / 2) % 60)) + ' мин'
                        elif int((e / ((k_min + k_max) / 2))) == 60:
                            time = 'Время обаботки: ' + str(int(e / ((k_min + k_max) / 2) // 60)) + ' час '
                        else:
                            time = 'Время обаботки: ' + str(round(e / ((k_min + k_max) / 2) % 60, 1)) + ' мин'
                elif int(e) == 0:
                    self.finish_label.setText('Люди пока что\n не научились\nделать еду\n из ничего))')
                    return
                elif int(e) <= data[0][0]:
                    if int(e / k_min) > 60:
                        time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' ч ' + str(int((e / k_min) % 60)) + ' мин'
                    elif int(e / k_min) == 60:
                        time = 'Время обаботки: ' + str(int((e / k_min) // 60)) + ' час '
                    else:
                        time = 'Время обаботки: ' + str(round((e / k_min) % 60, 1)) + ' мин'
                elif int(e) >= data[0][1]:
                    if int(e / k_max) > 60:
                        time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' ч ' + str(int((e / k_max) % 60)) + ' мин'
                    elif int(e / k_max) == 60:
                        time = 'Время обаботки: ' + str(int((e / k_max) // 60)) + ' час '
                    else:
                        time = 'Время обаботки: ' + str(round((e / k_max) % 60, 1)) + ' мин'
            self.finish_label.setText(meet_process_part + mass + time)

    def data_process(self):
        self.finish_label.setText('')
        self.false_0.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.combo_part.clear()
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
        self.combo_process.clear()
        self.combo_process.addItem('Какой вид обработки вы выбираете?')
        if self.combo_meet.currentText() == 'Из какого мяса продукт?':
            self.false_0.setText('*')
            pass
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

    def data_part(self):
        self.finish_label.setText('')
        self.false_1.setText('')
        self.false_2.setText('')
        self.false_3.setText('')
        self.combo_part.clear()
        self.combo_part.addItem('Какой продукт вы хотите обработать?')
        if self.combo_process.currentText() == 'Какой вид обработки вы выбираете?' or self.combo_meet.currentText() == 'Из какого мяса продукт?':
            self.false_1.setText('*')
            pass
        else:
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("SELECT part FROM tab_meet_finish WHERE meet == ? and process == ?",
                      (self.combo_meet.currentText(), self.combo_process.currentText(), ))
            data_part = c.fetchall()
            self.part = []
            for i in data_part:
                if not i in self.part:
                    self.part.append(i)
                else:
                    continue
            self.part.sort()
            self.combo_part.addItems([i[0] for i in self.part])
            c.close()
            conn.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())