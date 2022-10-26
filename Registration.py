import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Reg import *
import sqlite3
import Autorization


class RegistrationWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pb_1.clicked.connect(self.reg)
        self.ui.pb_2.clicked.connect(self.back)
        self.base_line_edit = [self.ui.Login, self.ui.Passw]

        self.authWindow = None

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    QtWidgets.QMessageBox.information(self, 'Информация', 'Заполните поля логин и пароль')
                    return
            funct(self)
        return wrapper

    def back(self):
        self.authWindow = Autorization.Interface()
        self.authWindow.show()
        self.close()

    @check_input
    def reg(self):
        name = self.ui.Login.text()
        passw = self.ui.Passw.text()

        con = sqlite3.connect("users.db")
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE name="{name}";')
        value = cur.fetchall()

        if value:
            QtWidgets.QMessageBox.warning(self, 'Предупреждение', 'Пользователь с таким именем уже существует')
            return 0
        else:
            cur.execute(f'INSERT INTO users (name, password) VALUES ("{name}", "{passw}")')
            QtWidgets.QMessageBox.information(self, 'Информация', 'Регистрация выполнена')
            con.commit()
        cur.close()
        con.close()
        self.back()