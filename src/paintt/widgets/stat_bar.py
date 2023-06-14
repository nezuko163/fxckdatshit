from PyQt6.QtWidgets import QStatusBar


class CustomStatusBar(QStatusBar):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def updateCoords(self, x: int, y: int):
        self.showMessage(f"{x}, {y}")
