copilot prompt:
using Python 3.10 and PyQt 6 that has a window with a directory tree that show the directory and the files in that directory. I'm having trouble understanding how to set the root path to a specific directory. I'm also having trouble with setting the width of the columns in the directory tree. It should not show the filesize or the file type columns. please add comments. this should be production quality code

I should update the prompt with PyQt version 6.4 (or 6.4.3)

response:
Alright, let’s dive into some PyQt magic. Here’s a solution with your specific requirements:
Python

Copy
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel
from PyQt6.QtCore import QModelIndex


class MainWindow(QMainWindow):
    def __init__(self, root_path):
        super().__init__()

        # Initialize the file system model
        self.model = QFileSystemModel()
        self.model.setRootPath(root_path)

        # Configure the model to hide file size and file type columns
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(root_path))
        self.tree.hideColumn(1)  # Hide file size column
        self.tree.hideColumn(2)  # Hide file type column

        # Set the width of columns
        self.tree.setColumnWidth(0, 300)  # Set width for the name column
        self.tree.setColumnWidth(3, 200)  # Set width for the date modified column

        self.setCentralWidget(self.tree)
        self.setWindowTitle('Directory Tree')
        self.setGeometry(300, 100, 800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Replace 'C:/path/to/directory' with your specific directory
    root_path = 'C:/path/to/directory'
    window = MainWindow(root_path)
    window.show()
    sys.exit(app.exec())

This code sets up a basic PyQt window displaying a directory tree, with hidden file size and type columns, and customizable column widths. Replace 'C:/path/to/directory' with the desired root path of your directory. All ready for you to test and deploy.

My prompt : update this code so its in its own class

Absolutely, let's refactor the code so that it’s encapsulated within a class for better modularity and reusability.
Python

Copy
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel
from PyQt6.QtCore import QModelIndex

class DirectoryTree:
    def __init__(self, root_path):
        self.root_path = root_path
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

Now the functionality is encapsulated within the DirectoryTree class, making it cleaner and more organized. The show() method is responsible for displaying the window. Go ahead and test it out!
