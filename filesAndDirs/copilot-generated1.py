import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QModelIndex

class DirectoryTree:
    def __init__(self, root_path):
        self.root_path = '/Users/gregm/src'
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()

        self.setupUI()

    def setupUI(self):
        self.model = QFileSystemModel()
        self.model.setRootPath(self.root_path)

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.root_path))
        self.tree.hideColumn(1)  # Hide file size column
        self.tree.hideColumn(2)  # Hide file type column

        self.tree.setColumnWidth(0, 300)  # Set width for the name column
        self.tree.setColumnWidth(3, 200)  # Set width for the date modified column

        self.window.setCentralWidget(self.tree)
        self.window.setWindowTitle('Directory Tree')
        self.window.setGeometry(300, 100, 800, 600)

    def show(self):
        self.window.show()
        sys.exit(self.app.exec())

if __name__ == '__main__':
    # Replace 'C:/path/to/directory' with your specific directory
    root_path = 'C:/path/to/directory'
    directory_tree = DirectoryTree(root_path)
    directory_tree.show()
