import unittest
from PyQt5.QtWidgets import QWidget, QApplication
import sys
from Autorization import *
from Registration import *

app = QApplication(sys.argv)


class TestAuth(unittest.TestCase):

    authWidget = None
    ui = None

    def setUp(self):
        self.authWidget = QWidget()
        self.ui = Interface()
        self.gg = RegistrationWindow()

    def test1(self):
        self.ui.ui.Login.setText('123')
        self.ui.ui.Passw.setText('123')
        result = self.ui.auth()
        print(result)
        self.assertEqual(result, 1)

    def test2(self):
        self.ui.ui.Login.setText('admin')
        self.ui.ui.Passw.setText('admin')
        result = self.ui.auth()
        print(result)
        self.assertEqual(result, 0)

    def test3(self):
        self.gg.ui.Login.setText('admin')
        self.gg.ui.Passw.setText('admin')
        result = self.gg.reg()
        print(result)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
