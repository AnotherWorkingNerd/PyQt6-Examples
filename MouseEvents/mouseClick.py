# detect right and left mouse buttons.
# From: https://stackoverflow.com/questions/66235661/qevent-mousebuttonpress-enum-type-missing-in-pyqt6?rq=3

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget

class Widget(QWidget):

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("left")
            print(event.pos().x(), event.pos().y())
        elif event.button() == Qt.MouseButton.RightButton:
            print("right")
            print(event.pos().x(), event.pos().y())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())
