import sqlite3
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QPushButton

import avtoriz2_ui
import registrasia_ui
from clienti2_ui import Ui_clienti2_ui
from menu_ui import Ui_menu_ui
from sotrudniki2_ui import Ui_sotrudniki2_ui
from tariffPlan2_ui import Ui_tariffPlan2_ui
from uslugi_ui import Ui_uslugi_ui

# Подключаемся к базе данных
db = sqlite3.connect('kursovaia.db')
cursor = db.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users(login TEXT, parol TEXT)''')
db.commit()

class Registrasia(QtWidgets.QMainWindow, registrasia_ui.Ui_registrasia_ui):
    def __init__(self):
        super(Registrasia, self).__init__()
        self.setupUi(self)
        self.lineEdit_login.setPlaceholderText('Введите логин')
        self.lineEdit_parol.setPlaceholderText('Введите пароль')
        self.pushButton_zaregestr.pressed.connect(self.reg)
        self.pushButton_voiti.pressed.connect(self.login)

    def login(self):
        self.login_window = Login()
        self.login_window.show()
        self.hide()

    def reg(self):
        try:
            user_login = self.lineEdit_login.text()
            user_parol = self.lineEdit_parol.text()

            if len(user_login) == 0:
                return
            if len(user_parol) == 0:
                return
            cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}" ')
            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO users VALUES("{user_login}","{user_parol}")')
                self.label_pustoi.setText(f'Аккаунт {user_login} успешно зарегистрирован')
                db.commit()
            else:
                self.label_pustoi.setText('Такая запись уже существует')
        except Exception as e:
            self.label_pustoi.setText(f'Аккаунт {user_login} успешно зарегистрирован')


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = avtoriz2_ui.Ui_avtoriz2_ui()
        self.ui.setupUi(self)
        self.ui.lineEdit_Login.setPlaceholderText('Введите логин')
        self.ui.lineEdit_Parol.setPlaceholderText('Введите пароль')
        self.ui.pushButton_vioti.clicked.connect(self.login)
        self.ui.pushButton_zaregestr.clicked.connect(self.reg)

    # Остальной код остается без изменений

    def reg(self):
        self.reg_window = Registrasia()
        self.reg_window.show()
        self.hide()

    def login(self):
        try:
            user_login = self.ui.lineEdit_Login.text()
            user_parol = self.ui.lineEdit_Parol.text()

            if len(user_login) == 0:
                return
            if len(user_parol) == 0:
                return

            cursor.execute(f'SELECT parol FROM users WHERE login = "{user_login}"')
            check_par = cursor.fetchall()

            cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
            check_login = cursor.fetchall()

            if check_par and check_login and check_par[0][0] == user_parol and check_login[0][0] == user_login:
                self.label_pustaia.setText(f'Успешная авториазация')

                self.open_menu()
            else:
                self.label_pustaia.setText(f'Неверный логин или пароль')
        except Exception as e:
            self.label_pustaia.setText(f'Ошибка при авторизации')

    def open_menu(self):
        self.menu_ui = Menu_ui()
        self.menu_ui.show()
        self.hide()


    # def open_menu(self):
    #     self.hide()  # Скрываем окно авторизации
    #     self.menu_ui = Menu_ui()
    #     self.menu_ui.show()
    # def show_clients(self):
    #     self.SH_clients = Ui_clienti2_ui()
    #     self.SH_clients.setupUi(self)  # Инициализируем форму клиентов
    #     self.SH_clients.show()


class Menu_ui(QWidget, Ui_menu_ui):
    def __init__(self):
        super(Menu_ui, self).__init__()
        self.setupUi(self)
        self.pushButton_clients.clicked.connect(self.show_clients)
        self.pushButton_tariffPlan.clicked.connect(self.show_tariffPlan)
        self.pushButton_sotrudniki.clicked.connect(self.show_sotrudniki)
        self.pushButton_uslugi.clicked.connect(self.show_uslugi)
        self.pushButton_exit.clicked.connect(QApplication.quit)

    def show_clients(self):
        self.SH_clients = Clienti2_ui()
        self.SH_clients.setupUi(self)
        self.SH_clients.show()

    def show_tariffPlan(self):
        self.SH_tariffPlan_ui = TariffPlan2_ui()
        self.SH_tariffPlan_ui.setupUi(self)
        self.SH_tariffPlan_ui.show()

    def show_sotrudniki(self):
        self.SH_sotrudniki_ui = Sotrudniki2_ui()
        self.SH_sotrudniki_ui.setupUi(self)
        self.SH_sotrudniki_ui.show()

    def show_uslugi(self):
        self.SH_uslugi = Uslugi_ui()
        self.SH_uslugi.setupUi(self)
        self.SH_uslugi.show()
    # def closeEvent(self, event):
    #     super(Menu_ui, self).closeEvent(event)
    #     self.deleteLater()  # Удаляем окно из памяти


# Класс для окна "Clienti2_ui"
class Clienti2_ui(QWidget, Ui_clienti2_ui):
    def __init__(self):
        super(Clienti2_ui, self).__init__()
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.open_clienti)
        self.pushButton_delete.clicked.connect(self.delete_clienti)
        self.pushButton_insert.clicked.connect(self.insert_clienti)
        self.conn = sqlite3.connect('kursovaia.db')
        self.update()



    def open_clienti(self):
        try:
            cur = self.conn.cursor()
            data = cur.execute("SELECT * FROM Subscriber;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД:", e)
            return

        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="SELECT * FROM Subscriber"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подключением: {d}")
            return

        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_clienti(self):
        row = [
            self.lineEdit_Imia.text(),
            self.lineEdit_Familia.text(),
            self.lineEdit_Otchestvo.text(),
            'муж' if self.radioButton_male.isChecked() else 'жен',
            self.dateEdit_DataRoxh.text(),
            self.lineEdit_telefon.text(),
            self.lineEdit_email.text()
        ]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""
                INSERT INTO Subscriber(first_name, surname, last_name, gender, Date_of_Birth, phone_number, email)
                VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}')
            """)
            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не удалось добавить запись:", r)
            return

        self.update()

    def delete_clienti(self):
        row = self.tableWidget.currentRow()
        num = self.tableWidget.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"DELETE FROM Subscriber WHERE id = {num}")
            self.conn.commit()
            cur.close()
        except Exception as g:
            print("Не удалось удалить запись:", g)
            return

        self.update()

# Класс для окна "Menu_ui"

class TariffPlan2_ui (QWidget, Ui_tariffPlan2_ui):
    def __init__(self):
        super(TariffPlan2_ui, self).__init__()
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.open_tariffPlan)
        self.pushButton_insert.clicked.connect(self.insert_tariffPlan)
        self.pushButton_delete.clicked.connect(self.delete_tariffPlan)


    def open_tariffPlan(self):  # кнопка добавить
        try:
            self.conn = sqlite3.connect('kursovaia.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Tariff Plan;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()


    def update(self, query="select * from Tariff Plan"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_tariffPlan(self):  # кнопка добавить
        row = [self.lineEdit_tariff.text(), self.lineEdit_stoimost.text(), self.lineEdit_minut.text(),
            self.lineEdit_internet.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Tariff Plan( name_tariff_plan, price(rub), tariff_data(phone), tariff_data(internet))
                            values('{row[0]}','{row[1]}','{row[2]}','{row[3]}'""")
            self.conn.commit()
            cur.close()
            self.update()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
        self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД



    def delete_tariffPlan(self):
        row = self.tableWidget.currentRow()
        num = self.tableWidget.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"DELETE FROM Tariff Plan WHERE id = {num}")
            self.conn.commit()
            cur.close()
        except Exception as g:
            print("Не удалось удалить запись:", g)
            return


class Sotrudniki2_ui(QWidget, Ui_sotrudniki2_ui):
    def __init__(self):
        super(Sotrudniki2_ui, self).__init__()
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.open_sotrudniki)
        self.pushButton_insert.clicked.connect(self.insert_sotrudniki)
        self.pushButton_delete.clicked.connect(self.delete_sotrudniki)

    def open_sotrudniki(self):  # кнопка добавить
        try:
            self.conn = sqlite3.connect('kursovaia.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Tariff Plan;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="select * from Employees"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_tariffPlan(self):  # кнопка добавить
        row = [self.lineEdit_tariff.text(), self.lineEdit_stoimost.text(), self.lineEdit_minut.text(),
                self.lineEdit_internet.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Employees( first_name, surname, last_name, gender, Date_of_Birth, phone_number, email, post)
            values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}')""")

            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
            self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

    def delete_sotrudniki(self):
        row = self.tableWidget.currentRow()
        num = self.tableWidget.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"DELETE FROM Employees WHERE id = {num}")
            self.conn.commit()
            cur.close()
        except Exception as g:
            print("Не удалось удалить запись:", g)
            return
class Uslugi_ui(QWidget, Ui_uslugi_ui):
    def __init__(self):
        super(Uslugi_ui, self).__init__()
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.open_uslugi)
        self.pushButton_insert.clicked.connect(self.insert_uslugi)
        self.pushButton_delete.clicked.connect(self.delete_uslugi)

    def open_uslugi(self):  # кнопка добавить
        try:
            self.conn = sqlite3.connect('kursovaia.db')
            cur = self.conn.cursor()
            data = cur.execute("select * from Additional Services;")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
        except Exception as e:
            print("Ошибки с подключением к БД")
            return e
        self.tableWidget.setColumnCount(len(col_name))
        self.tableWidget.setHorizontalHeaderLabels(col_name)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def update(self, query="select * from Additional Services"):  # после добавление сразу видно запись
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as d:
            print(f"Проблемы с подкл {d}")
            return d
        self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы заносим по новой
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elen in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
        self.tableWidget.resizeColumnsToContents()

    def insert_uslugi(self):  # кнопка добавить
        row = [self.lineEdit_usluga.text(), self.lineEdit_stoimUsl.text()]
        try:
            cur = self.conn.cursor()
            cur.execute(f"""insert into Additional Services( name_additional_services, price(rub))
            values('{row[0]}','{row[1]}'""")
            self.conn.commit()
            cur.close()
        except Exception as r:
            print("Не смогли добавить запись")
            return r
        self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД



    def delete_uslugi(self):
        row = self.tableWidget.currentRow()
        num = self.tableWidget.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"DELETE FROM Additional Services WHERE id = {num}")
            self.conn.commit()
            cur.close()
        except Exception as g:
            print("Не удалось удалить запись:", g)
            return




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())

