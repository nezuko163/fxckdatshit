from PyQt6.QtWidgets import QLabel, QApplication
from PyQt6.QtGui import QPixmap, QColor, QMouseEvent, QPaintEvent, QPen, QPainter, QImage
from PyQt6.QtCore import QPoint, Qt

import sys
from enum import Enum


class Mode:
    point = "point"
    line = 'line'
    rectangle = 'rectangle'
    circle = "circle"
    ellipse = "ellipse"
    eraser = "eraser"
    fill = "fill"
    spray = "spray"
    text = "text"


class PaintArea(QLabel):
    size = None
    bg_color = QColor("white")

    mode = Mode.point

    last_pos = None
    current_pos = None

    drawing = False

    brushSize = 4
    brushColor = QColor("black")

    def __init__(self, parent=None, w=400, h=400):
        super().__init__(parent)

        self.size = (w, h)
        self.image = QImage(*self.size, QImage.Format.Format_RGB32)
        self.resize(*self.size)
        self.clear()

        self.setMouseTracking(True)

    def clear(self):
        canvas = QPixmap(*self.size)
        canvas.fill(QColor("white"))
        self.setPixmap(canvas)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        if self.parent(): self.parent().mouseMoveEvent(ev)
        a = getattr(self, f"{self.mode}_mousePressEvent", None)
        if a:
            a(ev)

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        if self.parent(): self.parent().mouseMoveEvent(ev)
        a = getattr(self, f"{self.mode}_mouseReleaseEvent", None)
        if a:
            a(ev)

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        if self.parent(): self.parent().mouseMoveEvent(ev)
        a = getattr(self, f"{self.mode}_mouseMoveEvent", None)
        if a:
            a(ev)

    def point_mouseMoveEvent(self, ev: QMouseEvent) -> None:
        if self.drawing:
            self.drawPoint(ev.pos())
            self.last_pos = ev.pos()

    def point_mousePressEvent(self, ev: QMouseEvent) -> None:
        self.drawing = True
        self.last_pos = ev.pos()

    def point_mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.drawing = False
        self.last_pos = None

    def eraser_mousePressEvent(self, ev: QMouseEvent) -> None:
        self.drawing = True

    def eraser_mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.drawing = False

    def eraser_mouseMoveEvent(self, ev: QMouseEvent) -> None:
        if self.drawing:
            self.drawPoint(ev.pos(), self.bg_color)

    def drawCircle(self):
        canvas = self.pixmap()
        painter = QPainter(canvas)
        painter.begin(self)
        pen = QPen(self.brushColor, self.brushSize)

        painter.setPen(pen)
        painter.draw
        painter.end()
        self.setPixmap(canvas)

    def drawPoint(self, pos: QPoint, color=brushColor):
        canvas = self.pixmap()
        painter = QPainter(canvas)
        painter.begin(canvas)
        pen = QPen(color, self.brushSize)

        painter.setPen(pen)

        if self.last_pos:
            painter.drawLine(pos, self.last_pos)

        else:
            painter.drawPoint(pos)

        painter.end()
        self.setPixmap(canvas)

    # def timerEvent(self, a0: 'QTimerEvent') -> None:

    def drawLine(self, last_pos: QPoint, current_pos: QPoint):
        pass

    # def generic

    # def paintEvent(self, a0: QPaintEvent) -> None:
    #     canvasPainter = QPainter(self)
    #     canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    """
    setters
    """

    def setMode(self, mode: Mode):
        self.mode = mode

    def setBrushSize(self, size: int):
        self.brushSize = size

    def setBrushColor(self, rgb: tuple[int, int, int]):
        self.brushColor = QColor(*rgb)

    def setBrushColor(self, color: QColor):
        self.brushColor = color

    def setBgColor(self, rgb: tuple[int, int, int]):
        self.bg_color = QColor(*rgb)

    def setBgColor(self, color: QColor):
        self.bg_color = color


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PaintArea()

    ex.show()
    sys.exit(app.exec())
