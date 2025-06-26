# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

# this is from https://doc.qt.io/qtforpython-6/examples/example_widgets_widgets_charactermap.html#example-widgets-widgets-charactermap
# and modified for PyQt6 by Greg W. Moore
#

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow

"""PySide6 port of the widgets/widgets/ charactermap example from Qt6"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
