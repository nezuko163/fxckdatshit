import sys

from PyQt6.QtWidgets import QMenuBar, QMenu, QApplication
from PyQt6.QtGui import QAction


class CustomMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.initUi()

    def initUi(self):
        self.setStyleSheet("""QMenuBar {
             background-color: #FFFAFA;
        }""")
        file_menu = self.addMenu("&File")

        save_act = QAction("Save", self)
        save_act.triggered.connect(self.saveAsPNG)
        file_menu.addAction(save_act)

        save_menu = QMenu("Save as", self)

        save_as_jpg = QAction("Save as JPG", self)
        save_as_jpg.triggered.connect(self.saveAsJPG)
        save_menu.addAction(save_as_jpg)

        save_as_png = QAction("Save as PNG", self)
        save_as_png.triggered.connect(self.saveAsPNG)
        save_menu.addAction(save_as_png)

        save_as_gif = QAction("Save as GIF", self)
        save_as_jpg.triggered.connect(self.saveAsGIF)
        save_menu.addAction(save_as_gif)

        file_menu.addMenu(save_menu)

    def saveAsJPG(self):
        pass

    def saveAsPNG(self):
        pass

    def saveAsGIF(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CustomMenuBar()
    ex.show()
    sys.exit(app.exec())
