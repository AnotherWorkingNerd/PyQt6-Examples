
import os
import sys
# import string
from PyQt6.QtCore import QDir, QStorageInfo, pyqtSignal
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QTreeView, QComboBox, QLabel

# needed for CustomFileSystemModel class
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt, QDir, QSize
from PyQt6.QtGui import QFileSystemModel, QIcon

class CustomFileSystemModel(QFileSystemModel):
    # subclass QFileSystemModel and override its data() method to customize how the
    # directories are displayed. Check if a directory contains any files that match the
    # name filters that are in place and change the color of the directory and change
    # the color of the icon and .

    #   Subclassing for fun and no profit.

    def data(self, index, role):
        # QDir.addSearchPath('icon', '../assets/icons/')
        QDir.addSearchPath('icon', '../assets/')
        # if item is a directory
        if self.isDir(index):
            dir_path = self.filePath(index)
            directory = QDir(dir_path)

            # and contains filter matching files
            contains_matching_files = bool(directory.entryList(
                self.nameFilters(), QDir.Filter.Files
            ))

            # DO I WANT TO CHANGE THE ICONS and text???!?
            # Apply Custom Icons to folders
            # By default, QFileSystemModel uses native icons
            # for directories and files. To override these, you must
            # supply your own icons or use QIcon Objecta.
        # ICON SIZE MAY BE CHALLENGING.
            if role == Qt.ItemDataRole.DecorationRole:
                if contains_matching_files:
                    # return QIcon('./icons/matching_folder_icon.svg')
                    return QIcon('icon:Folder-Image-cyan.svg')
                else:
                    # return QIcon("./icons/greyed_out_folder.svg")
                    return QIcon('icon:Folder-Dashed-darkGray.svg')

            # if matches the filters then apply custom colors
            # colors are at https://doc.qt.io/qt-6/qcolorconstants.html
            # the SVG colors might be fun but maybe not consistant cross-platform.
            # for reference: Cyan = #00FFFF | darkGray = #808080
            if role == Qt.ItemDataRole.ForegroundRole:
                # return (QColor(Qt.GlobalColor.cyan) if contains_matching_files
                return (QColor(Qt.GlobalColor.green) if contains_matching_files
                    # else QColor(Qt.GlobalColor.darkGray))
                    else QColor(Qt.GlobalColor.gray))

            # and make the matching items bold
            if role == Qt.ItemDataRole.FontRole and contains_matching_files:
                return QFont("", weight=QFont.Weight.Bold)
        # Otherwise...
        return super().data(index, role)
##
# ### use it byt changeing line 90 to
#   self.model = CustomFileSystemModel()
# from:
#   self.model = QFileSystemModel()



class FileTreeView(QWidget):
    directoryChosen = pyqtSignal(str)
    fileSelected = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the file system model
        # self.model = QFileSystemModel()
        self.model = CustomFileSystemModel()
        self.model.setRootPath('')
        graphics_filters = ['*.png', '*.jpg', '*.jpeg', '*.tiff', '*.webp']
        self.model.setNameFilters(graphics_filters)
        self.model.setNameFilterDisables(False)
        self.model.setFilter(QDir.Filter.AllDirs | QDir.Filter.NoDotAndDotDot | QDir.Filter.AllEntries | QDir.Filter.System)

        # Set up the file tree view
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.rootPath()))
        self.tree.setSortingEnabled(True)
        self.tree.setAnimated(True)
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
        """Populate the dropdown with available drives or volumes using QStorageInfo."""
        drives = []
        # Directories or drives that I don't think should be shown
        # probably should add something for Windows but meh..someday.
        mac_verboten = {'TimeMachine', 'System','Libary'}
        linux_verboten = {'proc', 'sys', 'run', 'etc', 'sbin', 'bin'}

        for storage in QStorageInfo.mountedVolumes():
            if storage.isValid() and storage.isReady:
                root_path = storage.rootPath()
                volume_name = storage.displayName() or root_path
                logger.debug(f'{volume_name=}')

            # Skip certain volumes
            if sys.platform == 'darwin':
                # Exclude Time Machine volumes on macOS
                # if mac_verboten in volume_name:
                if volume_name in mac_verboten:
                    continue

            if sys.platform == 'linux':
                noslash_name = volume_name[1:] if volume_name.startswith('/') else volume_name
                if noslash_name in linux_verboten or root_path == '/':
                    continue

            # Exclude inaccessible volumes or ones with no root path
            if not root_path or not storage.isReady():
                continue

            # Add the volume name for display, and the root path for navigation
            drives.append((volume_name, root_path))

        # Populate the combo box
        for name, path in drives:
            self.driveSelector.addItem(name, path)
            # self.driveSelector.addItem(volume_name, path)

    def changeDrive(self, drive_name):
        """Change the root index of the file tree to the selected drive/volume."""
        drive_path = self.driveSelector.currentData()  # Get the root path from the combo box
        if drive_path:
            logger.debug(f'Selected drive: {drive_name}, Path: {drive_path}')
            self.model.setRootPath(drive_path)
            new_index = self.model.index(drive_path)
            self.tree.setRootIndex(new_index)

        if new_index.isValid():
            new_index = self.model.setRootPath(drive_path)  # Update model's root path
            self.tree.setRootIndex(new_index)

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
    import logging
    from pprint import pp, pprint
    from PyQt6.QtWidgets import QApplication

    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(module)s:%(lineno)s | %(message)s" )
    logger = logging.getLogger(__name__)

    app = QApplication(sys.argv)
    window = FileTreeView()
    window.show()
    sys.exit(app.exec())
