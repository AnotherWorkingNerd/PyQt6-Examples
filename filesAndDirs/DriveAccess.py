# while this works I think using Qt QStorage is a cleaner solution
# since this is a Qt app. so I went with storageinfo.py instead.
# 24Jan2025 - GMoore


import os
import sys
import string
from PyQt6.QtCore import Qt, QDir, pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QComboBox, QLabel
from PyQt6.QtGui import QFileSystemModel

class FileTreeView(QWidget):
    directoryChosen = pyqtSignal(str)
    fileSelected = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the file system model
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        graphics_filters = ['*.png', '*.jpg', '*.jpeg', '*.tiff', '*.webp']
        self.model.setNameFilters(graphics_filters)
        self.model.setNameFilterDisables(False)
        self.model.setFilter(QDir.Filter.AllDirs | QDir.Filter.NoDotAndDotDot | QDir.Filter.AllEntries | QDir.Filter.System)

        # Set up the file tree view
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(True)
        self.tree.setSortingEnabled(True)
        self.tree.setRootIndex(self.model.index(QDir.rootPath()))
        self.tree.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.tree.setIndentation(20)
        self.tree.setColumnHidden(1, True)
        self.tree.setColumnHidden(2, True)
        self.tree.setColumnHidden(3, True)

        # Connect the file selection signal
        self.tree.clicked.connect(self.onFileSelected)

        # Dropdown for drives/volumes
        self.driveSelector = QComboBox()
        self.populateDrives()
        self.driveSelector.currentTextChanged.connect(self.changeDrive)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Select Drive/Volume:"))
        layout.addWidget(self.driveSelector)
        layout.addWidget(self.tree)
        self.setLayout(layout)

    def populateDrives(self):
        """Populate the dropdown with available drives or volumes."""
        drives = []

        if sys.platform == 'win32':  # Windows
            # import string
            drives = [f"{letter}:/" for letter in string.ascii_uppercase if os.path.exists(f"{letter}:/")]
        elif sys.platform == 'darwin':  # macOS
            volumes_dir = '/Volumes'
            drives = [os.path.join(volumes_dir, d) for d in os.listdir(volumes_dir) if 'Time Machine' not in d]
            # drives.insert(0, '/')  # Add root '/' to the beginning
        else:  # Linux
            drives = ['/']  # Root filesystem
            media_dirs = ['/media', '/mnt']
            for media_dir in media_dirs:
                if os.path.exists(media_dir):
                    drives.extend([os.path.join(media_dir, d) for d in os.listdir(media_dir)])

        for drive in drives:
            self.driveSelector.addItem(drive, drive)

    # version 1
    # def changeDrive(self, drive_name):
    #     """Change the root index of the file tree to the selected drive/volume."""
    #     drive_path = self.driveSelector.currentData()  # Get the root path from the combo box
    #     index = self.model.index(drive_path)
    #     if index.isValid():
    #         self.tree.setRootIndex(index)

    # version 2
    def changeDrive(self, drive_name):
        """Change the root index of the file tree to the selected drive/volume."""
        drive_path = self.driveSelector.currentText()  # Get the selected drive text
        if os.path.exists(drive_path):  # Ensure the path exists
            index = self.model.setRootPath(drive_path)  # Update model's root path
            self.tree.setRootIndex(index)  # Set the tree's root index

    def onFileSelected(self, index):
        """Handle selection of a file or directory."""
        fqname = self.model.filePath(index)
        if os.path.isfile(fqname):
            self.fileSelected.emit(fqname)
            self.directoryChosen.emit(os.path.dirname(fqname))
        elif os.path.isdir(fqname):
            self.fileSelected.emit(None)
            self.directoryChosen.emit(fqname)


# Test the widget if running this script directly
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = FileTreeView()
    window.show()
    sys.exit(app.exec())
