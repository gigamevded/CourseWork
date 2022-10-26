import sys
import sqlite3
import Registration
import Sorted
from Aut import *


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pb_1.clicked.connect(self.auth)
        self.ui.pb_2.clicked.connect(self.regs)
        self.base_line_edit = [self.ui.Login, self.ui.Passw]

        self.sortWindow = None
        self.regWindow = None

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    QtWidgets.QMessageBox.warning(self, 'Предупреждение', 'Неверно введен логин или пароль')
                    return
            funct(self)
        return wrapper

    @check_input
    def auth(self):
        name = self.ui.Login.text()
        passw = self.ui.Passw.text()

        con = sqlite3.connect("users.db")
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE name="{name}";')
        value = cur.fetchall()
        cur.close()
        con.close()

        if value != [] and value[0][2] == passw:
            QtWidgets.QMessageBox.information(self, 'Информация', 'Авторизация выполнена успешно')
            self.sortWindow = Sorted.AnimationWidget()
            self.sortWindow.show()
            self.close()
            return 0
        else:
            QtWidgets.QMessageBox.warning(self, 'Предупреждение', 'Такого пользователя не существует')
            return 1

    def regs(self):
        self.regWindow = Registration.RegistrationWindow()
        self.regWindow.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())

