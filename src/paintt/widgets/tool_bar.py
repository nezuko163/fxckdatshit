from PyQt6.QtWidgets import QToolBar, QApplication, QMenu, QToolButton
from PyQt6.QtGui import QAction

import sys


class CustomToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.initUi()

    def initUi(self):
        self.