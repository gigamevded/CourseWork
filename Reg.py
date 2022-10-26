from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(312, 251)
        self.pb_1 = QtWidgets.QPushButton(Form)
        self.pb_1.setGeometry(QtCore.QRect(50, 190, 211, 31))
        self.pb_1.setObjectName("pb_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Login = QtWidgets.QLineEdit(Form)
        self.Login.setGeometry(QtCore.QRect(50, 60, 211, 31))
        self.Login.setObjectName("Login")
        self.Passw = QtWidgets.QLineEdit(Form)
        self.Passw.setGeometry(QtCore.QRect(50, 140, 211, 31))
        self.Passw.setObjectName("Passw")
        self.pb_2 = QtWidgets.QPushButton(Form)
        self.pb_2.setGeometry(QtCore.QRect(270, 0, 41, 21))
        self.pb_2.setObjectName("pb_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Регистрация"))
        self.pb_1.setText(_translate("Form", "Регистрация"))
        self.label.setText(_translate("Form", "Логин:"))
        self.label_2.setText(_translate("Form", "Пароль:"))
        self.pb_2.setText(_translate("Form", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
