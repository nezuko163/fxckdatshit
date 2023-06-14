from PyQt6 import uic
from PyQt6 import QtWidgets, QtCore
import pathlib
from sys import argv, exit
from singleton import Singleton


class MainWidnow(QtWidgets.QMainWindow, Singleton):
    def __init__(self):
        super(MainWidnow, self).__init__()
        self._initUi()

    def _initUi(self):
        uic.loadUi(pathlib.Path(__file__)
                   .parent.parent.__str__() +
                   r"\res\test_start.ui", self)
        self.setWindowTitle("Лаунчер")
        self.setFixedSize(QtCore.QSize(257, 300))

    def __connect_buttons(self):
        self.btn_account.clicked.connect(self.__goToAccountActivity())


    def __goToAccountActivity(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    ex = MainWidnow()
    ex.show()
    exit(app.exec())
