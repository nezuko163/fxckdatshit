from widgets.paitArea import PaintArea
from widgets.stat_bar import CustomStatusBar
from widgets.menu_bar import CustomMenuBar

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QMouseEvent

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.canvas = PaintArea(self)
        self.stat_bar = CustomStatusBar(self)
        self.menu_bar = CustomMenuBar(self)

        self.initUi()

    def initUi(self):
        self.initPaintArea()
        self.initStatusBar()
        self.initMenuBar()

        self.setStyleSheet("""QMainWindow {
             background-color: #F5F5F5;
        }""")

    def initPaintArea(self):
        self.setCentralWidget(self.canvas)

    def initStatusBar(self):
        self.setStatusBar(self.stat_bar)

        # без вызова этой функции метод mouseMoveEvent вызывается только при какой-либо нажатой кнопке мыши
        # теперь метод mouseMoveEvent будем вызываться без зажатой кнопки
        self.setMouseTracking(True)

    def initMenuBar(self):
        self.setMenuBar(self.menu_bar)


    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        self.stat_bar.updateCoords(a0.pos().x(), a0.pos().y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

# from PyQt6.QtWidgets import QMainWindow, QApplication
# from PyQt6.QtGui import QMouseEvent
#
# import sys
#
# from stat_bar import CustomStatusBar
#
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#
#
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle('Statusbar')
#         self.show()
#
#
#
#     def aye(self):
#         print('123')
#
#
# def main():
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec())
#
#
# if __name__ == '__main__':
#     main()
