# This was Qt5 and was converted to Qt6. Original is at:
# from https://forum.pythonguis.com/t/file-image-browser-app-with-thumbnails/557
# code below has been modified, refactored and added to.
# does a grid but doesn't resize.

import glob
import math
import sys
import os

from collections import namedtuple
from PyQt6.QtCore import QAbstractTableModel, Qt, QSize
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QStyledItemDelegate

# Create a custom namedtuple class to hold our data.
preview = namedtuple("preview", "id title image")

NUMBER_OF_COLUMNS = 4
CELL_PADDING = 1 # all sides. was 20 doesn't see to have an effect.

class PreviewDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        # data is our preview object
        data = index.model().data(index, Qt.ItemDataRole.DisplayRole)
        if data is None:
            return

        width = option.rect.width() - CELL_PADDING * 2
        height = option.rect.height() - CELL_PADDING * 2

        # option.rect holds the area we are painting on the widget (our table cell)
        # scale our pixmap to fit
        scaled = data.image.scaled(
            width,
            height,
            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
        )
        # Position in the middle of the area.
        x = CELL_PADDING + (width - scaled.width()) / 2
        y = CELL_PADDING + (height - scaled.height()) / 2

        painter.drawImage(int(option.rect.x() + x), int(option.rect.y() + y), scaled)

    def sizeHint(self, option, index):
        # All items the same size.
        return QSize(300, 200)


class PreviewModel(QAbstractTableModel):
    def __init__(self, todos=None):
        super().__init__()
        # .data holds our data for display, as a list of Preview objects.
        self.previews = []

    def data(self, index, role):
        try:
            data = self.previews[index.row() * 4 + index.column() ]
        except IndexError:
            # Incomplete last row.
            return

        if role == Qt.ItemDataRole.DisplayRole:
            return data   # Pass the data to our delegate to draw.

        if role == Qt.ItemDataRole.ToolTipRole:
            return data.title

    def columnCount(self, index):
        return NUMBER_OF_COLUMNS

    def rowCount(self, index):
        n_items = len(self.previews)
        return math.ceil(n_items / NUMBER_OF_COLUMNS)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QTableView()
        self.view.horizontalHeader().hide()
        self.view.verticalHeader().hide()
        self.view.setGridStyle(Qt.PenStyle.NoPen)

        delegate = PreviewDelegate()
        self.view.setItemDelegate(delegate)
        self.model = PreviewModel()
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)
        directory = '/Volumes/DataDisk/imageTestFiles'

        # Add a bunch of images.
        image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        # for n, fn in enumerate(glob.glob("*.jpg")):
        for n, fn in enumerate(image_files):
            fqfn = os.path.join(directory, fn)
            image = QImage(fqfn)
            item = preview(n, fqfn, image)
            self.model.previews.append(item)
        self.model.layoutChanged.emit()

        self.view.resizeRowsToContents()
        self.view.resizeColumnsToContents()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
