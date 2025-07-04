# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

# this is from https://doc.qt.io/qtforpython-6/examples/example_widgets_widgetsgallery.html#example-widgets-widgetsgallery
# and modified for PyQt6 by Greg W. Moore
#

from __future__ import annotations
import sys
from PyQt6.QtWidgets import QApplication
from widgetgallery import WidgetGallery

"""PySide6 port of the widgets/gallery example from Qt v5.15
   Converted to PyQt6
"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec())
