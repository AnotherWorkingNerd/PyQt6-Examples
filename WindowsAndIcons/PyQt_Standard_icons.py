# PyQt 6 Qt Standard icons.
# see: https://www.pythonguis.com/faq/built-in-qicons-pyqt/

# Also see:
# https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/
# https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/
# https://gist.github.com/centaurialpha/cfd7de48cb3e4d8e0d17f475b7ad3118

import sys
from PyQt6.QtWidgets import (QApplication, QGridLayout, QPushButton, QStyle,
                             QWidget)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        icons = sorted([attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")])
        layout = QGridLayout()

        for n, name in enumerate(icons):
            btn = QPushButton(name)

            pixmapi = getattr(QStyle.StandardPixmap, name)
            icon = self.style().standardIcon(pixmapi)
            btn.setIcon(icon)
            layout.addWidget(btn, int(n/4), int(n%4))

        self.setLayout(layout)


app = QApplication(sys.argv)

w = Window()
w.show()

app.exec()
